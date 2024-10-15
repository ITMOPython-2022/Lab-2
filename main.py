from csv import reader


output = open('result.txt', 'w')

while True:
    flag = 0
    search = input('Введите запрос: ')
    if search == '0':
        break
    with open('civic.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            lower_case = row[2].lower()
            index = lower_case.find(search.lower())
            if index != -1:
                print(row[2])
                output.write(f'{row[2]}. Цена {row[8]} руб. S/n {row[18]}\n')
                flag += 1



        if flag == 0:
            print('Ничего не найдено.')
        else:
            print(f'Найдено {flag} результатов.')

output.close()