from set_ast.node import Node


class SysPrint(Node):

    def __init__(self):
        self.parameters = ["X"]
    
    def execute_body(self, env=None):
        print(env.get_value(self.parameters[0]))
        return env.super_env.super_env, frozenset()

    def __str__(self):
        return "print"
