import unittest
from htmlnode import LeafNode

def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

def test_leaf_to_html_a_with_props(self):
    node = LeafNode("a", "Click here", {"href": "https://example.com"})
    self.assertEqual(node.to_html(), '<a href="https://example.com">Click here</a>')

def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, "This is just raw text.")
    self.assertEqual(node.to_html(), "This is just raw text.")

def test_leaf_to_html_missing_value(self):
    with self.assertRaises(ValueError):
        node = LeafNode("p", None)
        node.to_html()