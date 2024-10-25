from logging import exception
import unittest
from htmlnode import TagType, LeafNode, ParentNode, LeafNodeError, ParentNodeError

# Tests:
# 1. Test to html
# 2. Test repr
# 3. Test Exceptions - no tag, no children, child invalid tag, parent child invalid tag


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        tag = TagType.LINK.value
        props = {"href": "http://boot.dev"}
        children = [
            LeafNode("a", "click me!", {"href": "http://boot.dev"}),
            LeafNode(None, "Normal Text"),
            LeafNode("i", "Italic Text"),
            LeafNode(None, "Normal"),
            ParentNode("p", [LeafNode(None, "Normal")], {"href": "http://boot.dev"}),
        ]

        node = ParentNode(tag, children, props)
        node2 = ParentNode(tag, children, props)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        tag = TagType.LINK.value
        props = {"href": "http://boot.dev"}
        children = [
            LeafNode("a", "click me!", {"href": "http://boot.dev"}),
            LeafNode(None, "Normal Text"),
            LeafNode("i", "Italic Text"),
            LeafNode(None, "Normal"),
            ParentNode("p", [LeafNode(None, "Normal")], {"href": "http://boot.dev"}),
        ]
        tag2 = TagType.LINK.value
        props2 = {"href": "http://boot.dev"}
        children2 = [
            LeafNode("a", "click me!", {"href": "http://boot.dev"}),
            LeafNode(None, "Normal Text"),
            LeafNode(None, "Italic Text"),
            LeafNode(None, "Normal"),
            ParentNode("p", [LeafNode(None, "Normal")], {"href": "http://boot.dev"}),
        ]

        node = ParentNode(tag, children, props)
        node2 = ParentNode(tag2, children2, props2)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        tag = TagType.LINK.value
        props = {"href": "http://boot.dev"}
        children = [
            LeafNode("a", "click me!", {"href": "http://boot.dev"}),
            LeafNode(None, "Normal Text"),
            LeafNode("i", "Italic Text"),
            LeafNode(None, "Normal"),
            ParentNode("p", [LeafNode(None, "Normal")], {"href": "http://boot.dev"}),
        ]

        tag2 = TagType.LINK.value
        children2 = [
            LeafNode("a", "click me!", {"href": "http://boot.dev"}),
            LeafNode(None, "Normal Text"),
            LeafNode("i", "Italic Text"),
            LeafNode(None, "Normal"),
            ParentNode("p", [LeafNode(None, "Normal")], {"href": "http://boot.dev"}),
        ]

        node = ParentNode(tag, children, props)
        node2 = ParentNode(tag, children2, None)
        self.assertNotEqual(node, node2)

    def test_eq_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            f"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )


if __name__ == "__main__":
    unittest.main()
