"""
Lexer for the Bliss programming language.

This module uses the PLY library to define a lexical analyzer that tokenizes the input source code into meaningful symbols. It includes definitions for various token types such as identifiers, operators, and literals. Additionally, it handles reserved keywords and indentation, crucial for the syntactic structure of Bliss. The lexer supports error handling for unrecognized tokens and maintains line numbers for better error reporting.
"""


import ply.lex as lex

# List of token names. This is always required
tokens = (
    "FLOAT",
    "BOOLEAN",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "MODULO",
    "LPAREN",
    "RPAREN",
    "IDENTIFIER",
    "ASSIGN",
    "ADD_ASSIGN",
    "SUB_ASSIGN",
    "MUL_ASSIGN",
    "DIV_ASSIGN",
    "MOD_ASSIGN",
    "GREATER_THAN",
    "LESS_THAN",
    "GREATER_EQUAL",
    "LESS_EQUAL",
    "COLON",
    "EQUAL",
    "NOT_EQUAL",
    "INDENT",
    "OUTDENT",
    "COMMA",
    "SEMI",
    "INC",
    "DEC",
    "LBRACKET",
    "RBRACKET",
    "QUESTION",
    "COMMENT",
)

# Reserved keywords mapping
reserved = {
    "if": "IF",
    "else": "ELSE",
    "elif": "ELIF",
    "print": "PRINT",
    "int": "INTEGER",
    "str": "STRING",
    "for": "FOR",
    "while": "WHILE",
    "and": "AND",
    "or": "OR",
    "in": "IN",
    "range": "RANGE",
    "break": "BREAK",
    "continue": "CONTINUE",
    "def": "DEF",
    "not": "NOT",
}

tokens += tuple(reserved.values())

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_MODULO = r"%"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_GREATER_THAN = r">"
t_LESS_THAN = r"<"
t_GREATER_EQUAL = r">="
t_LESS_EQUAL = r"<="
t_COLON = r":"
t_COMMA = r","
t_SEMI = r";"
t_QUESTION = r"\?"
t_INC = r"\+\+"
t_DEC = r"--"

states = (("indent", "exclusive"),)
indent_size = 4
# Ignore spaces and tabs in all states
t_ignore = " \t"
t_indent_ignore = ""

lexer_tokens_queue = []
indent_stack = [0]


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
    position = t.lexer.lexpos
    remaining_data = t.lexer.lexdata[position:]
    new_indent_level = (
        len(remaining_data) - len(remaining_data.lstrip(" "))
    ) // indent_size
    current_indent_level = indent_stack[-1] if indent_stack else 0
    return_flag = False
    # Process indentation changes
    if new_indent_level > current_indent_level:
        indent_stack.append(new_indent_level)
        return generate_indent_token("INDENT", new_indent_level, t.lexer.lineno)
    while new_indent_level < current_indent_level:
        indent_stack.pop()
        if not return_flag:
            token = generate_indent_token(
                "OUTDENT", current_indent_level, t.lexer.lineno
            )
            return_flag = True
        else:
            token_to_append = generate_indent_token(
                "OUTDENT", current_indent_level, t.lexer.lineno
            )
            lexer_tokens_queue.append(token_to_append)
        current_indent_level = indent_stack[-1] if indent_stack else -1
    if return_flag:
        return token


def generate_indent_token(token_type, indent_level, line_no):
    token = lex.LexToken()
    token.type = token_type
    token.value = indent_level
    token.lineno = line_no
    token.lexpos = indent_level * indent_size if indent_level > 0 else 0
    return token


def t_error(t):
    if t.value[0] not in " \t":
        print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


def t_indent_other(t):
    r"[^\s]"
    # Return to the initial state when hitting non-whitespace
    t.lexer.begin("INITIAL")
    t.lexer.lexpos -= 1  # Re-evaluate this character in the initial state


def t_indent_error(t):
    print(f"Unexpected character {t.value[0]} in indentation")
    t.lexer.skip(1)


def t_RANGE(t):
    r"range"
    return t


def t_TRUE(t):
    r"True"
    t.value = True
    t.type = "BOOLEAN"
    return t


def t_FALSE(t):
    r"False"
    t.value = False
    t.type = "BOOLEAN"
    return t


def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "IDENTIFIER")
    return t


def t_FLOAT(t):
    r"(\d+\.\d*|\.\d+)([eE][+-]?\d+)?|\d+[eE][+-]?\d+"
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_STRING(t):
    r"('([^'\\\n]|(\\.))*?'|\"([^\"\\\n]|(\\.))*?\")"
    t.value = t.value[1:-1]
    return t


def t_EQUAL(t):
    r"=="
    return t


def t_NOT_EQUAL(t):
    r"!="
    return t


def t_ADD_ASSIGN(t):
    r"\+="
    return t


def t_SUB_ASSIGN(t):
    r"-="
    return t


def t_MUL_ASSIGN(t):
    r"\*="
    return t


def t_DIV_ASSIGN(t):
    r"/="
    return t


def t_MOD_ASSIGN(t):
    r"%="
    return t


def t_ASSIGN(t):
    r"="
    return t


def t_COMMENT(t):
    r"\#.*"
    pass


original_token_method = lex.Lexer.token


def new_token_method(self):
    # First check if there are tokens in the queue to be processed
    while lexer_tokens_queue:
        if lexer_tokens_queue[0].type in {"INDENT", "OUTDENT"}:
            return lexer_tokens_queue.pop(0)

    # If no tokens are in the queue, generate the next token using the original method
    token = original_token_method(self)
    return token


lex.Lexer.token = new_token_method

lexer = lex.lex()


def preprocess_input(data):
    """Ensure the input data ends with a newline for proper lexing."""
    if not data.endswith("\n"):
        data += "\n"
    return data


if __name__ == "__main__":
    # Test the lexer
    with open("tests/sample.bs", "r", encoding="utf-8") as f:
        bliss_code = f.read()

    lexer.input(preprocess_input(bliss_code))
    for tok in lexer:
        print(tok)


def get_lexer():
    return lexer
