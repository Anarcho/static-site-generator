from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        inner_result = []
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid Markdown: delimiter not present in node")
        elif node.text_type != TextType.TEXT.value:
            inner_result.append(node)
        else:
            for split in node.text.split(delimiter):
                text_node = None
                if node.text.split(delimiter).index(split) % 2 == 0:
                    text_node = TextNode(split, TextType.TEXT)
                else:
                    text_node = TextNode(split, text_type)
                inner_result.append(text_node)
        result.extend(inner_result)
    return result


# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]


def split_nodes_image(old_nodes):
    results = []
    for node in old_nodes:
        inner_results = []
        if node.text_type != TextType.TEXT.value:
            inner_results.append(node)
        else:
            node_text = node.text
            images = extract_markdown_images(node.text)
            for image in images:
                split_by = f"![{image[0]}]({image[1]})"
                node_text_split = node_text.split(split_by, 1)
                for split in node_text_split:
                    if node_text_split.index(split) % 2 == 0:
                        if len(split) > 0:
                            inner_results.append(TextNode(split, TextType.TEXT))
                    else:
                        inner_results.append(
                            TextNode(image[0], TextType.IMAGE, image[1])
                        )
                        node_text = node_text_split[1]
                        break
            if len(node_text) > 0:
                inner_results.append(TextNode(node_text, TextType.TEXT))
        results.extend(inner_results)
    return results


def split_nodes_link(old_nodes):
    results = []
    for node in old_nodes:
        inner_results = []
        if node.text_type != TextType.TEXT.value:
            inner_results.append(node)
        else:
            images = extract_markdown_links(node.text)
            node_text = node.text
            for image in images:
                split_by = f"[{image[0]}]({image[1]})"
                node_text_split = node_text.split(split_by, 1)
                for split in node_text_split:
                    if node_text_split.index(split) % 2 == 0:
                        if len(split) > 0:
                            inner_results.append(TextNode(split, TextType.TEXT))
                    else:
                        inner_results.append(
                            TextNode(image[0], TextType.LINK, image[1])
                        )
                        node_text = node_text_split[1]
                        break
            if len(node_text) > 0:
                inner_results.append(TextNode(node_text, TextType.TEXT))
        results.extend(inner_results)
    return results


def text_to_text_node(text):
    text_node = TextNode(text, TextType.TEXT)
    result = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "*", TextType.ITALIC)
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    result = split_nodes_link(result)
    result = split_nodes_image(result)
    return result

def detect_text_node(text):
    if re.findall()


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
