from printstructure import PrintStructure


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_print_dp_1(capsys):
    data = [[1, 2, 3], [4, 5, 6]]
    ps = PrintStructure()
    ps.print(data)
    out, err = capsys.readouterr()
    assert out == (
        "+--------+-----+-----+-----+\n"
        "|   col# |   0 |   1 |   2 |\n"
        "|   row# |     |     |     |\n"
        "+========+=====+=====+=====+\n"
        "|      0 |   1 |   2 |   3 |\n"
        "+--------+-----+-----+-----+\n"
        "|      1 |   4 |   5 |   6 |\n"
        "+--------+-----+-----+-----+\n"
    )


def test_print_dp_2(capsys):
    data = [1, 2, 3, 4, 5, 6]
    ps = PrintStructure()
    ps.print(data)
    out, err = capsys.readouterr()
    assert out == (
        "+--------+-----+-----+-----+-----+-----+-----+\n"
        "| col#   |   0 |   1 |   2 |   3 |   4 |   5 |\n"
        "+========+=====+=====+=====+=====+=====+=====+\n"
        "|        |   1 |   2 |   3 |   4 |   5 |   6 |\n"
        "+--------+-----+-----+-----+-----+-----+-----+\n"
    )


def test_print_dp_3(capsys):
    data = [[1], [2], [3], [4], [5], [6]]
    ps = PrintStructure()
    ps.print(data)
    out, err = capsys.readouterr()
    assert out == (
        "+--------+-----+\n"
        "|   col# |   0 |\n"
        "|   row# |     |\n"
        "+========+=====+\n"
        "|      0 |   1 |\n"
        "+--------+-----+\n"
        "|      1 |   2 |\n"
        "+--------+-----+\n"
        "|      2 |   3 |\n"
        "+--------+-----+\n"
        "|      3 |   4 |\n"
        "+--------+-----+\n"
        "|      4 |   5 |\n"
        "+--------+-----+\n"
        "|      5 |   6 |\n"
        "+--------+-----+\n"
    )


def test_print_tree(capsys):
    node1 = Node(3)
    node2 = Node(11)
    node3 = Node(9, node1, node2)
    node_ex1 = Node(50)
    node4 = Node(48, None, node_ex1)
    node5 = Node(43, node3, node4)
    node6 = Node(54)
    node7 = Node(96)
    node8 = Node(67, node6, node7)
    node9 = Node(99, node8)
    node10 = Node(52, node5, node9)
    ps = PrintStructure()
    ps.print(node10)
    out, err = capsys.readouterr()
    assert out == (
        "      ____52_______ \n"
        "     /             \\\n"
        "  __43_         __99\n"
        " /     \\       /    \n"
        " 9_   48_     67_   \n"
        "/  \\     \\   /   \\  \n"
        "3 11    50  54  96  \n"
    )
