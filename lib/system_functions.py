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
        elif key == "sleep":
            from lib.sys_functions.sys_sleep import SysSleep
            return SysSleep()
        elif key == "input":
            from lib.sys_functions.sys_input import SysInput
            return SysInput()
        else:
            ValueError("Unknown sys function")
