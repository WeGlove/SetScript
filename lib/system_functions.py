class SystemFunctions:

    def __init__(self):
        self.super_env = None

    def get_value(self, keys):
        if len(keys) > 0:
            ValueError()

        key = keys[0]

        if key == "out":
            from lib.sys_functions.sys_print import SysPrint
            return SysPrint()
        else:
            ValueError("Unknwown sys function")