class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        if tag is None:
            self.tag = ""
            self.element_start = ""
            self.element_end = ""
        else:
            self.element_start = f"<{tag}>"
            self.element_end = f"</{tag}>"
            self.tag = tag
        if value is None:
            self.element_value = None
        else:
            self.element_value = value
        if children is None:
            self.children = []
        else:
            self.children = children
        if props is None:
            self.props = {}
        else:
            self.props = props

    def __repr__(self):
        return f"{self.element_start}{self.element_end}, {self.tag}, {self.element_value}, {self.children}, {self.props}"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        prop_list = list(map(lambda x: x[0] + '="' + x[1] + '"', self.props.items()))
        prop_string = " ".join(prop_list)
        return prop_string


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        if value is None:
            raise ValueError
        if props is None:
            return None
        else:
            self.props = props

    def to_html(self):
        if self.tag == "" or self.tag is None:
            return self.element_value
        elif self.props is None or self.props == {}:
            return f"{self.element_start}{self.element_value}{self.element_end}"
        else:
            tag_with_props = self.element_start.replace(">", " " + self.props_to_html() + ">")
            return f"{tag_with_props}{self.element_value}{self.element_end}"

class ParentNode(LeafNode):
    def __init__(self, tag, children):
        self.tag = tag
        self.children = children

    def to_html()
