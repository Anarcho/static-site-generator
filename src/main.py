from textnode import TextNode
from htmlnode import HTMLNode


def main():
    text_node = TextNode("this is some text", "bold", "https://www.boot.dev")

    print(repr(text_node))

    props = {}
    props["href"] = "https://google.com"
    props["target"] = "_blank"
    test_tag = HTMLNode("p", "This is a paragraph", None, props)
    html_node = HTMLNode("p", "test text", None, props)

    print(repr(html_node))
    print(html_node.props_to_html())


main()
