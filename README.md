# Chatbot Using Python APIs

This project is a fully functional chatbot backend built using Python, Flask, and the Sentence Transformers library. The chatbot can handle user questions, respond with the most relevant answers, and learn new question-answer pairs dynamically. It is hosted on [Render](https://chat-bot-using-python-apis.onrender.com/).

## 🚀 Features
- **Natural Language Understanding**: Uses pre-trained transformer models to understand user queries.
- **Dynamic Learning**: The chatbot can learn new question-answer pairs during runtime.
- **API Integration**: Exposed via RESTful API endpoints, making it easy to connect with any frontend.
- **Embeddings-based Matching**: Uses cosine similarity with sentence embeddings for accurate question matching.

## 🛠️ Technologies Used
- Python
- Flask
- Sentence Transformers (`all-MiniLM-L6-v2` model)
- JSON for knowledge base storage

## 🌐 Hosted API
The chatbot backend is hosted on Render and can be accessed at:
https://chat-bot-using-python-apis.onrender.com/

## 📋 Endpoints Documentation

### 1. `GET /`
- **Description**: Checks if the API is running.
- **Request**: No parameters required.
- **Response**: 
  ```json
  "Chatbot API is running!"
2. POST /ask
Description: Submit a question and get the most relevant answer.
Request:
Method: POST
Content-Type: application/json
Body:
json
Copy code
{
  "question": "What is Python?"
}
Response:
If a matching question is found:
json
Copy code
{
  "answer": "Python is a programming language.",
  "similarity": 0.85
}
If no match is found:
json
Copy code
{
  "answer": "Sorry, I didn't understand that.",
  "similarity": 0
}
3. POST /learn
Description: Teach the chatbot a new question-answer pair.
Request:
Method: POST
Content-Type: application/json
Body:
json
Copy code
{
  "question": "What is Flask?",
  "answer": "Flask is a web framework for Python."
}
Response:
json
Copy code
{
  "message": "New knowledge added successfully!"
}
🖥️ Running Locally
Prerequisites
Make sure you have Python installed along with pip.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/chat-bot-using-python-apis.git
cd chat-bot-using-python-apis
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask server:

bash
Copy code
python app.py
The server will run on http://localhost:5000.

Testing the API
You can use tools like Postman or curl to test the API endpoints locally:

bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"question": "What is AI?"}' http://localhost:5000/ask
🌍 Frontend Example
Here's a simple HTML page that interacts with the API:

html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Chatbot</title>
    <script>
        async function askQuestion() {
            const question = document.getElementById("question").value;
            const response = await fetch("https://chat-bot-using-python-apis.onrender.com/ask", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ question })
            });
            const data = await response.json();
            document.getElementById("response").innerText = data.answer;
        }
    </script>
</head>
<body>
    <h1>Chatbot</h1>
    <input type="text" id="question" placeholder="Ask a question" />
    <button onclick="askQuestion()">Ask</button>
    <p id="response"></p>
</body>
</html>
🚀 Deploying on Render
To deploy your chatbot on Render:

Push your project to a GitHub repository.
Create a new Web Service on Render, linking it to your GitHub repository.
Set the start command to:
bash
Copy code
python app.py
Access your deployed API using the provided Render URL.
📂 Project Structure
bash
Copy code
chat-bot-using-python-apis/
├── app.py               # Main Flask application
├── knowledge_base.json  # JSON file storing question-answer pairs
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
📜 License
This project is licensed under the MIT License. Feel free to use and modify it.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📧 Contact
For questions or feedback, please reach out to your-email@example.com.

Thank you for using the Chatbot API! 🚀😊

vbnet
Copy code

Now this is the **entire content in a single block** and you should be able to copy and paste it all at once into your `README.md` file.

Let me know if this resolves the issue or if you need further assistance!