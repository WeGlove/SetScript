from set_ast.node import Node
from set_ast.Environment import Environment


class Function(Node):

    def __init__(self,  set_class, identifier, parameters, statements):
        self.identifier = identifier
        self.parameters = parameters
        self.statements = statements
        self.set_class = set_class

    def execute(self, env: Environment):
        env.set_value(self.identifier.name, self)
        return env, None

    def execute_body(self, env=None):
        for statement in self.statements:
            env, val = statement.execute(env)
            if env.return_flag:
                env.return_flag = False
                break

        if env.super_env is None:
            raise ValueError("Invalid scope atend of function call!")
        return env, val

    def __str__(self):
        return "Function: " + self.identifier
