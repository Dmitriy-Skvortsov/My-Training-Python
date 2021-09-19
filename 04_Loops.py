# 1.Напишите код печати чисел от 10 до 20.
# 2.Напишите код печати только делящихся на 3 чисел с использованием continue.
# 3.Напишите код поиска в списке первого элемента, меньшего 1, с использованием break и else.

i = 10
while i <= 20:
    print(i, end=' ')
    i += 1
print("")
print("")
for i in range(20):
    if i%3 != 0:
        continue
    print(i, end=' ')
print("")
print("")

numbers = [1,3,4,8,12,18,20]
for number in numbers:
    if number <1:
        print(number)
        break
else:
    print("Элемент не найден")
    
