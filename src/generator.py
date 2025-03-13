from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    
    with open(from_path, "r") as file:
        markdown_content = file.read()
    
    
    with open(template_path, "r") as file:
        template_content = file.read()

    node = markdown_to_html_node(markdown_content)
    html_content = node.to_html()
    
    
    
    title = extract_title(markdown_content)
    print(f"Extracted title: {title}")

    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, "w") as file:
        file.write(final_html)