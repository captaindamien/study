"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def coat_formula(self):
        pass

    @abstractmethod
    def costume_formula(self):
        pass


class Coat(Cloth):
    def __init__(self, v):
        self.v = v

    @property
    def coat_formula(self):
        return f"Кол-во ткани требуемое для пальто:{self.v / 6.5 + 0.5: .2f}м"

    def costume_formula(self):
        pass


class Costume(Cloth):
    def __init__(self, h):
        self.h = h

    @property
    def costume_formula(self):
        return f"Кол-во ткани требуемое для костюма:{2 * self.h + 0.3: .2f}м"

    def coat_formula(self):
        pass


size = Costume(2)
print(size.costume_formula)
height = Coat(6)
print(height.coat_formula)
