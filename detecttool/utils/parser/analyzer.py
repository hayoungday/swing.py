from collections import deque
import ast


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self._name = deque()

    @property
    def name(self):
        return ".".join(self._name)

    @name.deleter
    def name(self):
        self._name.clear()

    def visit_Import(self, node):
        for alias in node.names:
            self._name.append(alias.name)

    def visit_ImportFrom(self, node):
        module = node.module
        for alias in node.names:
            tmp = module + "." + alias.name
            self._name.append(tmp)

    def visit_ClassDef(self, node):
        self._name.append(node.name)

    def visit_FunctionDef(self, node):
        self._name.append(node.name)

    def visit_Name(self, node):
        self._name.appendleft(node.id)

    def visit_Attribute(self, node):
        try:
            self._name.appendleft(node.attr)
            self._name.appendleft(node.value.id)
        except AttributeError:
            self.generic_visit(node)

    def visit_Num(self, node):
        self._name.append(str(node.n))
