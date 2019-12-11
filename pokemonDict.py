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
                    'Bug' : float(i['against_bug']),
                    'Dark' : float(i['against_dark']),
                    'Dragon' : float(i['against_dragon']),
                    'Electric' : float(i['against_electric']),
                    'Fairy' : float(i['against_fairy']),
                    'Fight' : float(i['against_fight']),
                    'Fire' : float(i['against_fire']),
                    'Flying' : float(i['against_flying']),
                    'Ghost' : float(i['against_ghost']),
                    'Grass' : float(i['against_grass']),
                    'Ground' : float(i['against_ground']),
                    'Ice' : float(i['against_ice']),
                    'Normal' : float(i['against_normal']),
                    'Poison' : float(i['against_poison']),
                    'Psychic' : float(i['against_psychic']),
                    'Rock' : float(i['against_rock']),
                    'Steel' : float(i['against_steel']),
                    'Water' : float(i['against_water']),
                    '' : 1,
                    'moves': []}


    
    f = open('pokemon-data.csv')
    dreader = csv.DictReader(f, delimiter=';')
    pokeMovesData = []
    for i in dreader:
        pokeMovesData.append(i)
    f.close()
    
    poke_id = 1
    moves = []

    for i in pokeMovesData:
        name = i.get('Name')
        for j in range(len(pokeFightDict)):
            if pokeFightDict[j+1].get('name') == name:
                moves = i['Moves'][1:len(i['Moves'])-1].split(', ')
                for move in moves:
                    l = len(move) - 1
                    move_trimmed = move[1:l]
                    pokeFightDict[j+1]['moves'].append(move_trimmed)
                pokeFightDict[j+1]['moves']=set(pokeFightDict[j+1]['moves'])
    
    return pokeFightDict