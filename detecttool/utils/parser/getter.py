import ast
from utils.parser import analyzer


def get_func_calls(tree):
    res = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            a = analyzer.Analyzer()
            a.visit(node.func)
            res[a.name] = node
    return res


def get_import(tree):
    res = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            a = analyzer.Analyzer()
            a.visit(node)
            res[a.name] = node
        elif isinstance(node, ast.ImportFrom):
            a = analyzer.Analyzer()
            a.visit(node)         
            res[a.name] = node
    return res


def get_class(tree):
    res = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            a = analyzer.Analyzer()
            a.visit(node)
            res[a.name] = node
    return res


def get_func(tree):
    res ={}
    for node in ast.walk(tree):
        if isinstance(node,ast.FunctionDef):
            a = analyzer.Analyzer()
            a.visit(node)
            res[a.name]=node
    return res


def get_keyword(node):
    res = {}
    for keyword in node.keywords:
        res[keyword.arg] = keyword.value
    return res


def get_dic(node):
    res = {}
    for i in range(len(node.keys)):
        a = analyzer.Analyzer()
        a.visit(node.values[i])
        res[node.keys[i].s] = a.name
    return res

