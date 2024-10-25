import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, TagType, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        tag = TagType.LINK.value
        value = "This is a html node"
        children = []
        props = {"href": "http://boot.dev"}

        node = HTMLNode(tag, value, children, props)
        node2 = HTMLNode(tag, value, children, props)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        tag = TagType.LINK.value
        value = "This is a html node"
        children = []
        props = {"href": "http://boot.dev"}

        tag2 = TagType.PARAGRAPH.value
        value2 = "This is a html node"
        children2 = []
        props2 = {}

        node = HTMLNode(tag, value, children, props)
        node2 = HTMLNode(tag2, value2, children2, props2)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        tag = TagType.LINK.value
        value = "This is a html node"
        children = []
        props = {"href": "http://boot.dev"}

        tag2 = TagType.LINK.value
        value2 = "Click Me!"
        children2 = []
        props2 = {}

        node = HTMLNode(tag, value, children, props)
        node2 = HTMLNode(tag2, value2, children2, props2)
        self.assertNotEqual(node, node2)

    def test_exception_1(self):
        tag = TagType.LINK.value
        value = "This is a html node"
        children = []
        props = {"href": "http://boot.dev"}

        node = HTMLNode(tag, value, children, props)
        with self.assertRaises(Exception) as context:
            node.to_html()
        self.assertTrue("HTML Invalid: Not Implemented" in str(context.exception))

    def test_repr(self):
        tag = TagType.LINK.value
        value = "This is a html node"
        children = []
        props = {"href": "http://boot.dev"}

        node = HTMLNode(tag, value, children, props)
        self.assertEqual(
            "HTMLNode(a, \"This is a html node\", [], {'href': 'http://boot.dev'})",
            repr(node),
        )


if __name__ == "__main__":
    unittest.main()
