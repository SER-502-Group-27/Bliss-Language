import ply.lex as lex

# List of token names. This is always required
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
    'LPAREN', 'RPAREN',  # For numerical expressions
    'AND', 'OR', 'NOT',  # Logical operators
    'IDENTIFIER', 'ASSIGN',  # For variables
    'IF', 'ELSE',  # Conditional
    'PRINT',  # Built-in function
    'FOR', 'WHILE',  # Loops
)

# Reserved keywords mapping
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'print': 'PRINT',
    'int': 'INTEGER',
    'str': 'STRING',
    'for': 'FOR',
    'while': 'WHILE',
    'and': 'AND',
    'or': 'OR'
    # Add other keywords as needed
}

# Update tokens list to include reserved words
tokens += tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_AND     = r'&'
t_OR      = r'\|'
t_NOT     = r'!'
t_ASSIGN  = r'='

# A rule for identifiers (variable names)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

# A rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
    # Test the lexer
    data = '''
    if x = 10
        print x
    else
        print 0
    '''
    lexer.input(data)
    for tok in lexer:
        print(tok)