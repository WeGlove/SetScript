import time
from set_ast.node import Node
from set_math import SetMath


class SysSleep(Node):

    def __init__(self):
        self.parameters = ["X"]
    
    def execute_body(self, env=None):
        X = env.get_value(self.parameters[0])
        t = SetMath.build_number(X)
        time.sleep(t)

        return env.super_env.super_env, X

    def __str__(self):
        return "Sleep"
