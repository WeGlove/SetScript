from execute_file import compile
from set_ast.Environment import Environment
from sets.NormalSet import NormalSet
from factory.var_set_factory.PlainSetfactory import VarSetSetFactory


if __name__ == "__main__":
    path = "test.txt"
    factory = VarSetSetFactory(NormalSet)
    env = Environment()
    ast = compile(path, factory)
    ast.execute(env)
    print(env)
