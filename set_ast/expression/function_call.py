from set_ast.node import Node
from set_ast.Environment import Environment


class FunctionCall(Node):

    def __init__(self, identifier, expressions):
        self.identifier = identifier
        self.expressions = expressions

    def execute(self, env=None):
        scope_env = Environment(super_env=env)
        function = env.get_value(self.identifier.name)
        for parameter, expression in zip(function.parameters, self.expressions):
            env, val = expression.execute(env)
            scope_env.set_value(parameter, val)
        return function.execute_body(scope_env)

    def __str__(self):
        ...