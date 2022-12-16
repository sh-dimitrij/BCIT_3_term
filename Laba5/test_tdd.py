import unittest
import sort
class test_sort(unittest.TestCase):
    def test_res1(self):
        data = [2, -6, 3, 0, 7]
        result = [7, -6, 3, 2, 0]
        assert result == sort.res(data)
    def test_res2(self):
        data = [2, -5, 5, 8, 0, 1, -1, 13]
        result = [13, 8, -5, 5, 2, 1, -1, 0]
        self.assertEqual(sort.res(data), result)
    def test_res3(self):
        self.assertEqual(sort.res([0, -300, 300, 54, -54, 54, 99, 19, 14, -19]), [-300, 300, 99, 54, -54, 54, 19, -19, 14, 0])
    
    def test_rwl1(self):
        data = [2, -6, 3, 0, 7]
        result = [7, -6, 3, 2, 0]
        assert result == sort.res_with_lambda(data)
    def test_rwl2(self):
        data = [2, -5, 5, 8, 0, 1, -1, 13]
        result = [13, 8, -5, 5, 2, 1, -1, 0]
        self.assertEqual(sort.res_with_lambda(data), result)
    def test_rwl3(self):
        self.assertEqual(sort.res_with_lambda([0, -300, 300, 54, -54, 54, 99, 19, 14, -19]), [-300, 300, 99, 54, -54, 54, 19, -19, 14, 0])
if __name__ == "__main__":
    unittest.main() 