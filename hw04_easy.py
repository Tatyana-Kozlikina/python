# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [0, 1, 2, 3] --> [0, 1, 4, 9]
print ('Задание №1')
import random
spisok_1 = [random.randint(- 10,10) for _ in range(10)]
print ( 'Список №1 = ', spisok_1)
spisok_2 = [i**2 for i in spisok_1]
print ( 'Список №2 = ' , spisok_2)
print ('Задание №1 закончено \n')

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
print ('Задание №2')
total_fruit_list = ['apple', 'banana', 'grapes', 'pear', 'pineapple', 'tomato', 'cherry', 'orange', 'strawberry', 'pomello']
rand_fruit_list_1 = random.sample(total_fruit_list, 5)
rand_fruit_list_2 = random.sample(total_fruit_list, 5)

print('список №1 = ', rand_fruit_list_1)
print('список №2 = ', rand_fruit_list_2)

new_fruit_list = list(set(rand_fruit_list_2) & set(rand_fruit_list_1))
print('Список повторяющихся фруктов',new_fruit_list)
print ('Задание №2 закончено \n')


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 2
# + Элемент неотрицательный
# + Элемент не кратен 3
print ('Задание №3')
print()
randlist = [random.randint(-10, 10) for i in range(0, 50)]
print('Список случайных чисел', randlist)

newlist = [i for i in randlist if (((i % 2) == 0) and (i > 0) and ((i % 3) != 0))]
print ('Новый список', newlist)
print ('Задание №3 закончено \n')


