class Environment:

    def __init__(self, assignments=None, super_env=None):
        self.assignments = assignments if assignments is not None else {}
        self.super_env = super_env
        self.scope_close = False

    def get_value(self, key):
        if key in self.assignments.keys():
            return self.assignments[key]
        else:
            if self.super_env is None:
                raise ValueError(f"{key} not Found in Environment")
            else:
                return self.super_env.get_value(key)

    def set_value(self, key, val):
        self.assignments[key] = val

    def close_scope(self):
        self.scope_close = True

    def __str__(self):
        return str(self.assignments)