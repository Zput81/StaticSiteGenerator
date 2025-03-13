import os
import shutil
from generator import generate_page
from generate_pages_recursive import generate_pages_recursive
import sys

basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

def copy_static_recursive(src, dst):
    """
    Recursively copy files from src to dst.
    First removes dst if it exists.
    """
    
    print(f"Copying from {src} to {dst}")
    
    os.makedirs(os.path.dirname(dst), exist_ok=True)

    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    
    os.mkdir(dst)
    
    
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dst_item = os.path.join(dst, item)
        
        if os.path.isfile(src_item):
            
            print(f"Copying file: {src_item} -> {dst_item}")
            shutil.copy(src_item, dst_item)
        elif os.path.isdir(src_item):
            
            print(f"Found directory: {src_item}")
            copy_static_recursive(src_item, dst_item)

def main():
    copy_static_recursive("static", "docs/static")
   
    generate_pages_recursive("content", "template.html", "docs", basepath)
    
if __name__ == "__main__":
    main()