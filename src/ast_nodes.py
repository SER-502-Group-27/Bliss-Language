class ASTNode:
    def eval(self, context):
        pass

class Number(ASTNode):
    def __init__(self, value):
        self.value = value

    def eval(self, context):
        return self.value


class StringLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

    def eval(self, context):
        return self.value


class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name

    def eval(self, context):
        return context.get(self.name, 0)  # Default to 0 if not found


class BinaryOperation(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def eval(self, context):
        lval = self.left.eval(context)
        rval = self.right.eval(context)
        if self.operator == "+":
            return lval + rval
        elif self.operator == "-":
            return lval - rval
        elif self.operator == "*":
            return lval * rval
        elif self.operator == "/":
            return lval / rval
        elif self.operator == "%":
            return lval % rval
        elif self.operator == "==":
            return lval == rval
        elif self.operator == "!=":
            return lval != rval
        elif self.operator == "<":
            return lval < rval
        elif self.operator == ">":
            return lval > rval
        elif self.operator == "<=":
            return lval <= rval
        elif self.operator == ">=":
            return lval >= rval
        else:
            raise ValueError("Unknown operator")
        

class UnaryOperation(ASTNode):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def eval(self, context):
        value = self.operand.eval(context)
        if self.operator == '-':
            return -value
        elif self.operator == 'not':
            return not value
        else:
            raise ValueError(f"Unsupported unary operator {self.operator}")


class Assignment(ASTNode):
    def __init__(self, identifier, op, expr):
        self.identifier = identifier
        self.op = op
        self.expr = expr

    def eval(self, context):
        if self.op == "=":
            context[self.identifier.name] = self.expr.eval(context)
        elif self.op == "+=":
            context[self.identifier.name] += self.expr.eval(context)
        elif self.op == "-=":
            context[self.identifier.name] -= self.expr.eval(context)
        elif self.op == "*=":
            context[self.identifier.name] *= self.expr.eval(context)
        elif self.op == "/=":
            context[self.identifier.name] /= self.expr.eval(context)
        elif self.op == "%=":
            context[self.identifier.name] %= self.expr.eval(context)

class PrintStatement(ASTNode):
    def __init__(self, expr):
        self.expr = expr

    def eval(self, context):
        print(self.expr.eval(context))


class Block(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def eval(self, context):
        result = None
        for statement in self.statements:
            result = statement.eval(context)
        return result


class IfStatement(ASTNode):
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

    def eval(self, context):
        if self.condition.eval(context):
            return self.then_block.eval(context)
        elif self.else_block:
            return self.else_block.eval(context)


class WhileStatement(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def eval(self, context):
        while self.condition.eval(context):
            self.body.eval(context)


class FunctionDefinition(ASTNode):
    def __init__(self, name, body):
        self.name = name
        self.body = body

    def eval(self, context):
        # Assuming functions do not have parameters and do not return values for simplicity
        context[self.name] = self.body
