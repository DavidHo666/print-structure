import pytest
from printstructure.printtree import Tree

class Node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Node_without_left:
    def __init__(self, val = None, right = None):
        self.val = val
        self.right = right

class Node_without_right:
    def __init__(self, val = None, left = None):
        self.val = val
        self.left = left
def test_invalide_node_without_left():
    node = Node_without_left(1, right=None)
    with pytest.raises(AttributeError):
        tree = Tree(node)

def test_invalide_node_without_right():
    node = Node_without_right(1, left=None)
    with pytest.raises(AttributeError):
        tree = Tree(node)

def test_print_tree(capsys):
    node1 = Node(3)
    node2 = Node(11)
    node3 = Node(9, node1, node2)
    node_ex1 = Node(50)
    node4 = Node(48, None, node_ex1)
    node5 = Node(43,node3, node4)
    node6 = Node(54)
    node7 = Node(96)
    node8 = Node(67, node6, node7)
    node9 = Node(99, node8)
    node10 = Node(52, node5, node9)
    tree = Tree(node10)
    tree.print_tree()
    out, err = capsys.readouterr()
    assert out == (
         '      ____52_______ \n'
         '     /             \\\n'
         '  __43_         __99\n'
         ' /     \\       /    \n'
         ' 9_   48_     67_   \n'
         '/  \\     \\   /   \\  \n'
         '3 11    50  54  96  \n'
    )