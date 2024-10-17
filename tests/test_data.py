from langchain.docstore.document import Document
from utils.data import create_knowledge_base


def test_create_knowledge_base_with_valid_data():
    blogs = [
        {
            "name": "Blog 1",
            "content": ["This is the first sentence.", "Here is another sentence."]
        },
        {
            "name": "Blog 2",
            "content": ["Second blog content goes here.", "More content for blog 2."]
        }
    ]

    result = create_knowledge_base(blogs)

    # Assert
    assert len(result) == 2
    assert isinstance(result[0], Document)
    assert isinstance(result[1], Document)
    assert result[0].page_content == "Blog: Blog 1\nContent: This is the first sentence., Here is another sentence."
    assert result[1].page_content == "Blog: Blog 2\nContent: Second blog content goes here., More content for blog 2."


def test_create_knowledge_base_with_empty_blog_list():
    blogs = []
    result = create_knowledge_base(blogs)

    # Assert
    assert result == []


def test_create_knowledge_base_with_empty_blog_content():
    blogs = [
        {
            "name": "Empty Blog",
            "content": []
        }
    ]
    result = create_knowledge_base(blogs)

    # Assert
    assert len(result) == 1
    assert isinstance(result[0], Document)
    assert result[0].page_content == "Blog: Empty Blog\nContent: "

