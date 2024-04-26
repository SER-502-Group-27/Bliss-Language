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



if __name__ == "__main__":
    unittest.main()
