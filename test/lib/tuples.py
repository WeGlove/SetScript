import os.path
from unittest import TestCase
import execute_file
from set_ast.Environment import Environment


class tuple_tests(TestCase):

    def test_swap(self):
        path = os.path.join(".", "test_swap")

        env = Environment()
        env, val = execute_file.excecute_file(path, env)
        val = env.get_value("Y")

        A = frozenset()
        B = frozenset([frozenset()])

        self.assertEqual(val, frozenset([frozenset([B]), frozenset([A,B])]))
