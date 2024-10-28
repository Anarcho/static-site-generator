from block_markdown import (
    BlockTypes,
    block_to_block_type,
    markdown_to_blocks,
)
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_text_node

text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_children = text_to_children(block)
        block_parent = ParentNode("t", block_children)

    # header_count = block.count("#")
    # block_text = block.replace("#", "")
    # get_child_nodes = text_to_text_node(block_text)
    # header_node = ParentNode(f"h{header_count}", get_child_nodes)


def text_to_children(text):
    results = []
    text_nodes = text_to_text_node(text)
    for node in text_nodes:
        results.append(LeafNode(node.text_type, node.text))
    return results


markdown_to_html_node(text)
