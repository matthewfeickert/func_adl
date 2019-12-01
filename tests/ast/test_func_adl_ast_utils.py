# Test out the utility classes.
from func_adl.ast.func_adl_ast_utils import FuncADLNodeTransformer, is_call_of
import ast


class my_call_catcher(FuncADLNodeTransformer):
    def __init__ (self):
        self.count = 0
        self.args = []

    def call_dude(self, node, args):
        self.count += 1
        self.args = args
        return node


def test_node_transform_method_ast():
    start = ast.parse('a.dude()')
    expected = ast.dump(start)
    e = FuncADLNodeTransformer()
    assert expected == ast.dump(e.visit(start))

def test_node_transform_method_ast_with_object():
    start = ast.parse('a.dude()')
    expected = ast.dump(start)
    e = my_call_catcher()
    assert expected == ast.dump(e.visit(start))
    assert e.count == 0

def test_node_transform_function_ast_with_object():
    start = ast.parse('dude()')
    expected = ast.dump(start)
    e = my_call_catcher()
    assert expected == ast.dump(e.visit(start))
    assert e.count == 1

def test_node_transform_function_ast_with_object_args():
    start = ast.parse('dude(10)')
    expected = ast.dump(start)
    e = my_call_catcher()
    assert expected == ast.dump(e.visit(start))
    assert e.count == 1
    assert len(e.args) == 1
    assert isinstance(e.args[0], ast.Num)
    assert e.args[0].n == 10

def test_node_transform_function_ast_with_object_args_norec():
    start = ast.parse('dude1(10)')
    expected = ast.dump(start)
    e = my_call_catcher()
    assert expected == ast.dump(e.visit(start))
    assert e.count == 0

def test_node_transform_function_deep():
    start = ast.parse('dork(dude(10))')
    expected = ast.dump(start)
    e = my_call_catcher()
    assert expected == ast.dump(e.visit(start))
    assert e.count == 1

def _parse_ast (e : str) -> ast.AST:
    a = ast.parse(e)
    b = a.body[0]
    assert isinstance(b, ast.Expr)
    return b.value

def test_is_call_to_expected_function():
    start = _parse_ast('dude(10)')
    assert is_call_of(start, 'dude')

def test_is_call_to_unexpected_function():
    start = _parse_ast('dude(10)')
    assert not is_call_of(start, 'dude1')

def test_is_call_to_expected_method():
    start = _parse_ast('a.dude(10)')
    assert not is_call_of(start, 'dude')

def test_is_call_not_a_call():
    start = _parse_ast('dude1')
    assert not is_call_of(start, 'dude1')
