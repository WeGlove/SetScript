from set_ast.node import Node
from set_ast.Environment import Environment


class WhileLoop(Node):

    def __init__(self, condition, statements):
        self.condition = condition
        self.statements = statements

    def execute(self, env: Environment):
        while self.condition.execute(env)[1] == frozenset():
            for statement in self.statements:
                env, _ = statement.execute(env)
                if env.return_flag:
                    break
        return env, None

    def __str__(self):
        return "while"
