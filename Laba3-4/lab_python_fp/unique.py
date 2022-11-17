# Итератор для удаления дубликатов
from gen_random import gen_random
class Unique(object):
    def __init__(self, items, **kwargs):
        
        self._data = items
        self._ignore_case = kwargs["ignore_case"] if "ignore_case" in kwargs.keys() else False

    def __next__(self):
        
        res = []
        for temp in self._data:
            temp = temp.lower() if type(temp) == str and self._ignore_case else temp
            if temp not in res:
                res.append(temp)
        return res
    def __iter__(self):
        return self

if __name__ == "__main__":
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(Unique(data).__next__())

    data = gen_random(10, 1, 3)
    print(Unique(data).__next__())

    data = ["a", "A", "b", "B", "a", "A", "b", "B"]
    print(Unique(data).__next__())

    print(Unique(data, ignore_case=True).__next__())