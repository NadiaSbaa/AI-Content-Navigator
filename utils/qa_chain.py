from langchain.chains.question_answering import load_qa_chain
from .data import create_knowledge_base


class QAChain:
    """
    A class to set up and manage a question-answering (QA) chain using Langchain's
    capabilities and a knowledge base built from a set of documents.

    This class provides methods to initialize the QA chain with a language model and
    to create a knowledge base from the provided documents, allowing for question
    answering over the knowledge base.
    """

    def __init__(self, documents, llm):
        """
        Initializes the QAChain object with the provided documents and a language model.

        Args:
            documents (list): A list of documents that will be used to create the knowledge base.
            llm (LangchainLLM): A language model used to power the question-answering chain.

        Attributes:
            documents (list): Stores the provided list of documents.
            qa_chain (LangchainChain): Holds the initialized QA chain after creation.
            knowledge_base (list): Stores the knowledge base created from the documents.
        """
        self.documents = documents
        self.qa_chain = None
        self.knowledge_base = None
        self.initialize_chain(llm)

    def initialize_chain(self, llm):
        """
        Initializes the question-answering chain using the provided language model and
        creates a knowledge base from the documents.

        Args:
            llm (LangchainLLM): The language model used to power the question-answering chain.

        This method sets up the `qa_chain` using the Langchain `load_qa_chain` function,
        and generates the `knowledge_base` by processing the documents with `create_knowledge_base`.
        """
        self.qa_chain = load_qa_chain(llm, chain_type="stuff")
        self.knowledge_base = create_knowledge_base(self.documents)

    def get_qa_chain(self):
        """
        Returns the initialized question-answering chain.

        Returns:
            LangchainChain: The question-answering chain object.
        """
        return self.qa_chain

    def get_knowledge_base(self):
        """
        Returns the knowledge base created from the documents.

        Returns:
            list: A list of knowledge base documents that can be used for answering questions.
        """
        return self.knowledge_base




