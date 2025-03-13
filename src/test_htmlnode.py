import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://example.com","target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://example.com" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        result = node.props_to_html()
        self.assertEqual(result, '')

    def test_props_to_html_none(self):
        node = HTMLNode()
        result = node.props_to_html()
        self.assertEqual(result, '')

    def test_props_to_html_non_string_values(self):
        node = HTMLNode(props={"data-id": 123, "disabled": None})
        result = node.props_to_html()
        self.assertEqual(result, ' data-id="123" disabled="None"')

    