import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, TagType, LeafNode

# Tests:
# 1. To html
# 2. repr


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        tag = TagType.LINK.value
        value = "This is a html node"
        props = {"href": "http://boot.dev"}

        node = LeafNode(tag, value, props)
        node2 = LeafNode(tag, value, props)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        tag = TagType.LINK.value
        value = "This is a html node"
        props = {"href": "http://boot.dev"}

        tag2 = TagType.PARAGRAPH.value
        value2 = "This is a html node"
        props2 = {}

        node = LeafNode(tag, value, props)
        node2 = LeafNode(tag2, value2, props2)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        tag = TagType.LINK.value
        value = "This is a html node"
        props = {"href": "http://boot.dev"}

        tag2 = TagType.LINK.value
        value2 = "Click Me!"
        props2 = {}

        node = LeafNode(tag, value, props)
        node2 = LeafNode(tag2, value2, props2)
        self.assertNotEqual(node, node2)

    def test_eq_to_html(self):
        tag = TagType.LINK.value
        value = "This is a html node"
        props = {"href": "http://boot.dev"}

        node = LeafNode(tag, value, props)
        self.assertEqual(
            node.to_html(), '<a href="http://boot.dev">This is a html node</a>'
        )

    def test_exception_1(self):
        tag = TagType.LINK.value
        props = {"href": "http://boot.dev"}

        node = LeafNode(tag, None, props)
        with self.assertRaises(Exception) as context:
            node.to_html()
        self.assertTrue("Invalid LeafNode: No value provided" in str(context.exception))

    def test_repr(self):
        tag = TagType.LINK.value
        value = "This is a html node"
        props = {"href": "http://boot.dev"}

        node = LeafNode(tag, value, props)
        self.assertEqual(
            "LeafNode(a, \"This is a html node\", {'href': 'http://boot.dev'})",
            repr(node),
        )


if __name__ == "__main__":
    unittest.main()
