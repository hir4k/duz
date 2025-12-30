from tokens import *


class Lexer:
    def __init__(self, input: str):
        self.input = input
        self.input_len = len(input)
        self.position = 0
        self.read_position = 0
        self.ch: str = ""
        self.read_char()

    def read_char(self):
        """The purpose of readChar is to give us the next character and advance our position in the input string."""
        if self.read_position >= self.input_len:
            self.ch = ""
        else:
            self.ch = self.input[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def peek_char(self) -> str:
        """The purpose of peekChar is to look ahead in the input without moving our position."""
        if self.read_position >= self.input_len:
            return ""
        else:
            return self.input[self.read_position]

    def next_token(self) -> Token:
        """The purpose of nextToken is to return the next token from the input string."""

        self.skip_whitespace()

        if self.ch == "=":
            if self.peek_char() == "=":
                ch = self.ch
                self.read_char()
                literal = ch + self.ch
                tok = Token(EQ, literal)
            else:
                tok = Token(ASSIGN, self.ch)
        elif self.ch == "+":
            tok = Token(PLUS, self.ch)
        elif self.ch == ",":
            tok = Token(COMMA, self.ch)
        elif self.ch == ";":
            tok = Token(SEMICOLON, self.ch)
        elif self.ch == "(":
            tok = Token(LPAREN, self.ch)
        elif self.ch == ")":
            tok = Token(RPAREN, self.ch)
        elif self.ch == "{":
            tok = Token(LBRACE, self.ch)
        elif self.ch == "}":
            tok = Token(RBRACE, self.ch)
        elif self.ch == "!":
            if self.peek_char() == "=":
                ch = self.ch
                self.read_char()
                literal = ch + self.ch
                tok = Token(NOT_EQ, literal)
            else:
                tok = Token(BANG, self.ch)
        elif self.ch == "-":
            tok = Token(MINUS, self.ch)
        elif self.ch == "*":
            tok = Token(ASTERISK, self.ch)
        elif self.ch == "/":
            tok = Token(SLASH, self.ch)
        elif self.ch == "<":
            tok = Token(LT, self.ch)
        elif self.ch == ">":
            tok = Token(GT, self.ch)

        elif self.ch is None:
            tok = Token(EOF, "")
        else:
            if self.is_letter(self.ch):
                literal = self.read_identifier()
                type = self.lookup_identifier(literal)
                return Token(type, literal)
            elif self.is_digit(self.ch):
                literal = self.read_number()
                return Token(INT, literal)
            else:
                tok = Token(ILLEGAL, self.ch)

        self.read_char()
        return tok

    def is_letter(self, ch: str) -> bool:
        return "a" <= ch <= "z" or "A" <= ch <= "Z" or ch == "_"

    def is_digit(self, ch: str) -> bool:
        return "0" <= ch <= "9"

    def read_identifier(self) -> str:
        position = self.position
        while self.is_letter(self.ch):
            self.read_char()
        return self.input[position : self.position]

    def read_number(self) -> str:
        position = self.position
        while self.is_digit(self.ch):
            self.read_char()
        return self.input[position : self.position]

    def lookup_identifier(self, ident: str) -> str:
        keywords = {
            "let": LET,
            "fn": FUNCTION,
            "true": TRUE,
            "false": FALSE,
            "if": IF,
            "else": ELSE,
            "return": RETURN,
        }
        return keywords.get(ident, IDENT)

    def skip_whitespace(self):
        while self.ch in " \t\n\r":
            self.read_char()
