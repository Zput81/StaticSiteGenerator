from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    nodes = split_nodes_image(nodes, "![", "image")
    
    nodes = split_nodes_link(nodes, "[", "link")
    
    return nodes