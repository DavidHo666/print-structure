from .printdp import DPTable
from .printtree import Tree


class PrintStructure:
    def __int__(self, data, structure_type):
        self.data = data
        if structure_type != 'tree' or structure_type != 'dptable':
            raise ValueError('invalid argument type: {}, only tree and dptable are supported'.format(structure_type))
        self.structure_type = structure_type

    def print(self):
        if self.structure_type == 'dptable':
            dp = DPTable(self.data)
            dp.print_dp()
        elif self.structure_type == 'tree':
            tree = Tree(self.data)
            tree.print_tree()
