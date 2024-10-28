from block_markdown import (
    BlockTypes,
    block_to_block_type,
    markdown_to_blocks,
)
from htmlnode import HTMLNode

text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""


def markdown_to_html_node(markdown):
    split_to_blocks = markdown_to_blocks(markdown)

    for block in split_to_blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockTypes.HEADING:
                header_count = block.count("#")
                block_text = block.replace("#", "")
                header_node = HTMLNode(f"h{header_count}", block_text.strip())
            case _:
                print("null")


print(markdown_to_html_node(text))
