from flask import Flask, request, jsonify
import json
from typing import Optional
from sentence_transformers import SentenceTransformer, util
from flask_cors import CORS

# Initialize the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

app = Flask(__name__)
CORS(app)                           #

# Load the knowledge base from a JSON file
def load_knowledge_base(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        if "questions" not in data:
            data["questions"] = []
        return data
    except FileNotFoundError:
        return {"questions": []}
    except json.JSONDecodeError:
        return {"questions": []}

# Save the knowledge base to a JSON file
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Embed the questions in the knowledge base
def embed_questions(knowledge_base: dict):
    questions = [q["question"] for q in knowledge_base["questions"]]
    if not questions:
        return questions, None
    question_embeddings = model.encode(questions)
    return questions, question_embeddings

# Find the best match for a user's question
def find_best_match(user_question: str, questions: list[str], question_embeddings):
    if question_embeddings is None or question_embeddings.size == 0 or len(questions) == 0:
        return None, 0
    user_embedding = model.encode(user_question)
    similarities = util.cos_sim(user_embedding, question_embeddings)[0]
    best_match_idx = similarities.argmax()
    highest_score = similarities[best_match_idx]
    if highest_score >= 0.7:  # Define a similarity threshold
        return best_match_idx, highest_score.item()
    return None, 0

# Load the knowledge base at startup
knowledge_base = load_knowledge_base("knowledge_base.json")
questions, question_embeddings = embed_questions(knowledge_base)

# API endpoint to handle questions
@app.route('/ask', methods=['POST'])
def ask_question():
    user_input = request.json.get("question")
    if not user_input:
        return jsonify({"error": "No question provided"}), 400

    # Find the best match
    best_match_idx, score = find_best_match(user_input, questions, question_embeddings)
    if best_match_idx is not None:
        answer = knowledge_base["questions"][best_match_idx]["answer"]
        return jsonify({"answer": answer, "similarity": score})
    else:
        return jsonify({"answer": "Sorry, I didn't understand that.", "similarity": 0})

# Endpoint to add new questions to the knowledge base
@app.route('/learn', methods=['POST'])
def learn_question():
    new_question = request.json.get("question")
    new_answer = request.json.get("answer")
    if not new_question or not new_answer:
        return jsonify({"error": "Both question and answer are required"}), 400

    # Add the new question and answer to the knowledge base
    knowledge_base["questions"].append({"question": new_question, "answer": new_answer})
    save_knowledge_base("knowledge_base.json", knowledge_base)
    
    # Recompute embeddings
    global questions, question_embeddings
    questions, question_embeddings = embed_questions(knowledge_base)
    
    return jsonify({"message": "New knowledge added successfully!"})

# A simple route to check if the API is running
@app.route('/', methods=['GET'])
def home():
    return "!!!!! Its Working broooo !!!!!!!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
