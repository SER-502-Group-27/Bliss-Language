import ply.lex as lex

# List of token names. This is always required
tokens = (
    "NUMBER",
    "FLOAT",
    "BOOLEAN",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "MODULO",
    "LPAREN",
    "RPAREN",
    "NOT",
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
    "DEDENT",
    "STRING_LITERAL",
    "COMMA",
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
}

tokens += tuple(reserved.values())

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_MODULO = r"%"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_GREATER_THAN = r">"
t_LESS_THAN = r"<"
t_GREATER_EQUAL = r">="
t_LESS_EQUAL = r"<="
t_COLON = r":"
t_COMMA = r","

states = (("indent", "exclusive"),)

indent_stack = [0]

# Ignore spaces and tabs in all states
t_ignore = " \t"
t_indent_ignore = " \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
    t.lexer.begin("indent")  # Begin checking for indentation on new lines


def t_indent_whitespace(t):
    r"[ ]+"
    space_count = len(t.value)
    if space_count > indent_stack[-1]:
        indent_stack.append(space_count)
        t.type = "INDENT"
        return t
    elif space_count < indent_stack[-1]:
        while indent_stack and space_count < indent_stack[-1]:
            indent_stack.pop()
            t.lexer.emit("DEDENT")
    t.lexer.begin("INITIAL")


def t_error(t):
    if t.value[0] not in " \t":
        print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


def t_indent_other(t):
    r"[^\s]"
    t.lexer.begin("INITIAL")  # Return to the initial state when hitting non-whitespace
    t.lexer.lexpos -= 1  # Re-evaluate this character in the initial state


def t_indent_error(t):
    print(f"Unexpected character {t.value[0]} in indentation")
    t.lexer.skip(1)


def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.value = t.value
    if t.value.lower() in ("true", "false"):
        t.type = "BOOLEAN"
        t.value = True if t.value.lower() == "true" else False
    else:
        t.type = reserved.get(
            t.value.lower(), "IDENTIFIER"
        )  # Use lowercase for checking
    return t


def t_FLOAT(t):
    r"(\d+\.\d*|\.\d+)([eE][+-]?\d+)?|\d+[eE][+-]?\d+"
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_STRING_LITERAL(t):
    r"\"([^\\\n]|(\\.))*?\" "
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


lexer = lex.lex()

if __name__ == "__main__":
    # Test the lexer
    with open("tests/sample.bs", "r", encoding="utf-8") as f:
        bliss_code = f.read()

    lexer.input(bliss_code)
    for tok in lexer:
        print(tok)


def get_lexer():
    return lexer
