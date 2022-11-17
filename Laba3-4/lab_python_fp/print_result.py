def print_result1(func):
    def wrapper(args):
        print(func.__name__)
        f = func(args)
        if type(f) == dict:
            for i in f:
                print(i, '=', f.get(i))
            return 0

        if type(f) == list:
            print(*f, sep="\n")
            return 0
        
        else:
            print(f)
        
    return wrapper
def print_result(func):
    def wrapper():
        print(func.__name__)
        f = func()
        if type(f) == dict:
            for i in f:
                print(i, '=', f.get(i))
            return 0

        if type(f) == list:
            print(*f, sep="\n")
            return 0
        
        else:
            print(f)
        
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()