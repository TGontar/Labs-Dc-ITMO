import unittest
from main import insertionSort


class TestSort(unittest.TestCase):
    def test_oneValue(self):
        self.assertEqual(insertionSort([1]), [1])

    def test_sameValues(self):
        self.assertEqual(insertionSort([4, 4, 4, 4, 4]), [4, 4, 4, 4, 4])

    def test_allDifferentValues(self):
        self.assertEqual(insertionSort([5, 1, 3, 4, 2]), [1, 2, 3, 4, 5])

    def test_differentValues1(self):
        self.assertEqual(insertionSort([3, 2, 2, 1, 54, 2]), [1, 2, 2, 2, 3, 54])

    def test_differentValues2(self):
        self.assertEqual(insertionSort([43, 4, 2, 1, 1, 64, 4, 10]), [1, 1, 2, 4, 4, 10, 43, 64])

    def test_differentValues3(self):
        self.assertEqual(insertionSort([3, 654, 23, 7654, 1]), [1, 3, 23, 654, 7654])

    def test_bigValues(self):
        self.assertEqual(insertionSort([12_030_100, 423_234_543, 43_432_327]), [12_030_100, 43_432_327, 423_234_543])

    def test_manyValues(self):
        self.assertEqual(insertionSort([1 for i in range(1000)]), [1 for i in range(1000)])

    def test_manyDifferentValues(self):
        self.assertEqual(insertionSort([i for i in range(1000)]), [i for i in range(1000)])

    def test_manyDifferentValuesReversed(self):
        self.assertEqual(insertionSort([999 - i for i in range(1000)]), [i for i in range(1000)])
