import unittest

from src.lexer import get_lexer


class TestLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = get_lexer()

    def test_integer(self):
        self.lexer.input("1234")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "INTEGER")
        self.assertEqual(token.value, 1234)

    def test_float(self):
        self.lexer.input("12.34")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "FLOAT")
        self.assertEqual(token.value, 12.34)

    def test_string_literal_double_quotes(self):
        self.lexer.input('"hello world"')
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "STRING_LITERAL")
        self.assertEqual(token.value, "hello world")

    def test_string_literal_single_quotes(self):
        self.lexer.input("'hello world'")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "STRING_LITERAL")
        self.assertEqual(token.value, "hello world")

    def test_boolean_true(self):
        self.lexer.input("True")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "BOOLEAN")
        self.assertEqual(token.value, True)

    def test_boolean_false(self):
        self.lexer.input("False")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "BOOLEAN")
        self.assertEqual(token.value, False)

    def test_plus_operator(self):
        self.lexer.input("+")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "PLUS")

    def test_minus_operator(self):
        self.lexer.input("-")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "MINUS")

    def test_times_operator(self):
        self.lexer.input("*")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "TIMES")

    def test_divide_operator(self):
        self.lexer.input("/")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "DIVIDE")

    def test_modulo_operator(self):
        self.lexer.input("%")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "MODULO")

    def test_greater_than_operator(self):
        self.lexer.input(">")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "GREATER_THAN")

    def test_less_than_operator(self):
        self.lexer.input("<")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "LESS_THAN")

    def test_greater_equal_operator(self):
        self.lexer.input(">=")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "GREATER_EQUAL")

    def test_less_equal_operator(self):
        self.lexer.input("<=")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "LESS_EQUAL")

    def test_assign_operator(self):
        self.lexer.input("=")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "ASSIGN")

    def test_add_assign_operator(self):
        self.lexer.input("+=")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "ADD_ASSIGN")

    def test_sub_assign_operator(self):
        self.lexer.input("-=")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "SUB_ASSIGN")

    def test_mul_assign_operator(self):
        self.lexer.input("*=")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "MUL_ASSIGN")

    def test_div_assign_operator(self):
        self.lexer.input("/=")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "DIV_ASSIGN")

    def test_mod_assign_operator(self):
        self.lexer.input("%=")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "MOD_ASSIGN")

    def test_equal_operator(self):
        self.lexer.input("==")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "EQUAL")

    def test_not_equal_operator(self):
        self.lexer.input("!=")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "NOT_EQUAL")

    def test_indentation_single_indent(self):
        code = "if condition:\n    action"
        self.lexer.input(code)
        tokens = [token for token in self.lexer]

        self.assertTrue(any(t.type == "INDENT" for t in tokens))

    def test_indentation_with_dedent(self):
        code = "if condition:\n    action\nelse:\n    action2"
        self.lexer.input(code)
        tokens = [token for token in self.lexer]
        indents = [t.type for t in tokens]
        self.assertIn("INDENT", indents)
        self.assertIn("OUTDENT", indents)

    def test_keyword_if(self):
        self.lexer.input("if")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "IF")

    def test_keyword_else(self):
        self.lexer.input("else")
        token = self.lexer.token()
        self.assertIsNotNone(token)
        self.assertEqual(token.type, "ELSE")

    def test_nested_if(self):
        code = "if x > 0:\n    if x < 10:\n        print('x is between 0 and 10')"
        self.lexer.input(code)
        tokens = [token for token in self.lexer]
        self.assertTrue(
            any(t.type == "IF" for t in tokens)
            and len([t for t in tokens if t.type == "IF"]) == 2
        )

    def test_while_simple_loop(self):
        code = "while True:\n    print('Looping')"
        self.lexer.input(code)
        tokens = [token for token in self.lexer]
        self.assertTrue(any(t.type == "WHILE" for t in tokens))


if __name__ == "__main__":
    unittest.main()
