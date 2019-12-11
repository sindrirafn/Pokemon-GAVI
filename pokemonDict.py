import movesReader
import csv
import re
from collections import Counter

def pokeDict():
    f = open('PokemonReal.csv')
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
        pokeDict[i+1] = {'name': row.get('Name').replace("'",''),
                    'type1': row['Type 1'],
                    'type2': row['Type 2'],
                    'hp': float(row['HP']),
                    'attack': float(row['Attack']),
                    'defense': float(row['Defense']),
                    'sp_att': float(row['Sp. Atk']),
                    'sp_def': float(row['Sp. Def']),
                    'speed': float(row['Speed']),
                    'legendary': row['Legendary']}

    pokeDict[29]['name'] = 'Nidoran-F'
    pokeDict[32]['name'] = 'Nidoran-M'
    
    return pokeDict

# ----------------------------




def pokeFightDict(movesGen1):
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
        name_list.append(i.get('name').replace("'",''))

    #abilities,against_bug,against_dark,against_dragon,against_electric,against_fairy,against_fight,against_fire,against_flying,
    # against_ghost,against_grass,against_ground,against_ice,against_normal,against_poison,against_psychic,against_rock,against_steel,
    # against_water,attack,base_egg_steps,base_happiness,base_total,capture_rate,classfication,defense,experience_growth,height_m,hp,
    # japanese_name,name,percentage_male,pokedex_number,sp_attack,sp_defense,speed,type1,type2,weight_kg,generation,is_legendary

    pokeFightDict = {}

    for i in pokeFightData:
        pokeFightDict[int(i['pokedex_number'])] = {'name' : i['name'].replace("'",''),
                    'Bug' : float(i['against_bug']),
                    'Dark' : float(i['against_dark']),
                    'Dragon' : float(i['against_dragon']),
                    'Electric' : float(i['against_electric']),
                    'Fairy' : float(i['against_fairy']),
                    'Fighting' : float(i['against_fight']),
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
                    '' : 1.0,
                    'moves': []}

    pokeFightDict[29]['name'] = 'Nidoran-F'
    pokeFightDict[32]['name'] = 'Nidoran-M'
    
    f = open('pokemon-data.csv')
    dreader = csv.DictReader(f, delimiter=';')
    pokeMovesData = []
    for i in dreader:
        pokeMovesData.append(i)
    f.close()
    
    moves = []
    #movesGen1 = movesReader.import_moves()
    for i in pokeMovesData:
        name = i.get('Name').replace("'",'')
        for j in range(len(pokeFightDict)):
            if pokeFightDict[j+1].get('name') == name:
                moves = i['Moves'][1:len(i['Moves'])-1].split(', ')
                for move in moves:
                    l = len(move) - 1
                    move_trimmed = move[1:l].replace("'",'')
                    if move_trimmed in movesGen1:
                        pokeFightDict[j+1]['moves'].append(move_trimmed)
                pokeFightDict[j+1]['moves']=list(set(pokeFightDict[j+1]['moves']))
    
    return pokeFightDict


def getMovesRanked(moves):
    power = []; names = []
    for i in moves:
        names.append(i)
        power.append(moves[i].get('power')*moves[i].get('acc')/100)
    comb = list(zip(power,names))
    comb.sort(reverse=1)
    moves_ranked = []
    for i in comb:
        moves_ranked.append(i[1])
    moves_ranked.remove('SelfDestruct')
    moves_ranked.remove('Explosion')
    return moves_ranked

def topMoveDict(ranked_moves, pokeFight):
    topMoveDict = {}
    for i in pokeFight:
        top_moves=[]
        move_count = 0
        for move in ranked_moves:
            if move in pokeFight[i].get('moves'):
                top_moves.append(move)
                move_count += 1
            if move_count == 3:
                break
        topMoveDict[i] = {
            'name': pokeFight[i].get('name'),
            'top_moves': top_moves
        }

    return topMoveDict
