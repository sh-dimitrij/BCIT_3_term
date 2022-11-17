# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки
import random
def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)
    # Необходимо реализовать генератор

if __name__ == "__main__":
    print(*gen_random(5,1,3))