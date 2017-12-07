import foo
from unittest import TestCase


class TestFoo(TestCase):
    def test_foo(self):
        self.assertEqual(foo.foo(), 1)

