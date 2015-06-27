import unittest
from unittest.mock import patch

from app import Interpreter, Token, PLUS, SUBTRACT, DIVIDE, MULTIPLY, INTEGER, EOF, InvalidTokenException

class TestGetNextToken(unittest.TestCase):
    def test_return_eof_token_when_out_of_bounds(self):
        interpreter = Interpreter('')
        self.assertEqual(Token(EOF, None).type, interpreter.get_next_token().type)


class TestEat(unittest.TestCase):
    def test_valid_token_calls_get_next_token(self):
        interpreter = Interpreter('')
        with patch.object(interpreter, 'get_next_token') as get_next_token:
            interpreter.current_token = Token(PLUS, '+')
            interpreter.eat([PLUS, SUBTRACT, DIVIDE, MULTIPLY])
        self.assertTrue(get_next_token.called)

    def test_invalid_token_raises_exception(self):
        interpreter = Interpreter('')
        interpreter.current_token = Token(PLUS, '+')
        with self.assertRaises(InvalidTokenException) as exc:
            interpreter.eat([DIVIDE, MULTIPLY])


class TestEvaluateExpression(unittest.TestCase):
    def test_plus_operator(self):
        interpreter = Interpreter('')
        self.assertEqual(2, interpreter.evaluate_expression(1, PLUS, 1))

    def test_subtract_operator(self):
        interpreter = Interpreter('')
        self.assertEqual(1, interpreter.evaluate_expression(2, SUBTRACT, 1))

    def test_divide_operator(self):
        interpreter = Interpreter('')
        self.assertEqual(2, interpreter.evaluate_expression(4, DIVIDE, 2))

    def test_multiply_operator(self):
        interpreter = Interpreter('')
        self.assertEqual(4, interpreter.evaluate_expression(2, MULTIPLY, 2))

if __name__ == '__main__':
    unittest.main()
