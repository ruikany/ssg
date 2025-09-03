import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        leaf_node = LeafNode("p", "Hello world")
        expected = "<p>Hello world</p>"
        actual = f"{leaf_node.to_html()}"
        self.assertEqual(expected, actual)

    def test_leaf_to_html_props(self):
        leaf_node = LeafNode("a", "Click here for free robux", props={"href": "https://www.google.com", "target": "_blank"})
        expected = "<a href=\"https://www.google.com\" target=\"_blank\">Click here for free robux</a>"
        actual = leaf_node.to_html()
        self.assertEqual(expected, actual)

    def test_leaf_to_html_empty(self):
        with self.assertRaises(ValueError):
            leaf_node = LeafNode("p")
            leaf_node.to_html()

if __name__ == "__main__":
    unittest.main()
