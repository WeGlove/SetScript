from set_ast.node import Node
from set_math import SetMath


class SysPrint(Node):

    def __init__(self):
        self.parameters = ["X", "type"]
    
    def execute_body(self, env=None):
        content = env.get_value(self.parameters[0])
        type = env.get_value(self.parameters[1])
        if type == frozenset():
            print(self.build_string(content))
        else:
            print(self.build_number(content))
        return env.super_env.super_env, frozenset()

    def build_string(self, to_print, s=""):
        s += "{"

        for element in to_print:
            s = self.build_string(element, s)
            s += ","
        if s[-1] == ",":
            s = s[:-1]
        s += "}"
        return s

    def build_number(self, to_print, s=""):
        num = 0
        while to_print != frozenset():
            to_print = SetMath.big_union(to_print)
            to_print = SetMath.big_union(to_print)
            num += 1
        return str(num)

    def __str__(self):
        return "print"
