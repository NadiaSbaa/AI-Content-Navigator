from flask import Flask, redirect, render_template, request
from data.blogs import blogs
from llms.chat_groq import ChatGroqLLM
from utils.qa_chain import QAChain
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize the ChatGroq language model and QA chain when the app starts
chat_groq_llm = ChatGroqLLM()
groq_chain = QAChain(documents=blogs, llm=chat_groq_llm.model)

# Access the QA chain and blog documents for use in answering questions
qa_chain = groq_chain.get_qa_chain()
blogs_documents = groq_chain.get_knowledge_base()


@app.route('/ask', methods=['GET'])
def ask_assistant_page():
    """
    Renders the assistant page where users can input their questions.

    Returns:
        str: The rendered HTML template for the 'ask_assistant.html' page.
    """
    return render_template('ask_assistant.html')


@app.route('/ask', methods=['POST'])
def ask_assistant():
    """
    Handles the POST request when a user submits a question to the assistant.

    Retrieves the user’s question from the form, processes it through the
    QA chain, and returns a response.

    Returns:
        str: The response generated by the QA chain for the user's question.
    """
    user_message = request.form.get("message", "")

    # Use the QA chain to get a response to the user's question
    response = qa_chain.run(input_documents=blogs_documents,
                            question=user_message)
    return response


@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors (page not found) by redirecting users to the /ask route.

    Args:
        e (Exception): The exception raised when a 404 error occurs.

    Returns:
        Response: A redirect to the /ask page.
    """
    return redirect('/ask')


if __name__ == '__main__':
    app.run(debug=True)
