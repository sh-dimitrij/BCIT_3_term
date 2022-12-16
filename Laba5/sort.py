
data1 = [4, -30, 100, -100, 123, 1, 0, -1, -4]
def res(data):
    res = sorted(data, key=abs, reverse = True)
    return res
def res_with_lambda(data):
    result_with_lambda = sorted(data, key=lambda n: n*n, reverse = True)
    return result_with_lambda

if __name__ == '__main__':
    print(res(data1))
    print(res([0, -300, 300, 54, -54, 54, 99, 19, 14, -19]))
    print(res_with_lambda(data1))
    