
data1 = [4, -30, 100, -100, 123, 1, 0, -1, -4]
def res(data):
    res = sorted(data, key=abs, reverse = True)
    print(res)
def res_with_lambda(data):
    result_with_lambda = sorted(data, key=lambda n: n*n, reverse = True)
    print(result_with_lambda)

if __name__ == '__main__':
    res(data1)
    print('=====================')
    res_with_lambda(data1)
    