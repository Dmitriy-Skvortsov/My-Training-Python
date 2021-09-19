# 1.С помощью Python прочитайте содержимое прилагаемого файла 10_file_in.txt.
# 2.Удалите лишние вхождения слова “Счет” во второй колонке и запишите данные в файл 10_file_out.txt.
# 3.С помощью Pandas прочитайте содержимое прилагаемого файла 10_Invoices.csv.
# 4.Удалите лишние вхождения словосочетания “Сделка по заявке ” во второй колонке и запишите данные в файл 10_Invoices_out.csv.
import pandas as pd

def my_text():
    # Extract
    f = open("10_file_in.txt", "r", encoding='utf-8')
    s = f.read()
    f.close()
    print(s)
    # Transform
    s = s.replace("Счет ", "")
    print(s)
    # Load
    f = open("10_file_out.txt", "w", encoding='utf-8')
    f.write(s)
    f.close()
    
def my_pandas_csv():
    # Extract
    df = pd.read_csv('10_Invoices.csv', sep=';')
    print(df)
    # Transform
    cnt = df[df.columns[0]].count()
    print(cnt)
    for i in range(cnt):
        df.iat[i,1] = df.iat[i,1].replace("Сделка по заявке ", "")        
    print(df)
    # Load
    df.to_csv('10_Invoices_out.csv', sep=';', encoding='utf-8', index=False)
    

def main():
    my_text()
    my_pandas_csv()
    return 0

if __name__ == '__main__':
	main()

