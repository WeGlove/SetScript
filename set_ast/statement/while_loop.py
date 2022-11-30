from set_ast.node import Node


class WhileLoop(Node):

    def __init__(self, condition, statements):
        self.condition = condition
        self.statements = statements

    def execute(self, env=None):
        while self.condition.execute(env)[1] == frozenset():
            for statement in self.statements:
                env, _ = statement.execute(env)
        return env, None

    def __str__(self):
        return "while"
