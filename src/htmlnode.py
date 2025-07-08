class HTMLNode:
    """constructor
    
    tag: string representing HTML tag
    value: value of HTML tag
    children: list of children HTMLNode objs
    props: dictionary of attrs of HTML tag
    """
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_str = ""
        for key in self.props.keys():
            html_str += f" {key}=\"{self.props[key]}\""
        return html_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

