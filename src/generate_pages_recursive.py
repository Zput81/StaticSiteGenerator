import os
from generator import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    entries = os.listdir(dir_path_content)
    
    for entry in entries:
        source_path = os.path.join(dir_path_content, entry)
        
        if os.path.isfile(source_path) and source_path.endswith(".md"):
            rel_path = os.path.relpath(source_path, "content")
            
            if rel_path.endswith("index.md"):
                
                dest_path = os.path.join(dest_dir_path, os.path.dirname(rel_path), "index.html")
            else:
                
                filename = os.path.basename(rel_path).replace(".md", "")
                parent_dir = os.path.dirname(rel_path)
                dest_path = os.path.join(dest_dir_path, parent_dir, filename, "index.html")
            
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            generate_page(source_path, template_path, dest_path, basepath)
            
        elif os.path.isdir(source_path):
            generate_pages_recursive(source_path, template_path, dest_dir_path, basepath)