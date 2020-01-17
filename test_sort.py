
import unittest
import sort

class TestCode(unittest.TestCase):
    def test_one(self):
        test = ["beg", "life", "i", "to"]
        self.assertEqual(sort.sort_by_length(test), ["i", "to", "beg", "life"])

    def test_two(self):
        test = ["", "moderately", "brains", "pizza"]
        self.assertEqual(sort.sort_by_length(test), ["", "pizza", "brains", "moderately"])

if __name__ == '__main__':
    unittest.main()

# test.describe("Example Tests")

# tests = [
#     [["i", "to", "beg", "life"], ["beg", "life", "i", "to"]],
#     [["", "pizza", "brains", "moderately"], ["", "moderately", "brains", "pizza"]],
#     [["short", "longer", "longest"], ["longer", "longest", "short"]],
#     [["a", "of", "dog", "food"], ["dog", "food", "a", "of"]],
#     [["", "bees", "eloquent", "dictionary"], ["", "dictionary", "eloquent", "bees"]],
#     [["a short sentence", "a longer sentence", "the longest sentence"], ["a longer sentence", "the longest sentence", "a short sentence"]],
# ]

# for exp, inp in tests:
#     test.assert_equals(sort_by_length(inp), exp)
