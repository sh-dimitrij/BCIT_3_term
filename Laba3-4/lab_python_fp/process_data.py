
import json
from print_result import print_result1
from cm_timer import cm_timer_1
from gen_random import gen_random
from unique import Unique

path = "C:/Users/Dima/Documents/tasks_c++/Python/Laba3/lab_python_fp/data_light.json"
with open(path, encoding="utf8") as f:
    data = json.load(f)


def f1(arg):
    return sorted(Unique([i["job-name"] for i in arg], ignore_case=True).__next__())


def f2(arg):
    
    return list(filter(lambda n: "программист" == n.split()[0].strip(), arg))


def f3(arg):
    return list(map(lambda n: n + " с опытом Python", arg))


@print_result1
def f4(arg):
    randres = gen_random(len(arg), 100000, 200000)
    res = list(zip(arg, randres))
    return [x[0] + ", зарплата " + str(x[1]) + " руб." for x in res]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))