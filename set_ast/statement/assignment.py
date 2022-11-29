from set_ast.node import Node


class Assignment(Node):

    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def execute(self, env=None):
        env, val = self.expression.execute(env)
        env[self.variable.name] = val
        return env, None

    def __str__(self):
        return self.variable + "=" + self.expression
