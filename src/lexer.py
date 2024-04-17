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
}

# Update tokens list to include reserved words
tokens += tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_MODULO = r"%"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_AND = r"&"
t_OR = r"\|"
t_NOT = r"!"
t_GREATER_THAN = r">"
t_LESS_THAN = r"<"
t_GREATER_EQUAL = r">="
t_LESS_EQUAL = r"<="
t_COLON = r":"


# Define states for tracking indentation
states = (("indent", "exclusive"),)

# Track the stack of indent levels
indent_stack = [0]

# Rule for tracking newlines and whitespace


def t_ANY_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
    t.lexer.begin("indent")


def t_indent_whitespace(t):
    r"[ ]+"
    t.lexer.lexpos -= len(t.value)
    space_count = len(t.value)
    if space_count > indent_stack[-1]:
        indent_stack.append(space_count)
        t.type = "INDENT"
        t.value = space_count
        t.lexer.begin("INITIAL")
        return t
    elif space_count < indent_stack[-1]:
        while indent_stack and space_count < indent_stack[-1]:
            indent_stack.pop()
            t.type = "DEDENT"
            t.value = space_count
            t.lexer.begin("INITIAL")
            return t
    t.lexer.begin("INITIAL")


# Error handling rule for indentation state
def t_indent_error(t):
    print(f"Illegal character in indentation '{t.value[0]}'")
    t.lexer.skip(1)


# A rule for identifiers (variable names) and boolean values
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


# New Number rule containing both Int and Float - Optional
# def t_NUMBER(t):
#     r"\d*\.\d+([eE][-+]?\d+)?|\d+\.\d*([eE][-+]?\d+)?|\d+([eE][-+]?\d+)?"
#     try:
#         t.value = int(t.value)
#     except ValueError:
#         t.value = float(t.value)
#     return t

# Rule for Floats only
def t_FLOAT(t):
    r"(\d+\.\d*|\.\d+)([eE][+-]?\d+)?|\d+[eE][+-]?\d+"
    t.value = float(t.value)
    return t


# Rule for Integers only
def t_INTEGER(t):
    r"\d+"
    t.value = int(t.value)
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"


# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Assignment and assignment operators
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


# Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
    # Test the lexer
    data = """
    a = 2
    b = .3
    c = 0.6
    f = 1.0e+10
    g = 1.0e-10
    g1 = 1.0e-3
    h = 1e+10
    e = 1e-10
    e1 = 1e-3
    d = 1e10
    """
    lexer.input(data)
    for tok in lexer:
        print(tok)
