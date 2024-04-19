from lexer import tokens
import ply.yacc as yacc


symbol_table = {}


def p_program(p):
    """
    program : program statement
            | statement
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2] if p[1] and p[2] else p[1] or p[2]


def p_statement_expr(p):
    "statement : expression"
    p[0] = p[1]


def p_statement_assign(p):
    "statement : IDENTIFIER ASSIGN expression"
    symbol_table[p[1]] = p[3]
    print(f"{p[1]} = {p[3]}")


def p_expression_binop(p):
    """
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression MODULO expression
               | expression GREATER_THAN expression
               | expression LESS_THAN expression
               | expression GREATER_EQUAL expression
               | expression LESS_EQUAL expression
               | expression EQUAL expression
               | expression NOT_EQUAL expression
    """
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "%": lambda x, y: x % y,
        ">": lambda x, y: x > y,
        "<": lambda x, y: x < y,
        ">=": lambda x, y: x >= y,
        "<=": lambda x, y: x <= y,
        "==": lambda x, y: x == y,
        "!=": lambda x, y: x != y,
    }
    p[0] = operators[p[2]](p[1], p[3])


def p_expression_group(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]


def p_expression_number(p):
    "expression : INTEGER"
    p[0] = p[1]


def p_expression_float(p):
    "expression : FLOAT"
    p[0] = p[1]


def p_expression_identifier(p):
    "expression : IDENTIFIER"
    p[0] = symbol_table.get(p[1], 0)


def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")


def p_statement_print(p):
    "statement : PRINT LPAREN expression RPAREN"
    print(f"{p[3]}")


parser = yacc.yacc()


bliss_code = """
x = 2.5
y = 20
z = x + y
print(z)
x = x * 5
print(x)
"""

if __name__ == "__main__":
    print("Processing Bliss code:")
    parser.parse(bliss_code)
