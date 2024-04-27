import unittest
from src.parse import parse, preprocess_input
from src.ast_nodes import (
    Block,
    PrintStatement,
    BinaryOperation,
    Number,
    Boolean,
    List,
    IndexOrSlicing,
    Identifier,
    StringLiteral,
    UnaryOperation,
    Assignment,
    Range,
    IfStatement,
    WhileStatement,
    ForStatement,
    FunctionDefinition,
    FunctionCall,
)


class TestParser(unittest.TestCase):
    def test_basic_arithmetic(self):
        data = "3 + 4"
        result = parse(preprocess_input(data))
        self.assertIsInstance(result, Block)
        self.assertEqual(len(result.statements), 1)
        self.assertIsInstance(result.statements[0], BinaryOperation)
        self.assertEqual(result.statements[0].operator, "+")
        self.assertEqual(result.statements[0].left.value, 3)
        self.assertEqual(result.statements[0].right.value, 4)

    def test_print_statement(self):
        data = 'print("hello world")'
        result = parse(preprocess_input(data))
        self.assertIsInstance(result, Block)
        self.assertEqual(len(result.statements), 1)
        self.assertIsInstance(result.statements[0], PrintStatement)
        self.assertIsInstance(result.statements[0].expr, StringLiteral)
        self.assertEqual(result.statements[0].expr.value, "hello world")

    def test_numeric_expression(self):
        data = "42"
        result = parse(preprocess_input(data))
        self.assertIsInstance(result, Block)
        self.assertIsInstance(result.statements[0], Number)
        self.assertEqual(result.statements[0].value, 42)

    def test_string_literal(self):
        data = '"hello world"'
        result = parse(preprocess_input(data))
        self.assertIsInstance(result, Block)
        self.assertIsInstance(result.statements[0], StringLiteral)
        self.assertEqual(result.statements[0].value, "hello world")

    def test_boolean_expression(self):
        data = "True"
        result = parse(preprocess_input(data))
        self.assertIsInstance(result, Block)
        self.assertIsInstance(result.statements[0], Boolean)
        self.assertTrue(result.statements[0].value)

    def test_complex_arithmetic(self):
        data = "(3 + 4) * 5"
        result = parse(preprocess_input(data))
        self.assertIsInstance(result, Block)
        self.assertIsInstance(result.statements[0], BinaryOperation)
        self.assertEqual(result.statements[0].operator, "*")
        self.assertIsInstance(result.statements[0].left, BinaryOperation)
        self.assertEqual(result.statements[0].left.operator, "+")

    def test_if_statement(self):
        data = "if x > 10:\n    print('yes')"
        result = parse(preprocess_input(data))
        self.assertIsInstance(result, Block)
        self.assertIsInstance(result.statements[0], IfStatement)
        self.assertIsInstance(result.statements[0].condition, BinaryOperation)

    def test_while_loop(self):
        data = "while x < 10:\n    x += 1"
        result = parse(preprocess_input(data))
        self.assertIsInstance(result, Block)
        self.assertIsInstance(result.statements[0], WhileStatement)
        self.assertIsInstance(result.statements[0].body.statements[0], Assignment)

    def test_function_definition(self):
        data = "def my_func(x):\n    return x * 2"
        result = parse(preprocess_input(data))
        self.assertIsInstance(result, Block)
        self.assertIsInstance(result.statements[0], FunctionDefinition)
        self.assertEqual(result.statements[0].name, "my_func")

    def test_function_call(self):
        data = "result = my_func(5)"
        result = parse(preprocess_input(data))
        self.assertIsInstance(result, Block)
        self.assertIsInstance(result.statements[0], Assignment)
        self.assertIsInstance(result.statements[0].expr, FunctionCall)
        self.assertEqual(result.statements[0].expr.function_name, "my_func")

    def test_list_and_indexing(self):
        data = "my_list = [1, 2, 3][1]"
        result = parse(preprocess_input(data))
        self.assertIsInstance(result, Block)
        self.assertIsInstance(result.statements[0], Assignment)
        self.assertIsInstance(result.statements[0].expr, IndexOrSlicing)


if __name__ == "__main__":
    unittest.main()
