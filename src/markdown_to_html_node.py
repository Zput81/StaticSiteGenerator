import re
from htmlnode import HTMLNode, ParentNode, LeafNode
from BlockType import block_to_block_type, BlockType
from markdown_to_blocks import markdown_to_blocks
from text_to_html import text_node_to_html_node
from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from split_nodes_image import split_nodes_image, split_nodes_link

def text_to_children(text):
    parts = [TextNode(text, TextType.TEXT)]
    
    parts = split_nodes_link(parts, "[", TextType.LINK)
    parts = split_nodes_image(parts, "![", TextType.IMAGE)
    parts = split_nodes_delimiter(parts, "`", TextType.CODE)
    parts = split_nodes_delimiter(parts, "**", TextType.BOLD)
    parts = split_nodes_delimiter(parts, "_", TextType.ITALIC)
    
    return list(text_node_to_html_node(part) for part in parts)

def create_code_block_node(block_text):
    
    lines = block_text.split('\n')
    
    if lines[0].strip().startswith('```'):
        lines = lines[1:]
    if lines and lines[-1].strip() == '```':
        lines = lines[:-1]
    
    code_content = '\n'.join(lines)
    code_node = LeafNode("code", code_content)
    return ParentNode("pre", [code_node])

def create_paragraph_node(block_text):
    children = text_to_children(block_text)
    return ParentNode("p", children)

def create_heading_node(block_text):
    level = 0
    for char in block_text:
        if char == '#':
            level += 1
        else:
            break
    html_content = block_text[level:].strip()

    children = text_to_children(html_content)
    
    return ParentNode(f"h{level}", children)

def create_quote_node(block_text):
    
    lines = block_text.split('\n')
    cleaned_lines = [line.strip()[1:].strip() if line.strip().startswith('>') else line.strip() for line in lines]
    cleaned_text = '\n'.join(cleaned_lines)
    
    children = text_to_children(cleaned_text)
    return ParentNode("blockquote", children)

def create_unordered_list_node(block_text):
    items = [line.strip()[2:] for line in block_text.split('\n') if line.strip().startswith('- ')]
    li_nodes =[]
    for item in items:
        item_children = text_to_children(item)
        li_node = ParentNode("li", item_children)
        li_nodes.append(li_node)
    return ParentNode("ul", li_nodes)

def create_ordered_list_node(block_text):
    lines = [line.strip() for line in block_text.split('\n') if line.strip()]
    items = []
    for line in lines:
        match = re.match(r'^\d+\.\s+(.*)', line)
        if match:
            items.append(match.group(1))
    li_nodes = []
    for item in items:
        item_children = text_to_children(item)
        li_node = ParentNode("li", item_children)
        li_nodes.append(li_node)
    return ParentNode("ol", li_nodes)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH:
            children.append(create_paragraph_node(block))
        elif block_type == BlockType.HEADING:
            children.append(create_heading_node(block))
        elif block_type == BlockType.CODE:
            children.append(create_code_block_node(block))
        elif block_type == BlockType.QUOTE:
            children.append(create_quote_node(block))
        elif block_type == BlockType.UNORDERED_LIST:
            children.append(create_unordered_list_node(block))
        elif block_type == BlockType.ORDERED_LIST:
            children.append(create_ordered_list_node(block))
        else:
            raise ValueError(f"Unknown block type: {block_type}")
    
    return ParentNode("div", children)

        
        
