import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_noteqtext(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text node here", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_notequrl(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD,"www.testexample.com")
        self.assertNotEqual(node, node2)

    def test_noteqwhole(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text node here", TextType.ITALIC, "www.testexample.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()