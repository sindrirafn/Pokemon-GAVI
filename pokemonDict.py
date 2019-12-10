def pokeDict(data):
    #,Name,Type 1,Type 2,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
    name_list = []
    for i in data:
        name = i['Name']
        if 'Mega' not in name:
            name_list.append(name)

    pokeDict = {}
    for p in name_list:
        pokeDict[p] = {'id': 0,
                    'type1': [],
                    'type2': [],
                    'hp': 0,
                    'attack': 0,
                    'defense': 0,
                    'sp_att': 0,
                    'sp_def': 0,
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
            pokeDict[tempName]['sp_att'] = tempSpAtt
            pokeDict[tempName]['sp_def'] = tempSpDef
            pokeDict[tempName]['speed'] = tempSpeed
            pokeDict[tempName]['legendary'] = tempLeg
            pokeID += 1
            return pokeDict

            #penis