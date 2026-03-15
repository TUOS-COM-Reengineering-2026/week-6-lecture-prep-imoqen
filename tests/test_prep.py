import unittest
from prep import strange_function

# note: in pytest, Test class must begin with "Test" and tests must be named "test_<name>"
# Full line, branch and condition coverage was attempted. Some paths were infeasible due to conflicting conditions

class TestStrangeFunction(unittest.TestCase):
    # Behaviour 3, already provided:
    def test_should_return_behaviour3(self):
        self.assertEqual(
            first=strange_function(1, 2, 3, 4),
            second='behaviour 3'
        )

    # Behaviour 1: when a == b and c < d
    def test_should_return_behaviour1(self):
        # a == b && c < d case:
        self.assertEqual(
            first=strange_function(1, 1, 3, 4),
            second='behaviour 1'
        )

    # Behaviour 2: when a == b and c >= d
    def test_should_return_behaviour2(self):
        # a == b && c == d case:
        self.assertEqual(
            first=strange_function(1, 1, 4, 4),
            second='behaviour 2'
        )

        # a == b && c > d case:
        self.assertEqual(
            first=strange_function(1, 1, 5, 4),
            second='behaviour 2'
        )

    # Behaviour 4: when a != b and a >= c and d < b
    def test_should_return_behaviour4(self):
       # a != b && a > c && d < b case:
        self.assertEqual(
            first=strange_function(2, 1, 1, 0),
            second='behaviour 4'
        )

        # a != b && a == c && d < b case:
        self.assertEqual(
            first=strange_function(2, 1, 2, 0),
            second='behaviour 4'
        )

    # Behaviour 5: when a != b and a >= c and d >= b and c < a
    def test_should_return_behaviour5(self):
        # a != b && a > c && d > b && c < a case:
        # (c < a is a redundant condition here, as this is already covered by a > c)
        self.assertEqual(
            first=strange_function(2, 1, 1, 3),
            second='behaviour 5'
        )

        # a != b && a == c && d > b && c < a case:
        # not possible: conflicting conditions a == c and c < a.

        # a != b && a == c && d == b && c < a case:
        # not possible: conflicting conditions a == c and c < a.

        # a != b && a > c && d == b && c < a case:
        # (c < a is a redundant condition here, as this is already covered by a > c)
        self.assertEqual(
            first=strange_function(2, 1, 1, 1),
            second='behaviour 5'
        )

    # Behaviour 6: when a != b and a >= c and d >= b and c >= a
    def test_should_return_behaviour6(self):
        # a != b && a > c && d > b && c > a case:
        # not possible: a > c and c > a

        # a != b && a > c && d > b && c = a case:
        # not possible: a > c and c == a

        # a != b && a > c && d = b && c > a case:
        # not possible: a > c and c > a

        # a != b && a > c && d = b && c = a case:
        # not possible: a > c and c == a

        # a != b && a = c && d > b && c > a case:
        # not possible: a == c and c > a

        # a != b && a = c && d > b && c = a case:
        self.assertEqual(
            first=strange_function(2, 1, 2, 3),
            second='behaviour 6'
        )

        # a != b && a = c && d = b && c > a case:
        # not possible: a==c and c > a

        # a != b && a = c && d = b && c = a case:
        self.assertEqual(
            first=strange_function(2, 1, 2, 1),
            second='behaviour 6'
        )

        # in the future, I should try to simplify the logic before writing all of the test cases
        # for each behaviour
        # e.g., a != b and a >= c and d >= b and c >= a simplifies to a != b and a == c and d >= b
        # so from this, I immediately know only two test cases are required

