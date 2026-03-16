import unittest
from unittest.mock import patch

from lecture import randomised_function

class MyTestCase(unittest.TestCase):

    def test_randomised_function(self):
        self.assertEqual('software', randomised_function())  # This will pass or fail randomly
        # TODO: Can we make this test deterministic? (HINT: Mock testing)

    # Another solution is to control the randint function instead. So make it return a specific value rather than random.
    # But my solution targets is_small

    @patch('lecture.is_small')
    def test_randomised_function_deterministic_software(self, mock_is_small):
        mock_is_small.return_value = True
        self.assertEqual('software', randomised_function())  # This will pass or fail randomly

    @patch('lecture.is_small')
    def test_randomised_function_deterministic_engineering(self, mock_is_small):
        mock_is_small.return_value = False
        self.assertEqual('engineering', randomised_function())  # This will pass or fail randomly
