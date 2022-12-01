class Variable:

    def __init__(self, name):
        self.name = name

    def execute(self, env=None):
        return env, env.get_value(self.name)

    def __str__(self):
        return f"Variable: {self.name}"