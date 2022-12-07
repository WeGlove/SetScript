from execute_file import excecute_file
from set_ast.Environment import Environment

if __name__ == "__main__":
    path = "test.txt"
    env = Environment()
    excecute_file(path, env)