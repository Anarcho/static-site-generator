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
    header_pattern = r"^#{1,6}\s.+$"
    code_pattern = r"```[\s\S]*?```"
    quote_pattern = r"^>\s.+$"
    unordered_pattern = r"^\s*[-*+]\s.+$"
    ordered_pattern = r"^\s*\d+\.\s.+$"

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
