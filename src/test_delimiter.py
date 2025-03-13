import unittest
from delimiter import split_nodes_delimiter
from textnode import TextType, TextNode

def test_split_nodes_delimiter_bold():
    node = TextNode("this is a text with a **bolded** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node],"**", TextType.BOLD)
    assert len(new_nodes) == 3
    assert new_nodes[0].text == "this is a text with a "
    assert new_nodes[0].text_type == TextType.TEXT
    assert new_nodes[1].text == "bolded"
    assert new_nodes[1].text_type == TextType.BOLD
    assert new_nodes[2].text == " word"
    assert new_nodes[2].text_type == TextType.TEXT

def test_split_nodes_delimiter_italic():
    node = TextNode("this is a text with a _italicized_ word", TextType.ITALIC)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    assert len(new_nodes) == 3
    assert new_nodes[0].text == "this is a text with a "
    assert new_nodes[0].text_type == TextType.TEXT
    assert new_nodes[1].text == "italicized"
    assert new_nodes[1].text_type == TextType.ITALIC
    assert new_nodes[2].text == " word"
    assert new_nodes[2].text_type == TextType.TEXT

def test_split_nodes_delimiter_code():
    node = TextNode("this is text with a `code block` word", TextType.CODE)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    assert len(new_nodes) == 3
    assert new_nodes[0].text == "this is text with a "
    assert new_nodes[0].text_type == TextType.TEXT
    assert new_nodes[1].text == "code block"
    assert new_nodes[1].text_type == TextType.CODE
    assert new_nodes[2].text == " word"
    assert new_nodes[2].text_type == TextType.TEXT