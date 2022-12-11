from set_ast.node import Node
from set_ast.Environment import Environment


class FunctionCall(Node):

    def __init__(self, identifier, expressions):
        self.identifier = identifier
        self.expressions = expressions

    def execute(self, env: Environment):

        scope_env = Environment()
        qualified_env = Environment()
        if len(self.identifier.names) > 1:
            names = self.identifier.names[:-1]
            qualified_env = env.get_value(names)

        scope_env.super_env = qualified_env
        qualified_env.super_env = env

        function = env.get_value(self.identifier.names)
        for parameter, expression in zip(function.parameters, self.expressions):
            env, val = expression.execute(env)
            scope_env.set_value(parameter, val)

        _, val = function.execute_body(scope_env)

        qualified_env.super_env = None

        return env, val

    def __str__(self):
        ...