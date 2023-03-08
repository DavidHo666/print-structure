import pytest

from printstructure import PrintStructure
from printstructure.printdp import DPTable
from printstructure.printtree import Tree

from unittest import TestCase


def test_valid_data_type():
    data = [1,2,3]
    dp = DPTable(data)

def test_invalid_data_type_tuple():
    with pytest.raises(TypeError):
        data = tuple([1,2])
        dp = DPTable(data)

def test_valid_nested_data_type():
    data = [[1,2,3],[4,5,6]]
    dp = DPTable(data)

def test_invalid_nested_data_type():
    with pytest.raises(TypeError):
        data = [1, [1,2]]
        dp = DPTable(data)

def test_inconsistant_row_lenght():
    with pytest.raises(ValueError):
        data = [[1], [1,2]]
        dp = DPTable(data)

def test_2d_table_output(capsys):
    data = data = [['a', 'b', 'c'], ['b', 'c','d'], [1,2,3]]
    dp = DPTable(data)
    dp.print_dp()
    out, err = capsys.readouterr()
    assert out == (
        '+--------+-----+-----+-----+\n'
        '|   col# | 0   | 1   | 2   |\n'
        '|   row# |     |     |     |\n'
        '+========+=====+=====+=====+\n'
        '|      0 | a   | b   | c   |\n'
        '+--------+-----+-----+-----+\n'
        '|      1 | b   | c   | d   |\n'
        '+--------+-----+-----+-----+\n'
        '|      2 | 1   | 2   | 3   |\n'
        '+--------+-----+-----+-----+\n'
    )

def test_1d_table_output(capsys):
    data = data = [1,2,3]
    dp = DPTable(data)
    dp.print_dp()
    out, err = capsys.readouterr()
    assert out == (
         '+--------+-----+-----+-----+\n'
         '| col#   |   0 |   1 |   2 |\n'
         '+========+=====+=====+=====+\n'
         '|        |   1 |   2 |   3 |\n'
         '+--------+-----+-----+-----+\n'
    )