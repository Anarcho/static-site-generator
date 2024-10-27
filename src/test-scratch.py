from htmlnode import HTMLNode, LeafNode, ParentNode, TagType
from textnode import TextNode, TextType

string_node = "This is a text with a  **bold phrase** in the middle"

node = TextNode(string_node, TextType.BOLD)

# older_nodes = [node]
# delimiter = "**"
# text_type = TextType
#
# TextNode = text, text_type, url


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        inner_result = []
        if node.text.count(delimiter) != 2:
            raise Exception("Invalid Markdown: delimiter not present in node")
        elif text_type != TextType.TEXT 

    return result 


split_nodes_delimiter([node], "**", TextType.BOLD)
