from set_ast.node import Node
from set_ast.Environment import Environment


class Function(Node):

    def __init__(self, identifier, parameters, statements):
        self.identifier = identifier
        self.parameters = parameters
        self.statements = statements

    def execute(self, env: Environment):
        env.set_value(self.identifier.name, self)
        return env, None

    def execute_body(self, env=None):
        for statement in self.statements:
            env, val = statement.execute(env)
            if env.scope_close:
                break

        if not env.scope_close:
            raise ValueError()
        if env.super_env is None:
            raise ValueError("Invalid scope atend of function call!")
        return env, val

    def __str__(self):
        return "Function: " + self.identifier
