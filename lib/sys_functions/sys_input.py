from set_ast.node import Node
from set_math import SetMath


class SysInput(Node):

    def __init__(self):
        self.parameters = []
    
    def execute_body(self, env=None):
        s = input("Make an input")
        res_tuple = SetMath.string_to_set(s)
        return env.super_env.super_env, res_tuple

    def __str__(self):
        return "print"
