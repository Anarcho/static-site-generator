from enum import Enum
import re


class BlockTypes(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERD_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = list(map(str.strip, blocks))
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
