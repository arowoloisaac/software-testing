import unittest
from main import Solution


class TestTwoSum(unittest.TestCase):

    arr = [2, 7, 11, 15]

    def setUp(self):
        self.solution = Solution()

    """ The following test below are for the equivalence partitioning """
    # Test input with two numbers that add up to the target
    def test_with_any_integer(self):
        target = 9
        self.assertEqual(self.solution.twoSum(self.arr, target), [1, 2])

    def test_with_negative_number(self):
        numbers = [-5, -4, -3, -2, -1]
        target = -6
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 5])

    # Test input with two numbers where one number is zero and the other is the target
    def test_with_zero_target(self):
        numbers = [-1, 0, 1]
        target = 1
        self.assertEqual(self.solution.twoSum(numbers, target), [2, 3])

    # Test input with two numbers where both numbers are the target
    def test_input_same_target(self):
        numbers = [2, 2]
        target = 4
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 2])

    def test_input_no_solution(self):
        self.assertEqual(self.solution.twoSum(self.arr, 10), [])

    def test_with_mixed_number(self):
        numbers = [-5, -3, 0, 2, 4]
        target = -1
        self.assertEqual(self.solution.twoSum(numbers, target), [2, 3])

    """The below are test of boundary value analysis """

    lst = []

    def test_with_empty_list(self):
        numbers = []
        target = 0
        self.assertEqual(self.solution.twoSum(numbers, target), self.lst)  # []

    def test_with_single_length(self):
        numbers = [1]
        target = 1
        self.assertEqual(self.solution.twoSum(numbers, target), self.lst)

    def test_with_arrayEqual_target(self):
        numbers = [1, 2]
        target = 3
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 2])
        # print(self.solution.twoSum(numbers, target), [1, 2])

    """ Test with a list of length 2 where the sum is smaller or larger than target
        NB this two will be a bug as it is a failed test  """
    def test_with_smallerLarger_target(self):
        numbers = [1, 2]
        target = 5
        self.assertEqual(self.solution.twoSum(numbers, target), [])

        numbers = [1, 2]
        target = 2
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 2])


if __name__ == '__main__':
    unittest.main()
