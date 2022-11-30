class Intersection:

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def execute(self, env=None):
        env, lhs_val = self.lhs.execute(env)
        env, rhs_val = self.rhs.execute(env)

        return env, lhs_val & rhs_val