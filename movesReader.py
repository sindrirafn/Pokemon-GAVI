#fall sem les inn move-data.csv

def import_moves():
    import csv
    moves = open('move-data.csv')
    reader = csv.DictReader(moves, delimiter = ',')
    data = []
    for row in reader:
        data.append(row)
    moves.close()
    moveDict = {}
    for row in data:
        if int(row['Generation']) == 1:
            moveDict[row['Name'].replace('-','')] = {'ID': 0, 'type': '', 'category': '', 'pp': 0, 'power':0,'acc': 0,}

    cnt = 0                                                     # indexa oll moves og byrja i 0

    for row in data:
        if int(row['Generation']) == 1:                         # tek bara generation 1
            moveDict[row['Name'].replace('-','')]['ID'] = cnt
            moveDict[row['Name'].replace('-','')]['type'] = row['Type']
            moveDict[row['Name'].replace('-','')]['category'] = row['Category']
            moveDict[row['Name'].replace('-','')]['pp'] = int(row['PP'])
            if row['Power'] == 'None':
                moveDict[row['Name'].replace('-','')]['power'] = 100
            else:
                moveDict[row['Name'].replace('-','')]['power'] = int(row['Power'])
            if row['Accuracy'] == 'None':
                moveDict[row['Name'].replace('-','')]['acc'] = 100
            else:
                moveDict[row['Name'].replace('-','')]['acc'] = int(row['Accuracy'])
            cnt += 1
    return(moveDict)

