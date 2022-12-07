from lib.system_functions import SystemFunctions


class Environment:

    def __init__(self, assignments=None, super_env=None):
        self.assignments = assignments if assignments is not None else {}
        self.super_env = super_env
        self.scope_close = False

    def get_value(self, keys):
        if type(keys) == str:
            keys = [keys]

        key = keys[0]
        if key in self.assignments.keys():
            if len(keys) == 1:
                return self.assignments[key]
            else:
                return self.assignments[key].get_value(keys[1:])
        elif keys[0] == "sys":
            env = SystemFunctions()
            if len(keys) > 1:
                return env.get_value(keys[1:])
            else:
                return env
        else:
            if self.super_env is None:
                raise ValueError(f"{key} not Found in Environment")
            else:
                print(keys)
                return self.super_env.get_value(keys)

    def set_value(self, keys, val):
        if type(keys) == str:
            keys = [keys]
        key = keys[0]

        if key in self.assignments.keys():
            if len(keys) == 1:
                self.assignments[key] = val
            else:
                self.assignments[key].set_value(keys[1:])
        else:
            if len(keys) > 1:
                if self.super_env is None:
                    raise ValueError("Namespace doesnt exist!")
                else:
                    self.super_env.set_value(keys)
            else:
                self.assignments[key] = val

    def close_scope(self):
        self.scope_close = True

    def __str__(self):
        return str(self.assignments)