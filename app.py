INTEGER = 'INTEGER'
PLUS = 'PLUS'
SUBTRACT = 'SUBTRACT'
DIVIDE = 'DIVIDE'
MULTIPLY = 'MULTIPLY'
EOF = 'EOF'

class InvalidTokenException(Exception):
    pass


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return '<Token::{}={}>'.format(self.type, self.value)


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def get_next_token(self):
        if self.pos > len(self.text) - 1:
            return Token(EOF, None)

        current_char = self.text[self.pos]

        if current_char.isdigit():
            buffer = ''
            while current_char.isdigit():
                buffer += current_char
                self.pos += 1
                if self.pos > len(self.text) - 1:
                    break
                else:
                    current_char = self.text[self.pos]
            return Token(INTEGER, int(buffer))

        if current_char == '+':
            self.pos += 1
            return Token(PLUS, current_char)

        if current_char == '-':
            self.pos += 1
            return Token(SUBTRACT, current_char)

        if current_char == '/':
            self.pos += 1
            return Token(DIVIDE, current_char)

        if current_char == '*':
            self.pos += 1
            return Token(MULTIPLY, current_char)

        if current_char == ' ':
            self.pos += 1
            return self.get_next_token()

        raise Exception('Error parsing input')

    def eat(self, token_types):
        if self.current_token.type in token_types:
            self.current_token = self.get_next_token()
        else:
            raise InvalidTokenException('Token type \'{}\' is not valid in {}'.format(self.current_token.type, token_types))

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat([INTEGER])

        operator = self.current_token
        self.eat([PLUS, SUBTRACT, DIVIDE, MULTIPLY])

        right = self.current_token
        self.eat([INTEGER])

        return self.evaluate_expression(left.value, operator.type, right.value)

    def evaluate_expression(self, left_value, operator, right_value):
        if operator == PLUS:
            return int(left_value + right_value)
        if operator == SUBTRACT:
            return int(left_value - right_value)
        if operator == DIVIDE:
            return int(left_value / right_value)
        if operator == MULTIPLY:
            return int(left_value * right_value)


if __name__ == '__main__':
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break

        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)
