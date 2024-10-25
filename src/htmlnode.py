from enum import Enum


class TagType(Enum):
    PARAGRAPH = "p"
    BOLD = "b"
    ITALIC = "i"
    LINK = "a"


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value

        if children is None or children == []:
            self.children = []
        else:
            self.children = children

        if props is None or props == {}:
            self.props = {}
        else:
            self.props = props

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self):
        return f'HTMLNode({self.tag}, "{self.value}", {self.children}, {self.props})'

    def to_html(self):
        raise NotImplementedError("HTML Invalid: Not Implemented")

    def props_to_html(self):
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())


class HTMLNodeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class LeafNodeError(HTMLNodeError):
    def __init__(self, tag=None, message=None):
        if tag is None:
            self.message = message
        else:
            self.message = f"Invalid LeafNode: Error in tag {tag}: {message}"
        super().__init__(message)


class ParentNodeError(HTMLNodeError):
    def __init__(self, tag=None, message=None):
        if tag is None:
            self.message = message
        else:
            self.message = f"Invalid ParentNode: Error in tag {tag}: {message}"
        super().__init__(message)


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None or self.value == "":
            raise LeafNodeError(None, "Invalid LeafNode: No value provided")
        try:
            if self.tag is None or self.tag == "":
                return self.value
            elif self.props and len(self.props) > 0:
                leaf_props = self.props_to_html()
                return f"<{self.tag} {leaf_props}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
        except ValueError as e:
            raise LeafNodeError(None, str(e))
        except Exception as e:
            raise LeafNodeError(self.tag, str(e))

    def __repr__(self):
        return f'LeafNode({self.tag}, "{self.value}", {self.props})'


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        result = ""
        if self.tag is None or self.tag == "":
            raise ParentNodeError(None, "Invalid ParentNode: No tag provided")
        if self.children is None or self.children == []:
            raise ParentNodeError(None, "Invalid ParentNode: No children provided")
        try:
            for child in self.children:
                result += child.to_html()
            if self.props and len(self.props) > 0:
                parent_props = self.props_to_html()
                return f"<{self.tag} {parent_props}>{result}</{self.tag}>"
            else:
                return f"<{self.tag}>{result}</{self.tag}>"
        except LeafNodeError as e:
            raise ValueError(f"{str(e)}")
        except ParentNodeError as e:
            raise ValueError(f"{str(e)}")
        except Exception as e:
            raise ParentNodeError(self.tag, str(e))

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
