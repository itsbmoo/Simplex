LEFT_PAREN = ''
RIGHT_PAREN = ''
LEFT_BRACE = ''
RIGHT_BRACE = ''
COMMA = ''
DOT = ''
PLUS = ''
MINUS = ''
SEMICOLON = ''
SLASH = ''
STAR = ''



BANG = ''
BANG_EQUAL = ''
EQUAL = ''
EQUAL_EQUAL = ''
GREATER = ''
GREATER_THAN = ''
GREATER_EQUAL = ''
LESS = ''
LESS_EQUAL = ''



IDENTIFIER = ''
STRING = ''
NUMBER = ''



AND = ''
CLASS = ''
ELSE = ''
FALSE = ''
FUN = ''
FOR = ''
IF = ''
NIL = ''
OR = ''
PRINT = ''
RETURN = ''
SUPER = ''
THIS = ''
TRUE = ''
VAR = ''
WHILE = ''
EOF = ''



TOKEN_TYPE = [
    # Single Character Tokens
    LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE,
    COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR,
    
    # One or Two Character Tokens.
    BANG, BANG_EQUAL,
    EQUAL, EQUAL_EQUAL,
    GREATER, GREATER_EQUAL,
    LESS, LESS_EQUAL,

    # Literals
    IDENTIFIER, STRING, NUMBER,

    # Keywords
    AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NIL, OR,
    PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE, EOF
]
