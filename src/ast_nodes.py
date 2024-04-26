from calendar import c


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


class Boolean(ASTNode):
    def __init__(self, value):
        self.value = value

    def eval(self, context):
        return self.value


class List(ASTNode):
    def __init__(self, elements):
        self.elements = elements

    def eval(self, context):
        return [element.eval(context) for element in self.elements]


class Index(ASTNode):
    def __init__(self, list, index):
        self.list = list
        self.index = index

    def eval(self, context):
        self.list = self.list.eval(context)
        self.index = self.index.eval(context)

        if not hasattr(self.list, "__getitem__"):
            raise ValueError(f"Cannot index into {self.list}")

        if not isinstance(self.index, int):
            if self.index.is_integer():
                self.index = int(self.index)
            else:
                raise ValueError(f"Index {self.index} is not an integer")

        if not 0 <= self.index < len(self.list):
            raise ValueError(f"Index {self.index} out of range")

        return self.list[self.index]


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
        if self.operator == "-":
            return -value
        elif self.operator == "not":
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


class Range(ASTNode):
    def __init__(self, end):
        self.end = end

    def eval(self, context):
        return list(range(self.end.eval(context)))


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
