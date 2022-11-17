# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
 ]

def field(goods, *args):
    if len(args) == 0:
        yield None 

    for good in goods:
        res = {}
        for a in good:
            if a in args:
                res[a] = good[a]
        yield res

if __name__ == "__main__":
    f1 = field(goods, 'title')
    print(list(f1))
    f2 = field(goods, 'title', 'price')
    print(list(f2))