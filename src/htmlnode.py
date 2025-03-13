class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError("Subclasses must implement to_html")
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        return " " + props_str if props_str else ""


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value="", props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.tag is None:
            return self.value
        self_closing_tags = ["img", "br", "hr", "input", "meta", "link"]
        if self.tag in self_closing_tags:
            return f"<{self.tag}{self.props_to_html()} />"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children or [], props)
    
    def to_html(self):
        if self.tag is None:
            return "".join([child.to_html() for child in self.children])
        
        children_html = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"