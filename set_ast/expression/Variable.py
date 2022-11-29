class Variable:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def execute(self, env=None):
        return env, env[self.name]