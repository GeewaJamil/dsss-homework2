import unittest
from math_quiz import integer_function, random_application_Choice, operation_definition


class TestMathGame(unittest.TestCase):

    def test_number_choice(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num =integer_function(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operation_choice(self):
        total_operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            operator =random_application_Choice()
            self.assertIn(operator, total_operators)

    def test_selecting_operation(self):
        test_cases = [
            (3, 2, '-', '3 - 2', 1),
            (3, 2, '+', '3 + 2', 5),
            (3, 2, '*', '3 * 2', 6),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = operation_definition(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
