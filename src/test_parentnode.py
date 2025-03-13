from html import ParentNode, LeafNode

def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

def test_to_html_with_one_child(self):
    parent = ParentNode("div", [LeafNode("span", "text")])
    expected = "<div><span>text</span></div>"
    assert parent.to_html()

def test_to_html_no_children(self):
    try:
        ParentNode("div", []).to_html()
    except ValueError as e:
        assert str(e) == "ParentNode must have children"

