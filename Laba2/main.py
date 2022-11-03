from prettytable import PrettyTable

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

#python C:\Users\Dima\Documents\tasks_c++\Python\Laba2\main.py
def main():
    r = Rectangle("Cинего", 6, 6)
    c = Circle("Зеленого", 6)
    s = Square("Красного", 6)
    print(r)
    print(c)
    print(s)
    x = PrettyTable()
    x.field_names = ["Название фигуры", "Цвет фигуры", "Площадь фигуры"]
    x.add_rows([
        [r.get_figure_type(), r.color, r.square()],
        [c.get_figure_type(), c.fc.color_property, c.square()],
        [s.get_figure_type(), s.color, s.square()]
    ])
    print(x)
if __name__ == "__main__":
    main()
