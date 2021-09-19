# 1.Создайте и выполните функцию с блоком try - except обрабатывающим попытку распечатать несуществующую переменную.
# 2.Создайте и выполните функцию перевода списка строк в список целых чисел с блоком try - except, обрабатывающим ошибки преобразования. В случае ошибки выводить сообщение на экран и не добавлять новый элемент в итоговый список.
# 3.Создайте и выполните функцию с блоком try - except - finally, обрабатывающим попытку записать строку в файл, открытый на чтение. В блоке finally выполнить закрытие файла.
def process_data():    
        try:
            print(x)
        except NameError:
            print("Переменная x не определена")
def process_data2(inputs):
    for my_input in inputs:
        try:
            my_num = int(my_input)
            print(my_num, end=', ')
        except:
            print('не число', end=', ')
def process_data3():
    try:
        f = open("demofile.txt")
        f.write("Привет!")
    except:
        print("Ошибка при записи в файл!")
    finally:
        f.close()
def main():
    process_data()
    numbers = ['Hello', 'World', 'Work', 'Goodbye']
    print(" ")
    process_data2(numbers)
    print(" ")
    print(" ")
    process_data3()
    return 0

if __name__ == '__main__':
	main()

