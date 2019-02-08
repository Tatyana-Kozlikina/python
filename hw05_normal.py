# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
# ИСПОЛЬЗОВАТЬ МОДУЛЬ OS и SHUTIL
import os

def getCurFolderContent(path):
    if os.path.exists(path):
        return os.listdir(path)
    else:
        return 'Не удалось отобразить'


def changeDir(path):
    if os.path.exists(path):
        os.chdir(path)
        return 'Перешел'
    else:
        return 'Не перешел'


def delFolder(path):
    if os.path.exists(path):
        os.rmdir(path)
        return 'Удалил'
    else:
        return 'Не удалил'


def createFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)
        return 'Создал'
    else:
        return 'Не создал'


import datetime
curdate = datetime.datetime.now()
curdate = (int(curdate.strftime("%j")))
createdate = 737058 + curdate


while(1):
    print (''' 
****************************************************************** 
** 1111!!!!BEST CLI UTILITY EVER!!!!1111 ** 
****************************************************************** 
Выберите действия: 
—--------------------------------------------------------------— 
[1] - Перейти в папку 
или Go-Go-Go! 
[2] - Просмотреть содержимое папки 
от создателей "А если найду" 
[3] - Удалить папку 
aka Finish HIM!!! 
[4] - Создать папку 
на %d день бог все же создал эту папку 
[0] - Закончить 
мучить файловую систему 

—--------------------------------------------------------------— 

*** При каждом не правильном вводе в мире будет погибать 1 котенок 

''' % createdate)
    userinput = input('->')
    if userinput == '0':
        print('Гудбай')
        os._exit(0)
    elif userinput == '1':
        print('Переходим в папку ')
        userpath = input('Введите путь:')
        while not os.path.exists(userpath):
            print('Ну вот на одного котенка меньше')
            userpath = input('Введите путь:')
            if not userpath:
                userpath = os.getcwd()
                print('ну раз так берем путь ->', userpath)
        print(changeDir(userpath))
    elif userinput == '2':
        userpath = input('Введите путь:')
        while not os.path.exists(userpath):
            print('Ну вот на одного котенка меньше')
            userpath = input('Введите путь:')
        print(getCurFolderContent(userpath))
    elif userinput == '3':
        userpath = input('Введите путь:')
        while not os.path.exists(userpath):
            print('Ну вот на одного котенка меньше')
            userpath = input('Введите путь:')
        print(delFolder(userpath))
    elif userinput == '4':
        userpath = input('Введите путь:')
        while os.path.exists(userpath):
            print('Ну вот на одного котенка меньше')
            userpath = input('Введите путь:')
        print(createFolder(userpath))











