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
    "NEWLINE",
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

    # Process indentation changes
    if new_indent_level > current_indent_level:
        indent_stack.append(new_indent_level)
        add_token_to_queue("INDENT", t.lexer.lineno)
    while new_indent_level < current_indent_level:
        indent_stack.pop()
        add_token_to_queue("DEDENT", t.lexer.lineno)
        current_indent_level = indent_stack[-1] if indent_stack else 0

    t.type = "NEWLINE"
    return t

def add_token_to_queue(token_type, line_no):
    # print(f"Adding token {token_type} at line {line_no}")
    token = lex.LexToken()
    token.type = token_type
    token.value = None
    token.lineno = line_no
    token.lexpos = -1  # position not tracked
    lexer_tokens_queue.append(token)
    # print(lexer_tokens_queue)


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


original_token_method = lex.Lexer.token


def new_token_method(self):
    # First check if there are tokens in the queue to be processed
    if lexer_tokens_queue:
        # Get the next token from the queue
        queued_token = lexer_tokens_queue.pop(0)
        # print(f"Dequeuing: {queued_token.type} at line {queued_token.lineno}")
        return queued_token

    # If no tokens are in the queue, generate the next token using the original method
    token = original_token_method(self)

    # If the generated token is significant for indentation handling (like NEWLINE), recheck the queue
    if token and token.type == "NEWLINE":
        # Check if there are indentation changes that need to be processed before continuing
        if lexer_tokens_queue:
            # Insert the current token back at the start of the queue to handle it after the indentation tokens
            lexer_tokens_queue.insert(0, token)
            # print(f"Re-queueing NEWLINE for later processing")
            # Return the next token from the queue which should be an indentation token
            return lexer_tokens_queue.pop(0)

    # Return the generated token if no further queue processing is needed
    return token



lex.Lexer.token = new_token_method

lexer = lex.lex()
lexer.indent_stack = [0]

if __name__ == "__main__":
    # Test the lexer
    with open("tests/sample.bs", "r", encoding="utf-8") as f:
        bliss_code = f.read()

    lexer.input(bliss_code)
    for tok in lexer:
        print(tok)


def get_lexer():
    return lexer
