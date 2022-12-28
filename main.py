from execute_file import compile
from set_ast.Environment import Environment
from sets.NormalSet import NormalSet
from factory.plain_factory.PlainSetfactory import PlainSetFactory


if __name__ == "__main__":
    path = "test.txt"
    factory = PlainSetFactory()
    env = Environment()
    ast = compile(path, factory)
    ast.execute(env)
