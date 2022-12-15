import unittest
import time
def fibonachi(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


class TestEquation(unittest.TestCase):
    def test_fibonachi_1(self):
        exp_res = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        res = [i for i in fibonachi(10)]
        print(res)
        res1 = [0] * (len(res))
        
        for i in range(1,len(res)):
            res1[i] = res[i-1]
        self.assertEqual(res1, exp_res)

    def test_fibonachi_2(self):
        expected_res = []
        res = [i for i in fibonachi(0)]
        self.assertEqual(res, expected_res)
    def test_fibonachi_4(self): # ленивые вычисления
        start_time = time.time()
        s = fibonachi(999999)
        end_time = time.time() - start_time
        self.assertLess(end_time, 1)



if __name__ == '__main__':
    print(fibonachi(10))
    unittest.main()
