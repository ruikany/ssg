from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "regular text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    #constructor
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    #override
    def __eq__(self, other):
        if self.text != other.text or self.text_type != other.text_type or self.url != other.url:
            return False
        return True
    # override    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html(textNode):
        if textNode.text_type.value == TextType.TEXT:
            return LeafNode(None, textNode.text)
        elif textNode.text_type.value == TextType.BOLD:
            return LeafNode("b", textNode.text)
        elif textNode.text_type.value == TextType.ITALIC:
            return LeafNode("i", textNode.text)
        elif textNode.text_type.value == TextType.CODE:
            return LeafNode("code", textNode.text)
        elif textNode.text_type.value == TextType.LINK:
            # do i need to specify None for children arg?
            return LeafNode("a", textNode.text, None, props={"href": f"{textNode.url}"})
        elif textNode.text_type.value == TextType.IMAGE:
            return LeafNode("img", "", None, props={"src": f"{textNode.url}", "alt": f"{textNode.text}"})
