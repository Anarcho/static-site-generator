from block_markdown import (
    BlockTypes,
    block_to_block_type,
    markdown_to_blocks,
)
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_text_node
from textnode import TextType
import re

text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
test_text = (
    "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_children = text_to_children(block)
        block_parent = ParentNode("t", block_children)

    # header_count = block.count("#")
    # block_text = block.replace("#", "")
    # get_child_nodes = text_to_text_node(block_text)
    # header_node = ParentNode(f"h{header_count}", get_child_nodes)


def is_text_type(text, text_type):
    bold_pattern = r"(?<![\*_])[\*_]{2}(?![\*_])[^\*_]+[\*_]{2}(?![\*_])"
    code_pattern = r"`[^`]+`"
    italic_pattern = r"(?<![\*_])[\*_](?![\*_])[^\*_]+[\*_](?![\*_])"
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

    match text_type:
        case "bold":
            if len(re.findall(bold_pattern, text)) > 1:
                return True
            else:
                return False
        case "italic":
            if len(re.findall(italic_pattern, text)) > 1:
                return True
            else:
                return False
        case "code":
            if len(re.findall(code_pattern, text)) > 1:
                return True
            else:
                return False
        case "image":
            if len(re.findall(image_pattern, text)) > 1:
                return True
            else:
                return False
        case "link":
            if len(re.findall(link_pattern, text)) > 1:
                return True
            else:
                return False
        case _:
            return False


def text_to_children(text):
    results = []
    text_nodes = text_to_text_node(text)
    for node in text_nodes:
        results.append(LeafNode(node.text_type, node.text))
    return results


print(detect_text_type(test_text))
