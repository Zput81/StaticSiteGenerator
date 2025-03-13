import unittest
from BlockType import BlockType, block_to_block_type

def test_block_to_block_type():
    assert block_to_block_type("This is a paragraph") == BlockType.PARAGRAPH
    
    assert block_to_block_type("# Heading 1") == BlockType.HEADING
    assert block_to_block_type("## Heading 2") == BlockType.HEADING
    
    assert block_to_block_type("```\ncode here\n```") == BlockType.CODE
    
    assert block_to_block_type("> This is a quote\n> Another line") == BlockType.QUOTE
    
    assert block_to_block_type("- Item 1\n- Item 2") == BlockType.UNORDERED_LIST

    assert block_to_block_type("1. First\n2. Second") == BlockType.ORDERED_LIST

