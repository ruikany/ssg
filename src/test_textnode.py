import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_empty_url(self):
        node = TextNode("empty url node", TextType.TEXT)
        self.assertEqual(node.url, None)

    def test_types(self):
        node1 = TextNode("This is a text node", TextType.ITALIC, "google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "google.com")
        self.assertNotEqual(node1, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()


