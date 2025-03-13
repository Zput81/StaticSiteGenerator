from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes, delimiter, text_type):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT or "![" not in old_node.text:
            result.append(old_node)
            continue
        
        images = extract_markdown_images(old_node.text)
        
        if not images:
            result.append(old_node)
            continue
        
        current_text = old_node.text

        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            
            parts = current_text.split(image_markdown, 1)

            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))
            
            result.append(TextNode(alt_text, TextType.IMAGE, url))

            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""

        if current_text:
            result.append(TextNode(current_text, TextType.TEXT))
    return result

def split_nodes_link(old_nodes, delimiter, text_type):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT or "[" not in old_node.text:
            result.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)

        if not links:
            result.append(old_node)
            continue

        current_text = old_node.text

        for text, url in links:
            links_markdown = f"[{text}]({url})"
            parts = current_text.split(links_markdown)
            
            if parts[0]:
                result.append(TextNode(parts[0],TextType.TEXT))

            result.append(TextNode(text, TextType.LINK, url))

            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""

        if current_text:
            result.append(TextNode(current_text, TextType.TEXT))
    return result