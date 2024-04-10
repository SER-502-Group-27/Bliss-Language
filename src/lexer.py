import ply.lex as lex

# List of token names. This is always required
tokens = (
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "MODULO",
    "LPAREN",
    "RPAREN",  # For numerical expressions
    "AND",
    "OR",
    "NOT",  # Logical operators
    "IDENTIFIER",
    "ASSIGN",  # For variables
    "IF",
    "ELSE",  # Conditional
    "PRINT",  # Built-in function
    "FOR",
    "WHILE",  # Loops
    "ADD_ASSIGN",
    "SUB_ASSIGN",
    "MUL_ASSIGN",
    "DIV_ASSIGN",
    "MOD_ASSIGN",  # Assignment operators
    "GREATER_THAN",  # Comparison operators
    "LESS_THAN",
    "GREATER_EQUAL",
    "LESS_EQUAL",
)

# Reserved keywords mapping
reserved = {
    "if": "IF",
    "else": "ELSE",
    "print": "PRINT",
    "int": "INTEGER",
    "str": "STRING",
    "for": "FOR",
    "while": "WHILE",
    "and": "AND",
    "or": "OR",
    # Add other keywords as needed
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


# A rule for identifiers (variable names)
def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "IDENTIFIER")  # Check for reserved words
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "IDENTIFIER")  # Check for reserved words
    return t


# A rule for numbers
def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    r"\d+"
    t.value = int(t.value)
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"


# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    r"\n+"
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Assignment and assignment operators


def t_ASSIGN(t):
    r"="
    r"="
    return t


def t_ADD_ASSIGN(t):
    r"\+="
    r"\+="
    return t


def t_SUB_ASSIGN(t):
    r"-="
    r"-="
    return t


def t_MUL_ASSIGN(t):
    r"\*="
    r"\*="
    return t


def t_DIV_ASSIGN(t):
    r"/="
    r"/="
    return t


def t_MOD_ASSIGN(t):
    r"%="
    r"%="
    return t


# Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
    # Test the lexer
    # if x = 10 % 2
    #     print x
    # else
    #     print 0
    data = """
    a = 2
    a += 3
    """
    lexer.input(data)
    for tok in lexer:
        print(tok)
