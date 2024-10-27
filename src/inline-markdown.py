from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        inner_result = []
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid Markdown: delimiter not present in node")
        else:
            for split in node.text.split(delimiter):
                print(split)
                text_node = None
                if node.text.split(delimiter).index(split) % 2 == 0:
                    text_node = TextNode(split, TextType.TEXT)
                else:
                    text_node = TextNode(split, text_type)
                inner_result.append(text_node)
            result.extend(inner_result)
    return result
