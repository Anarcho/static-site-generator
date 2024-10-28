from block_markdown import BlockTypes
import re


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return blocks


def block_to_block_type(markdown_block):
    header_pattern = r"^#+\s"  # Matches Markdown headers
    code_pattern = r"`{3}"  # Matches code block delimiters (```)
    quote_pattern = r"^>\s"  # Matches blockquotes
    unordered_pattern = r"^(?:\*.*\s)+"  # Matches unordered lists (* or -)
    ordered_pattern = r"^\d+\.\s"  # Matches ordered lists (e.g., 1. Item)

    print(markdown_block)
    if len(re.findall(header_pattern, markdown_block)) > 0:
        return BlockTypes.HEADING

    elif len(re.findall(code_pattern, markdown_block)) > 0:
        return BlockTypes.CODE

    elif len(re.findall(quote_pattern, markdown_block)) > 0:
        return BlockTypes.QUOTE

    elif len(re.findall(unordered_pattern, markdown_block)) > 0:
        return BlockTypes.UNORDERED_LIST

    elif len(re.findall(ordered_pattern, markdown_block)) > 0:
        return BlockTypes.HEADING
    else:
        return BlockTypes.PARAGRAPH


text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

list_md = markdown_to_blocks(text)

for md in list_md:
    print(block_to_block_type(md))
