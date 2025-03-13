from enum import Enum
from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode

def text_node_to_html_node(text_node):
    text_type = text_node.text_type
    
    if isinstance(text_type, str):
        text_type = TextType(text_type)

    if text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_type == TextType.LINK:
        if not hasattr(text_node, 'url') or text_node.url is None:
            raise ValueError("Url is required for LINK text type")
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    elif text_type == TextType.IMAGE:
        if not hasattr(text_node, 'url') or text_node.url is None:
            raise ValueError("Url is required for IMAGE text type")
        return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception(f"invalid text type: {text_type}")