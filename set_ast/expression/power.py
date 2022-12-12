from set_ast.node import Node
from set_ast.Environment import Environment


class Power(Node):

    def __init__(self, expr):
        self.expr = expr

    def execute(self, env: Environment):
        env, val = self.expr.execute(env)

        out = self.compute_power_set(list(val))

        return env, out

    def compute_power_set(self, elements):
        if len(elements) == 0:
            return frozenset([frozenset()])
        else:
            val = elements[0]
            new_elements = elements[1:]

            pow = self.compute_power_set(new_elements)

            pow = pow.union(frozenset([x.union(frozenset(val)) for x in pow]))

            return pow

    def __str__(self):
        return "P(...)"
