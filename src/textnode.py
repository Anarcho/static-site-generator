class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        if url is None:
            self.url = None
        else:
            self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"{self.text}, {self.text_type}, {self.url}"

    def is_valid_url(self):
        if self.url is not None and self.url[:8] == "https://":
            return True
        else:
            return False
