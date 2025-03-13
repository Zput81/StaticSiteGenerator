from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def is_ordered_list(block):
    lines= block.split('\n')
    for i, line in enumerate(lines):
        expected_prefix = f"{i+1}."
        if not line.startswith(expected_prefix):
            return False
    return True

def is_unordered_list(block):
    lines = block.split('\n')
    for i, line in enumerate(lines):
        expected_prefix = f"- "
        if not line.startswith(expected_prefix):
            return False
    return True

def is_quote(block):
    lines = block.split('\n')
    for line in lines:
        if not line.startswith('>'):
            return False
    return True

def block_to_block_type(block):
    match block:
        case _ if block.startswith('#'):
            return BlockType.HEADING
        case _ if block.startswith('```'):
            return BlockType.CODE
        case _ if is_quote(block):
            return BlockType.QUOTE
        case _ if is_ordered_list(block):
            return BlockType.ORDERED_LIST
        case _ if is_unordered_list(block):
            return BlockType.UNORDERED_LIST
        case _:
            return BlockType.PARAGRAPH