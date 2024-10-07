import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_tag_construction(self):
        test_tag = HTMLNode("p", "This is a paragraph")
        self.assertEqual(test_tag.element_start, "<p>", "element created successfully")

    def test_prop_to_html(self):
        props = {}
        props["href"] = "https://google.com"
        props["target"] = "_blank"
        test_tag = HTMLNode("p", "This is a paragraph", None, props)
        test_props = test_tag.props_to_html()
        self.assertEqual(
            test_props,
            'href="https://google.com" target="_blank"',
            "sucessful prop creation",
        )

    def test_to_html_exception(self):
        test_exception = HTMLNode("p", "This is a paragraph")
        with self.assertRaises(NotImplementedError):
            test_exception.to_html()

    def test_to_html_with_props(self):
        props = {}
        props["href"] = "https://google.com"
        props["target"] = "_blank"
        test_tag = LeafNode("p", "This is a paragraph", props)
        self.assertEqual(
            test_tag.to_html(),
            '<p href="https://google.com" target="_blank">This is a paragraph</p>',
            "successfully created html element with props",
        )

    def test_to_html_no_props(self):
        test_tag = LeafNode("p", "This is a paragraph")
        self.assertEqual(
            test_tag.to_html(),
            "<p>This is a paragraph</p>",
            "successfully created html element without props",
        )
