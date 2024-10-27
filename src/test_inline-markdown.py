import unittest
from textnode import TextNode, TextType
from inline-markdown import split_nodes_delimiter 

Class TestInlineMarkdown(unittest.TestCase):
    def test_bold(self):
        string_node = "This is a text with a **bold phrase** in the middle"
        node = TextNode(string_node, TextType.TEXT)
        result = f'TextNode("This is a text with a ", text, "None", TextNode("bold phrase", bold, )


