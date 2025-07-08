import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node1, node2)

    def test_empty_url(self):
        node = TextNode("empty url node", TextType.TEXT)
        self.assertEqual(node.url, None)

    def test_types(self):
        node1 = TextNode("This is a text node", TextType.ITALIC_TEXT, "google.com")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "google.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()


