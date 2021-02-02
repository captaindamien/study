"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        return f"Ваша матрица:\n{self.args[0]}\n{self.args[1]}\n{self.args[2]}"

    def __add__(self, other):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for el in range(len(self.args)):
            for el_2 in range(len(other.args)):
                result[el][el_2] = self.args[el][el_2] + other.args[el][el_2]
        return f"Результат сложения двух матриц:\n{result[0]}\n{result[1]}\n{result[2]}"


first_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
second_matrix = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(first_matrix)
print(first_matrix + second_matrix)