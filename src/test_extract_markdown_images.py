import unittest
from extract_markdown_images import extract_markdown_images, extract_markdown_links

def test_extract_markdown_images(self):
    matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

def test_extract_markdown_links(self):
    matches = extract_markdown_links("This is text with a link [test](https://www.example.com)")
    self.assertListEqual([("test", "https://www.example.com")], matches)