from textnode import TextNode
from textnode import TextType

def main():
    test = TextNode("hi", TextType.BOLD_TEXT, "https://www.boot.dev")
    print(test)

main()

