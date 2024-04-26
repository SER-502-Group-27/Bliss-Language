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


class IndexOrSlicing(ASTNode):
    def __init__(self, list, index_or_slice):
        self.list = list
        self.index_or_slice = index_or_slice

    def eval(self, context):
        self.list = self.list.eval(context)

        if not hasattr(self.list, "__getitem__"):
            raise TypeError(
                f"Type {type(self.list).__name__} does not support indexing or slicing"
            )

        if isinstance(self.index_or_slice, tuple):
            # Handling slicing
            start, stop, step = self.index_or_slice
            start_val = start.eval(context) if start else None
            stop_val = stop.eval(context) if stop else None
            step_val = step.eval(context) if step else None

            if step_val is not None and step_val == 0:
                raise ValueError("Slice step cannot be zero")

            # Adjust for negative indices
            length = len(self.list)
            if start_val and start_val < 0:
                start_val += length
            if stop_val and stop_val < 0:
                stop_val += length

            return self.list[start_val:stop_val:step_val]

        else:
            # Handling simple indexing
            index_val = self.index_or_slice.eval(context)
            if index_val < 0:
                index_val += len(self.list)
            if index_val >= len(self.list) or index_val < 0:
                raise IndexError("List index out of range")
            return self.list[index_val]


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
    def __init__(self, start, stop, step=None):
        self.start = start
        self.stop = stop
        self.step = step

    def eval(self, context):
        start_val = (
            self.start if isinstance(self.start, int) else self.start.eval(context)
        )
        stop_val = self.stop.eval(context)
        if self.step:
            step_val = self.step.eval(context)
            return list(range(start_val, stop_val, step_val))
        else:
            return list(range(start_val, stop_val))


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
