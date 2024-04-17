import unittest
from lexer import get_lexer


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


if __name__ == "__main__":
    unittest.main()
