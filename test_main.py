from main import (
    Lexer,
    Token,
    ASSIGN,
    PLUS,
    COMMA,
    SEMICOLON,
    LPAREN,
    RPAREN,
    LBRACE,
    RBRACE,
    EOF,
    LET,
    IDENT,
    INT,
    FUNCTION,
)


def test_next_token():
    """Test tokenization of single-character operators"""
    input_str = """
    let five = 5;
    let ten = 10;
    let add = fn(x, y) {
        x + y;
    };
    let result = add(five, ten);
    """

    lexer = Lexer(input_str)

    expected_tokens = [
        Token(LET, "let"),
        Token(IDENT, "five"),
        Token(ASSIGN, "="),
        Token(INT, "5"),
        Token(SEMICOLON, ";"),
        Token(LET, "let"),
        Token(IDENT, "ten"),
        Token(ASSIGN, "="),
        Token(INT, "10"),
        Token(SEMICOLON, ";"),
        Token(LET, "let"),
        Token(IDENT, "add"),
        Token(ASSIGN, "="),
        Token(FUNCTION, "fn"),
        Token(LPAREN, "("),
        Token(IDENT, "x"),
        Token(COMMA, ","),
        Token(IDENT, "y"),
        Token(RPAREN, ")"),
        Token(LBRACE, "{"),
        Token(IDENT, "x"),
        Token(PLUS, "+"),
        Token(IDENT, "y"),
        Token(SEMICOLON, ";"),
        Token(RBRACE, "}"),
        Token(SEMICOLON, ";"),
        Token(LET, "let"),
        Token(IDENT, "result"),
        Token(ASSIGN, "="),
        Token(IDENT, "add"),
        Token(LPAREN, "("),
        Token(IDENT, "five"),
        Token(COMMA, ","),
        Token(IDENT, "ten"),
        Token(RPAREN, ")"),
        Token(SEMICOLON, ";"),
        Token(EOF, ""),
    ]

    for expected_token in expected_tokens:
        token = lexer.next_token()
        assert (
            token.type == expected_token.type
        ), f"Expected type {expected_token.type}, got {token.type}"
        assert (
            token.literal == expected_token.literal
        ), f"Expected literal {expected_token.literal}, got {token.literal}"
