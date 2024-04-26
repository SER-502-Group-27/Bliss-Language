import ply.yacc as yacc
from lexer import tokens, lexer
from ast_nodes import (
    Block,
    PrintStatement,
    BinaryOperation,
    Number,
    Boolean,
    Identifier,
    StringLiteral,
    UnaryOperation,
    Assignment,
    IfStatement,
    WhileStatement,
    FunctionDefinition,
)


# Precedence and associativity of operators
precedence = (
    ("right", "NOT"),
    ("left", "OR"),
    ("left", "AND"),
    (
        "nonassoc",
        "LESS_THAN",
        "GREATER_THAN",
        "LESS_EQUAL",
        "GREATER_EQUAL",
        "EQUAL",
        "NOT_EQUAL",
    ),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE", "MODULO"),
    ("right", "UMINUS"),  # Unary minus and logical not
)


def p_program(p):
    """
    program : statements
    """
    p[0] = Block(p[1])


def p_statements(p):
    """
    statements : statements statement
               | statement
    """
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_statement(p):
    """
    statement : assignment
              | expression
              | control_flow
              | function_definition
              | PRINT LPAREN expression RPAREN
    """
    if len(p) == 5:
        p[0] = PrintStatement(p[3])
    else:
        p[0] = p[1]


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
    p[0] = BinaryOperation(p[1], p[2], p[3])


def p_expression_group(p):
    """
    expression : LPAREN expression RPAREN
    """
    p[0] = p[2]


def p_expression_number(p):
    """
    expression : INTEGER
               | FLOAT
    """
    p[0] = Number(p[1])


def p_expression_identifier(p):
    """
    expression : IDENTIFIER
    """
    p[0] = Identifier(p[1])


def p_expression_string(p):
    """
    expression : STRING_LITERAL
    """
    p[0] = StringLiteral(p[1])


def p_expression_boolean(p):
    """
    expression : BOOLEAN
    """
    p[0] = Boolean(p[1])


def p_expression_negate(p):
    """
    expression : MINUS expression %prec UMINUS
               | NOT expression %prec NOT
    """
    if p[1] == "-":
        p[0] = UnaryOperation("-", p[2])
    else:
        p[0] = UnaryOperation("not", p[2])


def p_assignment(p):
    """
    assignment : IDENTIFIER ASSIGN expression
               | IDENTIFIER ADD_ASSIGN expression
               | IDENTIFIER SUB_ASSIGN expression
               | IDENTIFIER MUL_ASSIGN expression
               | IDENTIFIER DIV_ASSIGN expression
               | IDENTIFIER MOD_ASSIGN expression
    """
    p[0] = Assignment(Identifier(p[1]), p[2], p[3])


def p_control_flow(p):
    """
    control_flow : if_statement
                 | while_statement
    """
    p[0] = p[1]


def p_if_statement(p):
    """
    if_statement : IF expression COLON block ELSE COLON block
                 | IF expression COLON block
    """
    if len(p) == 8:
        p[0] = IfStatement(p[2], p[4], p[7])
    else:
        p[0] = IfStatement(p[2], p[4])


def p_while_statement(p):
    """
    while_statement : WHILE expression COLON block
    """
    p[0] = WhileStatement(p[2], p[4])


def p_block(p):
    """
    block : INDENT statements OUTDENT
    """
    p[0] = Block(p[2])


def p_function_definition(p):
    """
    function_definition : DEF IDENTIFIER LPAREN RPAREN COLON block
    """
    p[0] = FunctionDefinition(p[2], p[6])


def p_error(p):
    print(
        f"Syntax error at {p.value} on line {p.lineno}" if p else "Syntax error at EOF"
    )


def preprocess_input(data):
    """Ensure the input data ends with a newline for proper lexing."""
    if not data.endswith("\n"):
        data += "\n"
    return data


# Build the parser
parser = yacc.yacc()


def parse(data):
    return parser.parse(data, lexer=lexer)


if __name__ == "__main__":
    with open("tests/sample.bs", "r", encoding="utf-8") as f:
        bliss_code = f.read()
    ast = parse(preprocess_input(bliss_code))
    ast.eval({})  # Execute with an empty context
