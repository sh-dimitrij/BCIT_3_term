import sys
import math

def correct_vvod_float(floatik, index):
    try:
        float(floatik)
        if ((float(floatik) == 0) and (index == 1)):
            print("A!=0, так как это не биквадратное уравнение. Повторите попытку")
            return 0
        return 1
    except ValueError:
        print("Неверный ввод. Повторите попытку")
        return 0
def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
        while not(correct_vvod_float(coef_str,index)):
            coef_str = input()
        # Переводим строку в действительное число
        coef = float(coef_str)
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    '''
    # Биквадратное уравнение
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = math.sqrt((-b + sqD) / (2.0*a))
        root2 = -math.sqrt((-b + sqD) / (2.0*a))
        root3 = math.sqrt((-b - sqD) / (2.0*a))
        root4 = -math.sqrt((-b - sqD) / (2.0*a))
        result.append(root1)
        result.append(root2)
        result.append(root3)
        result.append(root4)
        
    elif D < 0.0:
        print("complex numbers")
    return result


def main():
    '''
    Основная функция
    '''
    print("Решаем биквадратное уравнение a*x^4 + b*x^2 + c = 0")
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    
    for i in range (0,len(roots)):
        if roots[i] == -0:
            roots[i] = 0
    answer = [a for i, a in enumerate(roots) if not(a in roots[:i])]
    # Вывод корней


    len_roots = len(answer)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {:.3f}'.format(answer[0]))
    elif len_roots == 2:
        print('Два корня: {:.3f} и {:.3f}'.format(answer[0], answer[1]))
    elif len_roots == 3:
        print('Три корня: {:.3f}, {:.3f} и {:.3f}'.format(answer[0], answer[1], answer[2]))
    elif len_roots == 4:
        print('Четыре корня: {:.3f}, {:.3f}, {:.3f} и {:.3f}'.format(answer[0], answer[1], answer[2], answer[3]))

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
