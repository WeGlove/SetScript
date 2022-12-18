from set_ast.node import Node
from set_ast.Environment import Environment


class ForLoop(Node):

    def __init__(self, start, condition, induction, statements):
        self.start = start
        self.condition = condition
        self.induction = induction
        self.statements = statements

    def execute(self, env: Environment):
        env, _ = self.start.execute(env)
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
            env, _ = self.induction.execute(env)
        return env, None

    def __str__(self):
        return "for"
