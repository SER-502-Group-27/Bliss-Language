from lexer import tokens
import ply.yacc as yacc

# Define the grammar

# Mathematical Operations
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
         | factor
    """
    if len(p) == 4:
        if p[2] == "*":
            p[0] = p[1] * p[3]
        elif p[2] == "/":
            p[0] = p[1] / p[3]
    else:  # base case (factor)
        p[0] = p[1]


def p_factor(p):
    """
    factor : NUMBER
           | LPAREN expression RPAREN
    """
    if len(p) == 2:
        p[0] = p[1]
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
    print("Enter an arithmetic expression, or 'exit' to quit:")
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
