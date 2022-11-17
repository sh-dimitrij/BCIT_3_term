
b1 = [(x, x ** 2) for x in [i for i in range(1,10)]]
print(b1)

b2 = list(map(lambda n: (n, n ** 2), [x for x in range(1,10)]))
print(b2)

b3 = map(lambda x, y: (x, y), [i for i in range(1,10)], [x ** 2 for x in [i for i in range(1,10)]])
print(list(b3))

b4 = zip([x for x in range(1,10)], [x ** 2 for x in [i for i in range(1,10)]])
print(list(b4))

