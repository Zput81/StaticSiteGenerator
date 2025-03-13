import unittest
from split_nodes_image import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def test_split_links(self):
    node = TextNode(
        "This is text with a [link](https://example.com) and another [second link](https://example.org)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node], "[", "link")
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://example.org"),
        ],
        new_nodes,
    )

def test_split_images(self):
    node = TextNode(
        "This is a text with a ![image](https://example.org/image.png) and another ![second image](https://example.com/image.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node], "![", "link")
    self.assertListEqual(
        [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.org/image.png"),
            TextNode("and another", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://example.com/image.png"),
        ],
        new_nodes,
    )

def test_split_single_image(self):
    node = TextNode(
        "This is text with just one ![image](https://example.com/image.png) in it.",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node], "![", "link")
    self.assertListEqual(
        [
            TextNode("This is text with just one ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" in it.", TextType.TEXT),
        ],
        new_nodes,
    )

def test_split_single_link(self):
    node = TextNode(
        "This is text with just one [link](https://example.com) in it.",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node], "[", "link")
    self.assertListEqual(
        [
            TextNode("This is text with just one ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" in it.", TextType.TEXT),
        ],
        new_nodes,
    )

