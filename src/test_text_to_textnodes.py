import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_example_case(self):
        text = text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(len(expected), len(actual))
        for i in range(len(expected)):
            self.assertEqual(expected[i].text, actual[i].text)
            self.assertEqual(expected[i].text_type, actual[i].text_type)
            self.assertEqual(expected[i].url, actual[i].url)

    def test_bold_text(self):
        text = "This is a **bold** text"
        expected = [
        TextNode("This is a ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" text", TextType.TEXT)
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(len(expected), len(actual))
        for i in range(len(expected)):
            self.assertEqual(expected[i].text, actual[i].text)
            self.assertEqual(expected[i].text_type, actual[i].text_type)
            self.assertEqual(expected[i].text, actual[i].text)
            if expected[i].text_type in [TextType.LINK, TextType.IMAGE]:
                self.assertEqual(expected[i].url, actual[i].url)

def test_italic_text(self):
    text = "This is _italic_ text"
    expected = [
        TextNode("This is ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" text", TextType.TEXT)
    ]
    actual = text_to_textnodes(text)
    self.assertEqual(len(expected), len(actual))
    for i in range(len(expected)):
        self.assertEqual(expected[i].text, actual[i].text)
        self.assertEqual(expected[i].text_type, actual[i].text_type)
        self.assertEqual(expected[i].text, actual[i].text)
        if expected[i].text_type in [TextType.LINK, TextType.IMAGE]:
            self.assertEqual(expected[i].url, actual[i].url)

def test_code_text(self):
    text = "This is a `code block` text"
    expected = [
        TextNode("This is a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" text", TextType.TEXT)
    ]
    actual = text_to_textnodes(text)
    self.assertEqual(len(expected), len(actual))
    for i in range (len(expected)):
        self.assertEqual(expected[i].text, actual[i].text)
        self.asssertEqual(expected[i].text_type, actual[i].text_type)
        self.assertEqual(expected[i].text, actual[i].text)
        if expected[i].text_type in [TextType.LINK, TextType.IMAGE]:
            self.assetEqual(expected[i].url, actual[i].url)

def test_image_node(self):
    text = "This is an ![image alt text](https://example.com/image.jpg) in text"
    expected = [
        TextNode("This is an ", TextType.TEXT),
        TextNode("image alt text", TextType.IMAGE, "https://example.com/image.jpg"),
        TextNode(" in text", TextType.TEXT)
    ]
    actual = text_to_textnodes(text)
    self.assertEqual(len(expected), len(actual))
    for i in range(len(expected)):
        self.assertEqual(expected[i].text, actual[i].text)
        self.assertEqual(expected[i].text_type, actual[i].text_type)
        if expected[i].text_type == TextType.IMAGE:
            self.assertEqual(expected[i].url, actual[i].ur)

def test_link_node(self):
    text = "This is a [link text](https://example.com) in text"
    expected = [
        TextNode("This is a ", TextType.TEXT),
        TextNode("link text", TextType.LINK, "https://example.com"),
        TextNode(" in text", TextType.TEXT)
    ]
    actual = text_to_textnodes(text)
    self.assertEqual(len(expected), len(actual))
    for i in range(len(expected)):
        self.assertEqual(expected[i].text, actual[i].text)
        self.assertEqual(expected[i].text_type, actual[i].text_type)
        if expected[i].text_type == TextType.LINK:
            self.assertEqual(expected[i].url, actual[i].url)