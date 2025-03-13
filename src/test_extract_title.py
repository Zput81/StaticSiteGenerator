import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_h1_header(self):
        self.assertEqual(extract_title("# Hello World"), "Hello World")

    def test_h1_with_other_content(self):
        markdown = "# title\nSome content\n## Subtitle"
        self.assertEqual(extract_title(markdown), "title")

    def test_h1_with_extra_whitespace(self):
        self.assertEqual(extract_title("#     Spacey Title     "), "Spacey Title")

    def test_no_h1_header(self):
        with self.assertRaises(Exception):
            extract_title("")
    
    def test_only_h2_header(self):
        with self.assertRaises(Exception):
            extract_title("## Only h2 header")

    def test_no_header(self):
        with self.assertRaises(Exception):
            extract_title("no header here")

if __name__ == "__main__":
    unittest.main()