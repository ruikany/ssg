import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode("p", "this a paragraph node", props={"href": "https://www.google.com", "target": "_blank"})
        expected = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(html_node.props_to_html(), expected)

    def test_to_string(self):
        html_node = HTMLNode("p", "this a paragraph node", props={"href": "https://www.google.com", "target": "_blank"})
        expected = f"HTMLNode(p, this a paragraph node, None, {html_node.props})"
        self.assertEqual(repr(html_node), expected)
        
    def test_empty(self):
        html_node = HTMLNode()
        expected = "HTMLNode(None, None, None, None)"
        self.assertEqual(repr(html_node), expected)


if __name__ == "__main__":
    unittest.main()

