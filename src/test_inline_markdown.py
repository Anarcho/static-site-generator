from contextlib import suppress
from typing import Text
import unittest
from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_text_node,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode(
            "This is text with **bold text** located in the middle", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" located in the middle", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_double_bold(self):
        node = TextNode(
            "This is text with **bold text** located in the middle with **some here** as well",
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" located in the middle with ", TextType.TEXT),
                TextNode("some here", TextType.BOLD),
                TextNode(" as well", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode(
            "This is text with *italic* located in the middle", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" located in the middle", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_double_italic(self):
        node = TextNode(
            "This is text with *italic text* located in the middle with *some here* as well",
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("italic text", TextType.ITALIC),
                TextNode(" located in the middle with ", TextType.TEXT),
                TextNode("some here", TextType.ITALIC),
                TextNode(" as well", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_extract_images(self):
        text = "This is a text with a ![rick roll](https://google.com/rick-roll.gif) image and a ![obi wan](https://google.com/images/obi-wan.jpeg) image"
        extract_images = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("rick roll", "https://google.com/rick-roll.gif"),
                ("obi wan", "https://google.com/images/obi-wan.jpeg"),
            ],
            extract_images,
        )

    def test_extract_links(self):
        text = "This is a text with a [rick roll](https://google.com/rick-roll.gif) link and a [obi wan](https://google.com/images/obi-wan.jpeg) link"
        extract_link = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("rick roll", "https://google.com/rick-roll.gif"),
                ("obi wan", "https://google.com/images/obi-wan.jpeg"),
            ],
            extract_link,
        )

    def test_split_link(self):
        node = TextNode(
            "This is a text with a [rick roll](https://google.com/rick-roll.gif) link and a [obi wan](https://google.com/images/obi-wan.jpeg) link",
            TextType.TEXT,
        )
        node2 = TextNode(
            "[rick roll](https://google.com/rick-roll.gif) link and a [obi wan](https://google.com/images/obi-wan.jpeg)",
            TextType.TEXT,
        )
        list_of_nodes = [node, node2]
        results = split_nodes_link(list_of_nodes)
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode(
                    "rick roll", TextType.LINK, "https://google.com/rick-roll.gif"
                ),
                TextNode(" link and a ", TextType.TEXT),
                TextNode(
                    "obi wan", TextType.LINK, "https://google.com/images/obi-wan.jpeg"
                ),
                TextNode(" link", TextType.TEXT),
                TextNode(
                    "rick roll", TextType.LINK, "https://google.com/rick-roll.gif"
                ),
                TextNode(" link and a ", TextType.TEXT),
                TextNode(
                    "obi wan", TextType.LINK, "https://google.com/images/obi-wan.jpeg"
                ),
            ],
            results,
        )

    def test_split_images(self):
        node = TextNode(
            "This is a text with a ![rick roll](https://google.com/rick-roll.gif) image and a ![obi wan](https://google.com/images/obi-wan.jpeg) image",
            TextType.TEXT,
        )
        node2 = TextNode(
            "![rick roll](https://google.com/rick-roll.gif) image and a ![obi wan](https://google.com/images/obi-wan.jpeg)",
            TextType.TEXT,
        )
        list_of_nodes = [node, node2]
        results = split_nodes_image(list_of_nodes)
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode(
                    "rick roll", TextType.IMAGE, "https://google.com/rick-roll.gif"
                ),
                TextNode(" image and a ", TextType.TEXT),
                TextNode(
                    "obi wan", TextType.IMAGE, "https://google.com/images/obi-wan.jpeg"
                ),
                TextNode(" image", TextType.TEXT),
                TextNode(
                    "rick roll", TextType.IMAGE, "https://google.com/rick-roll.gif"
                ),
                TextNode(" image and a ", TextType.TEXT),
                TextNode(
                    "obi wan", TextType.IMAGE, "https://google.com/images/obi-wan.jpeg"
                ),
            ],
            results,
        )

    def test_to_text_node(self):
        result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_to_test = text_to_text_node(text)
        self.assertListEqual(result, text_to_test)


if __name__ == "__main__":
    unittest.main()
