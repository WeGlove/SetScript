from set_ast.node import Node
from set_ast.Environment import Environment


class StmtIf(Node):

    def __init__(self,  set_class, condition, if_statements, else_statements):
        self.condition = condition
        self.if_statements = if_statements
        self.else_statements = else_statements
        self.set_class = set_class

    def execute(self, env: Environment):
        env, val = self.condition.execute(env)
        for statement in (self.if_statements if val == frozenset() else self.else_statements):
            env, val = statement.execute(env)
            if env.return_flag or env.continue_flag or env.break_flag:
                return env, val

        return env, None

