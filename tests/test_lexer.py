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


if __name__ == "__main__":
    unittest.main()
