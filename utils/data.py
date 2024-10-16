from langchain.docstore.document import Document


def create_knowledge_base(blogs):
    """
    Converts a list of blog data into a list of Langchain Document objects.

    Args:
        blogs (list): A list of dictionaries where each dictionary contains 'name' and 'content'
                      of a blog. 'content' is a list of strings.

    Returns:
        list: A list of Document objects, each representing the content of a blog.
    """
    documents = []
    for blog in blogs:
        content = f"Blog: {blog['name']}\nContent: {', '.join(blog['content'])}"
        documents.append(Document(page_content=content))
    return documents
