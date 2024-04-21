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


def p_block(p):
    """
    block : INDENT statements OUTDENT
    """
    p[0] = p[2]


def p_statements(p):
    """
    statements : statement
               | statements statement
    """
    if len(p) == 2:
        p[0] = [p[1]]
        print(f"Adding single statement at line: {p.lineno(1)}")
    else:
        p[0].append(p[2])
        print(f"Appending statement at line: {p.lineno(2)}")


def p_statement(p):
    """
    statement : simple_statement
              | compound_statement
    """
    p[0] = p[1]


def p_simple_statement(p):
    """
    simple_statement : expression_stmt
                     | assignment_stmt
                     | print_stmt
    """
    p[0] = p[1]


def p_compound_statement(p):
    """
    compound_statement : if_stmt
    """
    p[0] = p[1]


def p_if_stmt(p):
    """
    if_stmt : IF expression COLON block
            | IF expression COLON block ELSE COLON block
    """
    if len(p) == 5:
        p[0] = ("if", p[2], p[4])
        print(f"Processed IF without ELSE at line {p.lineno(1)}")
    elif len(p) == 8:
        p[0] = ("if-else", p[2], p[4], p[7])
        print(f"Processed IF with ELSE at line {p.lineno(1)}")


def p_expression_stmt(p):
    "expression_stmt : expression"
    p[0] = p[1]


def p_assignment_stmt(p):
    "assignment_stmt : IDENTIFIER ASSIGN expression"
    symbol_table[p[1]] = p[3]
    p[0] = (p[1], p[3])


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
        print(f"Syntax error at '{p.value}', type: {p.type}, line: {p.lineno}")
    else:
        print("Syntax error at EOF")


def p_print_stmt(p):
    "print_stmt : PRINT LPAREN expression RPAREN"
    print(f"{p[3]}")


parser = yacc.yacc()


with open("tests/sample.bs", "r", encoding="utf-8") as f:
    bliss_code = f.read()

if __name__ == "__main__":
    print("Processing Bliss code:")
    parser.parse(bliss_code)
