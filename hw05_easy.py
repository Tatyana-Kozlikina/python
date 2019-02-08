# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
for i in range(1, 10):
    os.mkdir(os.path.join(os.getcwd(),'dir_'+str(i)))
input('Удаляем ?')
for i in range(1, 10):
    os.rmdir(os.path.join(os.getcwd(),'dir_'+str(i)))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!
import os
print( [f for f in os.listdir(os.getcwd()) if os.path.isdir(f)])


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS
import os
cmd = 'copy '+ str(os.path.split( __file__)[1])+ ' cpy_'+str(os.path.split( __file__)[1])
print(cmd)
os.system(cmd)