from htmlnode import HTMLNode, LeafNode, ParentNode, TagType


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

node3 = ParentNode(
    "p",
    [
        LeafNode("a", "click me!", {"href": "http://boot.dev"}),
        LeafNode(None, "Normal Text"),
        LeafNode("i", "Italic"),
        LeafNode(None, "Normal"),
        ParentNode("p", [LeafNode(None, "Normal")], {"href": "http://boot.dev"}),
    ],
    {"href": "http://boot.dev"},
)

tag = TagType.LINK.value
value = "This is a html node"
children = []
props = {"href": "http://boot.dev"}

node4 = HTMLNode(tag, value, children, props)

try:
    node.to_html()
except Exception as e:
    print(str(e))


try:
    node2.to_html()
except Exception as e:
    print(str(e))
print(node3.to_html())

print(node4.props_to_html())
