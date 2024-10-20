from htmlnode import LeafNode, ParentNode


node = ParentNode(
    "p",
    [
        LeafNode("a", "click me!", {"href": "http://boot.dev"}),
        LeafNode(None, "Normal Text"),
        LeafNode("i", None),
        LeafNode(None, "Normal"),
    ],
)


node2 = ParentNode(
    "p",
    [
        LeafNode("a", "click me!", {"href": "http://boot.dev"}),
        LeafNode(None, "Normal Text"),
        LeafNode("i", "Italic"),
        LeafNode(None, "Normal"),
        ParentNode("p", None, None),
    ],
    {"href": "http://boot.dev"},
)

try:
    node.to_html()
except Exception as e:
    print(str(e))


try:
    node2.to_html()
except Exception as e:
    print(str(e))
