from set_ast.node import Node
from set_ast.Environment import Environment


class WhileLoop(Node):

    def __init__(self, set_class,  condition, statements):
        self.condition = condition
        self.statements = statements
        self.set_class = set_class

    def execute(self, env: Environment):
        while self.condition.execute(env)[1] == frozenset():
            for statement in self.statements:
                env, _ = statement.execute(env)
                if env.return_flag:
                    break
                elif env.continue_flag:
                    env.continue_flag = False
                    continue
                elif env.break_flag:
                    env.break_flag = False
                    break
            if env.return_flag:
                break
        return env, None

    def __str__(self):
        return "while"
