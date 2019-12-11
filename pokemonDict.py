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
                    'bug' : float(i['against_bug']),
                    'dark' : float(i['against_dark']),
                    'dragon' : float(i['against_dragon']),
                    'electric' : float(i['against_electric']),
                    'fairy' : float(i['against_fairy']),
                    'fight' : float(i['against_fight']),
                    'fire' : float(i['against_fire']),
                    'flying' : float(i['against_flying']),
                    'ghost' : float(i['against_ghost']),
                    'grass' : float(i['against_grass']),
                    'ground' : float(i['against_ground']),
                    'ice' : float(i['against_ice']),
                    'normal' : float(i['against_normal']),
                    'poison' : float(i['against_poison']),
                    'psychic' : float(i['against_psychic']),
                    'rock' : float(i['against_rock']),
                    'steel' : float(i['against_steel']),
                    'water' : float(i['against_water']),
                    'moves': []}



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