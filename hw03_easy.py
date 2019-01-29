# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print("Задача №1")
def okrugleniye(drobnaya,razryad) :
    dotpos = str(drobnaya).find('.')+1
    if int(str(drobnaya)[razryad+dotpos]) >= 5 :
        newdrobnaya = float(str(drobnaya)[:razryad+dotpos])+1/10**razryad
    else:
        newdrobnaya = float(str(drobnaya)[:razryad + dotpos])
    return newdrobnaya
chislo = float(input('Введите любое дробное число через точку '))
razryad = int(input('Введите число разрядов после округления '))
celaya = int(chislo)
drobnaya = chislo % 1
newChislo = celaya+okrugleniye(drobnaya,razryad)
print(newChislo)
print("Задача №1 закончена")
print(' ')

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

print("Задача №2")
def proverkabyleta(No):
    part1 = (No[0:3])
    part2 = (No[3:6])
    s1 = 0
    s2 = 0
    for c1 in part1:
        s1 += int(c1)
    for c2 in part2:
        s2 += int(c2)
    if s1 == s2:
        return True
    else:
        return False
byletNo = input('Введите № билета ')
if True == (proverkabyleta(byletNo)) :
    print('Счастливый билет')
else :
    print('несвезло')
print("Задача №2 закончена")




