import unittest

from textnode import TextNode, TextType, text_node_to_html_node

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

    def test_texttype_enum1(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_texttype_enum_img(self):
        node = TextNode("shhhhh", TextType.IMAGE, "img src")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, TextType.IMAGE.value)
        self.assertEqual(html_node.props.src, "shhhhh")

if __name__ == "__main__":
    unittest.main()


