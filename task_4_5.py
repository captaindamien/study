"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте максимум возможностей, изученных на уроках по ООП.
"""
werehouse_equipments = dict()
units = dict()


class OfficeWerehouse:
    def __init__(self, type, quantity):

        self.type = type
        self.quantity = quantity

    def receipt(self):
        # при вызове сразу добавляет на склад
        OfficeWerehouse.storage(self)
        return f"На склад поступил {self.type}, в кол-ве {self.quantity} шт." \
               f"\nОбщий остаток {self.type} на складе: {werehouse_equipments[self.type]}"

    @staticmethod
    def deliver(type, name_of_unit, quantity):

        werehouse_equipments[type] -= quantity
        if name_of_unit in units:
            if type in units[name_of_unit]:
                units[name_of_unit][type] += quantity
            else:
                units[name_of_unit][type] = quantity
        else:
            units[name_of_unit] = {type: quantity}
        return f"Со склада списан {type}, в кол-ве {quantity} шт для подразделения {name_of_unit}." \
               f"\nОбщий остаток {type} на складе: {werehouse_equipments[type]}"

    # хранит весь перечень товаров
    def storage(self):
        if self.type in werehouse_equipments:
            werehouse_equipments[self.type] += self.quantity
        else:
            werehouse_equipments[self.type] = self.quantity

    @staticmethod
    def avaliable(type=input("Введите тип техники, остаток которой желаете получить: ")):
        return f"Остаток {type} на складе: {werehouse_equipments[type]}"


class OfficeEquipments(OfficeWerehouse):
    def stand(self):
        return f"Стоит и ничего с ним не происходит"

    def broke(self):
        return f"Сломался!"

    def consume_electricity(self):
        return f"Тратит ваши деньги потребляя энергию :("


class Printer(OfficeEquipments):
    def print(self):
        return f"Напечатал документ на листе А4"


class Xerox(OfficeEquipments):
    def copy(self):
        return f"Скопировал ваш документ"


class Scanner(OfficeEquipments):
    def scan(self):
        return f"Отсканировал ваш документ"
