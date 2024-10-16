# AI-Content-Navigator

A simple question-answering web application that utilizes the ChatGroq language model and a knowledge base of blogs. This application allows users to interact with the assistant by asking questions and receiving answers based on the provided documents.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Suggestions](#suggestions)

## Features

- User-friendly web interface to ask questions.
- Integration with the ChatGroq language model.
- Knowledge base built from blog content.
- Handles undefined routes with user-friendly redirection.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **LangChain**: A framework for developing applications powered by language models.
- **ChatGroq**: A language model used for generating responses to user queries.
- **Python**: The programming language used for the backend logic.
- **HTML/CSS**: For rendering the frontend user interface.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/chatgroq-qa-assistant.git
   cd chatgroq-qa-assistant

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

4. **Create a .env file in the root directory: Add any necessary environment variables required for your application**
    ```bash
   GROQ_API_KEY=
   LANGCHAIN_API_KEY=

5. **Run the application**
    ```bash
   python app.py

5. **Access the application: Open your web browser and navigate to http://127.0.0.1:5000/ask**

## Usage
1. Open the application in your web browser.
2. Enter your question in the input field and submit the form.
3. The assistant will process your question and provide an answer based on the knowledge base of blogs.

## Folder Structure
    AI-Content-Navigator/
    │
    ├── data/
    │   ├── __init__.py         # Initialization file for the data module
    │   └── blogs.py            # Contains the blog data used in the application
    │
    ├── utils/                  # Utility modules for the application
    │   ├── __init__.py         # Initialization file for the utils module
    │   ├── chat_groq.py        # Module for handling the ChatGroq language model
    │   └── qa_chain.py         # Module for managing the question-answering chain
    │
    ├── templates/              # HTML templates for rendering pages
    │   ├── ask_assistant.html   # Template for the question-asking page
    │   └── ...
    │
    ├── app.py                  # Main application file
    └── requirements.txt        # List of required Python packages

## Suggestions
- **Enhance Error Handling**: Improve error messages and handling for different types of user inputs.
- **Expand Knowledge Base**: Implement a database (SQL or NoSQL) to allow for dynamic updates and management of the knowledge base with new blog entries.
- **Testing**: Add unit tests for the application to ensure stability and functionality.
- **Multi-language Support**: Introduce language detection and translation for better language support.