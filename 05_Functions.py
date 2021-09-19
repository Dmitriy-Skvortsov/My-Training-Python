# 1.Создайте функцию печати элементов списка, делящихся на 5.
# 2.Напишите код выполнения созданной функции.
# 3.Создайте функцию простого поиска и возвращения минимального элемента в списке.
# 4.Напишите код выполнения созданной функции.
# 5.Создайте функцию поиска в списке первого элемента, меньшего my_value.
# 6.Напишите код выполнения созданной функции.
def function_list_5(numbers):
    for number in numbers:
        if number%5 != 0:
            continue
        print(number, end=' ')
    print(" ")    
numbers = [4, 10, 20, 24, 30, 36, 40, 41, 50, 55, 100, 120]
function_list_5(numbers)
print(" ")
def get_min_simpl(numbers):
    m = numbers[0]
    for number in numbers:
        if number < m:
            m = number
    return m    
numbers1 = [41, 15, 28, 45, 8, 21, 89, 102]
numbers2 = [27, 9, 18, 11, 3, 16, 7, 5, 14]
my_min = get_min_simpl(numbers1)
print(my_min)
my_min = get_min_simpl(numbers2)
print(my_min)
print(" ")
def get_first_exceed(numbers, my_value):
    for number in numbers:
        if number < my_value:
            print(number)
            break
    else:
        print("Элемент не найден")        
numbers1 = [12, 32, 46, 14, 18, 98, 63, 8]
numbers2 = [95, 87, 102, 305, 64, 423, 78, 51]
get_first_exceed(numbers1, 7)
get_first_exceed(numbers2, 80)



