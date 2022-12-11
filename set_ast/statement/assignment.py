from set_ast.node import Node
from set_ast.Environment import Environment


class Assignment(Node):

    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def execute(self, env: Environment):
        env, val = self.expression.execute(env)
        env.set_value(self.variable.names, val)
        return env, None

    def __str__(self):
        return self.variable + "=" + self.expression
