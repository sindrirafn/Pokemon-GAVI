import csv

f = open('pokemon.csv')
dreader = csv.DictReader(f, delimiter=',')

data = []
gen1 = 0
for i in dreader:
    data.append(i)
    gen1 += 1
    if gen1 == 166:
        break

f.close()
#,Name,Type 1,Type 2,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
megaCount = 0
name_list = []
for i in data:
    name = i['Name']
    if 'Mega' not in name:
        name_list.append(name)
    else:
        megaCount += 1

pokeDict = {}
for p in name_list:
    pokeDict[p] = {'id': 0,
                'type1': [],
                'type2': [],
                'hp': 0,
                'attack': 0,
                'defense': 0,
                'sp att': 0,
                'sp def': 0,
                'speed': 0,
                'legendary': False}

pokeID = 1
for i in data:
    name = i['Name']
    if 'Mega' not in name:
        tempName = i['Name']
        tempID = pokeID
        tempType1 = i['Type 1']
        tempType2 = i['Type 2']
        tempHP = int(i['HP'])
        tempAtt = int(i['Attack'])
        tempDef = int(i['Defense'])
        tempSpAtt = int(i['Sp. Atk'])
        tempSpDef = int(i['Sp. Def'])
        tempSpeed = int(i['Speed'])
        tempLeg = i['Legendary']
        pokeDict[tempName]['id'] = tempID
        pokeDict[tempName]['type1'] = tempType1
        pokeDict[tempName]['type2'] = tempType2
        pokeDict[tempName]['hp'] = tempHP
        pokeDict[tempName]['attack'] = tempAtt
        pokeDict[tempName]['defense'] = tempDef
        pokeDict[tempName]['sp att'] = tempSpAtt
        pokeDict[tempName]['sp def'] = tempSpDef
        pokeDict[tempName]['speed'] = tempSpeed
        pokeDict[tempName]['legendary'] = tempLeg
        pokeID += 1

