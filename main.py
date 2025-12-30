from lexer import Lexer
from tokens import EOF


if __name__ == "__main__":
    while True:
        try:
            input_str = input(">> ")
        except EOFError:
            break
        lexer = Lexer(input_str)

        tok = lexer.next_token()
        while tok.type != EOF:
            print(tok)
            tok = lexer.next_token()
