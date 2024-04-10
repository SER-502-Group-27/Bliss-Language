from lexer import tokens
import ply.yacc as yacc

# Symbol table to store variable values
symbol_table = {}


def p_statement_expr(p):
    "statement : expression"
    p[0] = p[1]


def p_statement_assign(p):
    "statement : IDENTIFIER ASSIGN expression"
    symbol_table[p[1]] = p[3]
    p[0] = p[3]


def p_statement_assign_shorthand(p):
    """
    statement : IDENTIFIER ADD_ASSIGN expression
              | IDENTIFIER SUB_ASSIGN expression
              | IDENTIFIER MUL_ASSIGN expression
              | IDENTIFIER DIV_ASSIGN expression
              | IDENTIFIER MOD_ASSIGN expression
    """
    if p[2] == "+=":
        symbol_table[p[1]] = symbol_table.get(p[1], 0) + p[3]
    elif p[2] == "-=":
        symbol_table[p[1]] = symbol_table.get(p[1], 0) - p[3]
    elif p[2] == "*=":
        symbol_table[p[1]] = symbol_table.get(p[1], 0) * p[3]
    elif p[2] == "/=":
        symbol_table[p[1]] = symbol_table.get(p[1], 0) / p[3]
    elif p[2] == "%=":
        symbol_table[p[1]] = symbol_table.get(p[1], 0) % p[3]
    p[0] = symbol_table[p[1]]


def p_expression_var(p):
    "expression : IDENTIFIER"
    p[0] = symbol_table.get(p[1], 0)


def p_expression(p):
    """
    expression : expression PLUS term
               | expression MINUS term
               | term
    """
    if len(p) == 4:  # expression PLUS term or expression MINUS term
        if p[2] == "+":
            p[0] = p[1] + p[3]
        elif p[2] == "-":
            p[0] = p[1] - p[3]
    else:  # base case (term)
        p[0] = p[1]


def p_term(p):
    """
    term : term TIMES factor
         | term DIVIDE factor
         | term MODULO factor
         | factor
    """
    if len(p) == 4:
        if p[2] == "*":
            p[0] = p[1] * p[3]
        elif p[2] == "/":
            p[0] = p[1] / p[3]
        elif p[2] == "%":
            p[0] = p[1] % p[3]
    else:
        p[0] = p[1]


def p_factor(p):
    """
    factor : NUMBER
           | IDENTIFIER
           | LPAREN expression RPAREN
    """
    if len(p) == 2:
        p[0] = symbol_table.get(p[1], p[1]) if p[1] in symbol_table else p[1]
    else:
        p[0] = p[2]


def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")


# Build the parser
parser = yacc.yacc()

# Testing the parser with an interactive loop
if __name__ == "__main__":
    print("Enter an expression, or 'exit' to quit:")
    while True:
        try:
            s = input("calc > ").strip()
            if s.lower() == "exit":
                break
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result)
