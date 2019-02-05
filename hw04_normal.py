# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
print ('Задание №1')
import string,random
randcharsstr = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
print(randcharsstr)
tmpstr = ''
tmplist = []
for i in randcharsstr:
    if i.islower():
        tmpstr += i
    if i.isupper() and tmpstr != '':
        tmplist.append(tmpstr)
        tmpstr = ''
if tmpstr != '':
    tmplist.append(tmpstr)
print("Способ №1", tmplist)
import re
tmplist2 = re.findall(r'[a-z]+', randcharsstr)
print("Способ №2", tmplist2)
print ('Задание №1 закончено \n')

# Задание-2:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
print ('Задание №2')
import random
s = ''
for i in range(2500):
    s += str(random.randint(0, 9))
f = open('text.txt', 'w')
f.write(s)
f.close()
print(s, '\n')
f = open('text.txt', 'r')
c = [0, 0]
l = [s[0], s[0]]
for i in s:
    if i == l[1]:
        c[1] += 1
        if c[1] > c[0]:
            c[0] = c[1]
            l[0] = l[1]
    else:
        c[1] = 1
        l[1] = i
print(l[0]*c[0])
f.close()
print ('Задание №2 закончено \n')