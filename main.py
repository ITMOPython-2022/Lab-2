import csv

flag = 0
with open('civic.csv', 'r', newline='') as csvfile:
    table = csv.reader(csvfile, delimiter=';', quotechar='|')
    # print(list(table))
    for row in list(table)[3:5]:
        print(row[0])
        # for r in row[0]:
        #     print(r)
    #     #if (int(row[8]) < 7000) and (int(row[8]) > 2000):
            #print(row[0], row[8])

    '''search = input('Search: ')
    f = open('d:/itmo/python/L1/result.txt', 'w')
    for row in table:
        data = str(row[2]).lower()
        index = data.find(search.lower())
        if (index != -1):
            print(row)
            flag = 1
            f.write(row[0] + ". " + row[2] + ". Стоимость " + row[8] + " рублей.\n")

    if (flag == 0):
        print("Nothing found.")

    f.close()'''



