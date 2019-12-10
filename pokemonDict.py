def pokeDict():
    import csv
    f = open('pokemon.csv')
    dreader = csv.DictReader(f, delimiter=',')
    gen1 = 0
    pokeData = []
    for i in dreader:
        pokeData.append(i)
        if gen1 == 167:
            break
        gen1 += 1

    f.close()
    #,Name,Type 1,Type 2,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
    name_list = []
    for i in pokeData:
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
    for i in pokeData:
        name = i['Name']
        if 'Mega' not in name:
            tempName = i['Name']
            tempID = pokeID
            tempType1 = i['Type 1']
            tempType2 = i['Type 2']
            tempHP = float(i['HP'])
            tempAtt = float(i['Attack'])
            tempDef = float(i['Defense'])
            tempSpAtt = float(i['Sp. Atk'])
            tempSpDef = float(i['Sp. Def'])
            tempSpeed = float(i['Speed'])
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

def pokeFightDict():
    import csv
    import re
    f = open('pokemon-2.csv')
    dreader = csv.DictReader(f, delimiter=',')
    pokeFightData = []
    gen1 = 1
    for i in dreader:
        pokeFightData.append(i)
        gen1 += 1
        if gen1 == 151:
            break
    f.close()

    name2_list = []
    for i in pokeFightData:
        name = i['name']
        name2_list.append(name)
    #abilities,against_bug,against_dark,against_dragon,against_electric,against_fairy,against_fight,against_fire,against_flying,
    # against_ghost,against_grass,against_ground,against_ice,against_normal,against_poison,against_psychic,against_rock,against_steel,
    # against_water,attack,base_egg_steps,base_happiness,base_total,capture_rate,classfication,defense,experience_growth,height_m,hp,
    # japanese_name,name,percentage_male,pokedex_number,sp_attack,sp_defense,speed,type1,type2,weight_kg,generation,is_legendary

    pokeFightDict = {}
    for p in name2_list:
        pokeFightDict[p] = {'id': 0,
                    'against_bug': 0,
                    'against_dark': 0,
                    'against_dragon': 0,
                    'against_electric': 0,
                    'against_fairy': 0,
                    'against_fight': 0,
                    'against_fire': 0,
                    'against_flying': 0,
                    'against_ghost': 0,
                    'against_grass': 0,
                    'against_ground': 0,
                    'against_ice': 0,
                    'against_normal': 0,
                    'against_poison': 0,
                    'against_psychic': 0,
                    'against_rock': 0,
                    'against_steel': 0,
                    'against_water': 0,
                    'moves': []}

    for i in pokeFightData:
        tempName = i['name']
        pokeFightDict[tempName]['id'] = float(i['pokedex_number'])
        pokeFightDict[tempName]['against_bug'] = float(i['against_bug'])
        pokeFightDict[tempName]['against_dark'] = float(i['against_dark'])
        pokeFightDict[tempName]['against_dragon'] = float(i['against_dragon'])
        pokeFightDict[tempName]['against_electric'] = float(i['against_electric'])
        pokeFightDict[tempName]['against_fairy'] = float(i['against_fairy'])
        pokeFightDict[tempName]['against_fight'] = float(i['against_fight'])
        pokeFightDict[tempName]['against_fire'] = float(i['against_fire'])
        pokeFightDict[tempName]['against_flying'] = float(i['against_flying'])
        pokeFightDict[tempName]['against_ghost'] = float(i['against_ghost'])
        pokeFightDict[tempName]['against_grass'] = float(i['against_grass'])
        pokeFightDict[tempName]['against_ground'] = float(i['against_ground'])
        pokeFightDict[tempName]['against_ice'] = float(i['against_ice'])
        pokeFightDict[tempName]['against_normal'] = float(i['against_normal'])
        pokeFightDict[tempName]['against_poison'] = float(i['against_poison'])
        pokeFightDict[tempName]['against_psychic'] = float(i['against_psychic'])
        pokeFightDict[tempName]['against_rock'] = float(i['against_rock'])
        pokeFightDict[tempName]['against_steel'] = float(i['against_steel'])
        pokeFightDict[tempName]['against_water'] = float(i['against_water'])
        
    f = open('pokemon-data.csv')
    dreader = csv.DictReader(f, delimiter=';')
    pokeMovesData = []
    for i in dreader:
        pokeMovesData.append(i)
    f.close()

    
    for i in pokeMovesData:
        tempName = i['Name']
        if tempName in name2_list:
            moves = i['Moves'][1:len(i['Moves'])-1]
            tempSpl = moves.split(', ')
            for move in tempSpl:
                l = len(move) - 1
                move = move[1:l]
                pokeFightDict[tempName]['moves'].append(move)
        
            """
            for k in movesTemp:
                pokeFightDict[tempName]['moves'].add(k)
                #pokeFightDict[tempName]['moves'] = i['Moves']
             """
    return pokeFightDict