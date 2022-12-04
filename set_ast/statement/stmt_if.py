from set_ast.node import Node
from set_ast.Environment import Environment


class StmtIf(Node):

    def __init__(self, condition, if_statements, else_statements):
        self.condition = condition
        self.if_statements = if_statements
        self.else_statements = else_statements

    def execute(self, env: Environment):
        env, val = self.condition.execute(env)
        for statement in (self.if_statements if val == frozenset() else self.else_statements):
            env, _ = statement.execute(env)

        return env, None

