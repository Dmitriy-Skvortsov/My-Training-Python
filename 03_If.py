# 1.Напишите код печати результата сравнения двух целочисленных переменных.
# 2.Напишите код определения делимости числа на 3.
# 3.Создайте две логические переменные. Напишите код, распечатывающий, сколько переменных имеют значение False: обе, одна или ни одной.

g = 33
s = 24

if g == s:
    print("Переменные равны")
elif g < s:
    print("g меньше s")
elif g > s:
    print("g больше s")
else:
    print("Не должно быть напечатано")
print("")
if g%3 == 0:
    print("g не чётное число")
else:
    print("g чётное число")
print("")    
g = False
s = False

if g and s:
    print("g и s")
elif g or s:
    print("Один из g или s")
else:
    print("Ничего")


