import csv

flag = 0
search = input('Search for: ')
f = open('result.txt','w')
with open('civic.csv','r') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')
    for row in table:
        #if (int(row[8]) >= 7000):
            # print(row[2], ' ', row[8])
        lower_case = row[2].lower()
        index = lower_case.find(search.lower())
        if (index != -1):
            print(len(row[2]))

            #row[8].replace(',','.')

            flag = 1
            f.write(row[0] + ' ' + row[2] + ' Стоимость: ' + row[8] + ' рублей.\n')

    if (flag == 0):
        print("Nothing found.")

f.close()
