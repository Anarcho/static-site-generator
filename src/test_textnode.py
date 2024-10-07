import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_valid_url(self):
        test_url_return = TextNode("test 1", "bold", "https://www.google.com")
        self.assertEqual(
            test_url_return.is_valid_url(), True, "valid url test successful"
        )

    def test_invalid_url(self):
        test_url_return = TextNode("test 2", "bold", "www.google.com")
        self.assertEqual(
            test_url_return.is_valid_url(), False, "invalid url est successful"
        )

    def test_url_none(self):
        test_url_return = TextNode("test 2", "bold")
        self.assertEqual(test_url_return.url, None, "url none return is successful")

    def test_url_not_none(self):
        test_url_return = TextNode("test 2", "bold", "https://test.com")
        self.assertEqual(
            test_url_return.url, "https://test.com", "url return is successful"
        )
