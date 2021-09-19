# 1.Создайте и распечатайте массив в NumPy.
# 2.Создайте и распечатайте массив в Pandas.
import numpy as np
import pandas as db

def my_numpy():
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
    print(type(arr))

def my_pandas():
    a = [1, 2, 3, 4, 5]
    myvar = db.Series(a)
    print(myvar)
    print(" ")
    print(myvar[1])

def main():
    my_numpy()
    print(" ")
    my_pandas()    
    return 0

if __name__ == '__main__':
	main()

