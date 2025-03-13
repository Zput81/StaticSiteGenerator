import re

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if re.match(r'^# ', line):
            return line[2:].strip()
        
    raise Exception("No h1 header found in markdown")