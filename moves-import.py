#fall sem les inn move-data.csv

import csv

moves = open('move-data.csv')

reader = csv.DictReader(moves, delimiter = ',')

data = []
for row in reader:
    data.append(row)
moves.close()



moveDict = {'ID': 0, 'Type': '', 'Category': '', 'pp': 0, 'power':0,'Accuracy': 0,}

cnt = 0

for row in data:
    #moveDict[row['Name']]['ID'] = cnt
    print(row['Name'])

    cnt += 1