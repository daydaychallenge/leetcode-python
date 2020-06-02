import unittest
from minimum_window_substring import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual("BANC", sol.minWindow("ADOBECODEBANC", "ABC"))


if __name__ == '__main__':
    unittest.main()
