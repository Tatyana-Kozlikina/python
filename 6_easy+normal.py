# Задача-1: Написать класс, например, Worker, который должен содержать информацию
# о работнике (ФИО, оклад, надбавка за напряженность).
# Создать экземпляр класса и передать конкретные данные (примеры ФИО, должности,
# оклад и надбавки). Оклад и надбавку передать в виде строки.
# На основе строки создать атрибут income, который реализовать в виде словаря
# и инкапуслировать. Словарь income должен содержать информацию об окладе и надбавке.
# Применить к экземпляру
# класса метод __dict__ и проверить какой будет результат применения этого метода.
# А комментариях к заданию написать тип результата на русском языке.
# '''

class Worker(object):
    def __init__(self, fio, position, incomeandbonuses):
        self.fio = fio
        self.position = position
        self.__income = {'bare income': int(incomeandbonuses.split(' ')[0]), 'OverIncome': incomeandbonuses.split(' ')[-1]}


incomestr = '1000 1000000'
employed = Worker('Скайворкер Люк Энакинович', 'Зам начлаьника повстанцев', incomestr)
print(employed.__dict__) # в результате выведем словарь

# '''
# Задача-2: Продолжить работу над задачей 1. Создать на основе класса Worker класс
# Position (реализовать наследование). Добавить классу уникальный атрибут -
# % премии к зарплате (от суммы оклада).
# Создать метод расчета зарплаты с учетом только премии.
# Реализовать обращение к этому атриубуту, как к свойству.
# Проверить работу всей структуры на реальных данных, вывести результаты.
# '''

class Position(Worker):
    def __init__(self, fio, position, incomeandbonuses, monthbonus):
        Worker.__init__(self, fio, position, incomeandbonuses)
        self.monthbonus = monthbonus
    @property
    def incomeCalc(self):
        self.incomewithbonus = self.monthbonus * self._Worker__income.get('bare income')

incomestr = '100000 10000000'
employedP = Position('Скайворкер-Органа Лея Энакиновна', 'Начлаьник повстанцев', incomestr, 100)
employedP.incomeCalc
print(employedP.incomewithbonus)

# '''
# Задача-3: Продолжить работу над задачей 2. Реализовать полиморфизм
# использования знака + в методах 1) вывода полного имени работника и возраста
# 2) вычисления общего дохода работника с учетом надбавки .
# Проверить работу всей структуры на реальных данных, вывести результаты.
# '''



# normal
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры
import math
class Triangle(object):
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):

        self.lena = math.sqrt(pow((b_x - a_x),2)+pow((b_y - a_y),2))
        self.lenb = math.sqrt(pow((c_x - a_x),2)+pow((c_y - a_y),2))
        self.lenc = math.sqrt(pow((c_x - b_x),2)+pow((c_y - b_y),2))
        self.__private__atr_sidedict = {'A': self.lena, 'B': self.lenb, 'C': self.lenc, 'a': self.lena, 'b': self.lenb, 'c': self.lenc}
    def square(self):
        return (self.lena*self.lenb*self.lenc)
    def perimetr(self):
        return (self.lena+self.lenb+self.lenc)
    def height(self,side):
        return self.square() * 2/self.__private__atr_sidedict[side]

tr1 = Triangle(0,0,10,10,20,20)
print(tr1.square())
print(tr1.perimetr())
print(tr1.height('A'))