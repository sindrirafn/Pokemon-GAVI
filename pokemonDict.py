def pokeDict():
    import csv
    f = open('pokemon.csv')
    dreader = csv.DictReader(f, delimiter=',')
    gen1 = 1
    pokeData = []
    for i in dreader:
        pokeData.append(i)
        gen1 += 1
        if gen1 == 167:
            break


    f.close()
    #,Name,Type 1,Type 2,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary

    '''
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
            pokeDict[name]['id'] = pokeID
            pokeDict[name]['type1'] = i['Type 1']
            pokeDict[name]['type2'] = i['Type 2']
            pokeDict[name]['hp'] = float(i['HP'])
            pokeDict[name]['attack'] = float(i['Attack'])
            pokeDict[name]['defense'] = float(i['Defense'])
            pokeDict[name]['sp_att'] = float(i['Sp. Atk'])
            pokeDict[name]['sp_def'] = float(i['Sp. Def'])
            pokeDict[name]['speed'] = float(i['Speed'])
            pokeDict[name]['legendary'] = i['Legendary']
            pokeID += 1
    return pokeDict
    '''

    gen1_data = []
    for row in pokeData:
        if 'Mega' not in row['Name']:
            gen1_data.append(row)

    pokeDict = {}
    for i ,row in enumerate(gen1_data):
        pokeDict[i+1] = {'name': row['Name'],
                    'type1': row['Type 1'],
                    'type2': row['Type 2'],
                    'hp': float(row['HP']),
                    'attack': float(row['Attack']),
                    'defense': float(row['Defense']),
                    'sp_att': float(row['Sp. Atk']),
                    'sp_def': float(row['Sp. Def']),
                    'speed': float(row['Speed']),
                    'legendary': row['Legendary']}
    return pokeDict

# ----------------------------




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
        if gen1 == 152:
            break
    f.close()


    name_list = []
    for i in pokeFightData:
        name_list.append(i['name'])

    #abilities,against_bug,against_dark,against_dragon,against_electric,against_fairy,against_fight,against_fire,against_flying,
    # against_ghost,against_grass,against_ground,against_ice,against_normal,against_poison,against_psychic,against_rock,against_steel,
    # against_water,attack,base_egg_steps,base_happiness,base_total,capture_rate,classfication,defense,experience_growth,height_m,hp,
    # japanese_name,name,percentage_male,pokedex_number,sp_attack,sp_defense,speed,type1,type2,weight_kg,generation,is_legendary

    pokeFightDict = {}

    for i in pokeFightData:
        pokeFightDict[int(i['pokedex_number'])] = {'name' : i['name'],
                    'against_bug' : float(i['against_bug']),
                    'against_dark' : float(i['against_dark']),
                    'against_dragon' : float(i['against_dragon']),
                    'against_electric' : float(i['against_electric']),
                    'against_fairy' : float(i['against_fairy']),
                    'against_fight' : float(i['against_fight']),
                    'against_fire' : float(i['against_fire']),
                    'against_flying' : float(i['against_flying']),
                    'against_ghost' : float(i['against_ghost']),
                    'against_grass' : float(i['against_grass']),
                    'against_ground' : float(i['against_ground']),
                    'against_ice' : float(i['against_ice']),
                    'against_normal' : float(i['against_normal']),
                    'against_poison' : float(i['against_poison']),
                    'against_psychic' : float(i['against_psychic']),
                    'against_rock' : float(i['against_rock']),
                    'against_steel' : float(i['against_steel']),
                    'against_water' : float(i['against_water']),
                    'moves': []}



    '''
    name_list = []
    for i in pokeFightData:
        name_list.append(i['name'])

    #abilities,against_bug,against_dark,against_dragon,against_electric,against_fairy,against_fight,against_fire,against_flying,
    # against_ghost,against_grass,against_ground,against_ice,against_normal,against_poison,against_psychic,against_rock,against_steel,
    # against_water,attack,base_egg_steps,base_happiness,base_total,capture_rate,classfication,defense,experience_growth,height_m,hp,
    # japanese_name,name,percentage_male,pokedex_number,sp_attack,sp_defense,speed,type1,type2,weight_kg,generation,is_legendary

    pokeFightDict = {}

    for p in name_list:
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
        name = i['name']
        pokeFightDict[name]['id'] = float(i['pokedex_number'])
        pokeFightDict[name]['against_bug'] = float(i['against_bug'])
        pokeFightDict[name]['against_dark'] = float(i['against_dark'])
        pokeFightDict[name]['against_dragon'] = float(i['against_dragon'])
        pokeFightDict[name]['against_electric'] = float(i['against_electric'])
        pokeFightDict[name]['against_fairy'] = float(i['against_fairy'])
        pokeFightDict[name]['against_fight'] = float(i['against_fight'])
        pokeFightDict[name]['against_fire'] = float(i['against_fire'])
        pokeFightDict[name]['against_flying'] = float(i['against_flying'])
        pokeFightDict[name]['against_ghost'] = float(i['against_ghost'])
        pokeFightDict[name]['against_grass'] = float(i['against_grass'])
        pokeFightDict[name]['against_ground'] = float(i['against_ground'])
        pokeFightDict[name]['against_ice'] = float(i['against_ice'])
        pokeFightDict[name]['against_normal'] = float(i['against_normal'])
        pokeFightDict[name]['against_poison'] = float(i['against_poison'])
        pokeFightDict[name]['against_psychic'] = float(i['against_psychic'])
        pokeFightDict[name]['against_rock'] = float(i['against_rock'])
        pokeFightDict[name]['against_steel'] = float(i['against_steel'])
        pokeFightDict[name]['against_water'] = float(i['against_water'])
    '''
    f = open('pokemon-data.csv')
    dreader = csv.DictReader(f, delimiter=';')
    pokeMovesData = []
    for i in dreader:
        pokeMovesData.append(i)
    f.close()
    
    id = 1
    for i in pokeMovesData:
        name = i['Name']
        if name == pokeFightDict[id].get('name'):
            moves = i['Moves'][1:len(i['Moves'])-1].split(', ')
            for move in moves:
                l = len(move) - 1
                move = move[1:l]
                pokeFightDict[id]['moves'].append(move)
            pokeFightDict[id]['moves']=set(pokeFightDict[id]['moves'])
            id+=1
    
    return pokeFightDict