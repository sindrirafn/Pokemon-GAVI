import csv
import pokemonDict
import movesReader

poke = pokemonDict.pokeDict()

pokeFight = pokemonDict.pokeFightDict()

moveDict = movesReader.import_moves()


with open('insertPokemon.SQL', 'w', newline='') as f: 
    '''
    for k in range(len(poke)):
        i = k+1
        f.write('insert into pokemon (id, pokemon, type1, type2, hp, attack, defense, sp_att, sp_def, speed, legendary) values ({}, "{}", "{}", "{}", {}, {}, {}, {}, {}, {}, "{}");\n'.format(i, poke[i]['name'], poke[i]['type1'], poke[i]['type2'], poke[i]['hp'], poke[i]['attack'], poke[i]['defense'], poke[i]['sp_att'], poke[i]['sp_def'], poke[i]['speed'], poke[i]['legendary']))
    
    for k in range(len(poke)):
        i = k+1
        f.write("insert into pokemon (id, pokemon, type1, type2, hp, attack, defense, sp_att, sp_def, speed, legendary) values ({}, '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, '{}');\n".format(i, poke[i]['name'], poke[i]['type1'], poke[i]['type2'], poke[i]['hp'], poke[i]['attack'], poke[i]['defense'], poke[i]['sp_att'], poke[i]['sp_def'], poke[i]['speed'], poke[i]['legendary']))
    '''
    
    for k in range(len(pokeFight)):
        i = k+1
        f.write("insert into pokeMoves (id, pokemon, Bug, Dark, Dragon, Electric, Fairy, Fire, Flying, Ghost, Grass, Ground, Ice, Normal, Poison, Psychic, Rock, Steel, Water, Moves) values ({}, '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}');\n".format(i, pokeFight[i]['name'], pokeFight[i]['Bug'], pokeFight[i]['Dark'], pokeFight[i]['Dragon'], pokeFight[i]['Electric'], pokeFight[i]['Fairy'], pokeFight[i]['Fire'], pokeFight[i]['Flying'], pokeFight[i]['Ghost'], pokeFight[i]['Grass'], pokeFight[i]['Ground'], pokeFight[i]['Ice'], pokeFight[i]['Normal'], pokeFight[i]['Poison'], pokeFight[i]['Psychic'], pokeFight[i]['Rock'], pokeFight[i]['Steel'], pokeFight[i]['Water'], list(pokeFight[i]['moves'])))
    
    for k in range(len(pokeFight)):
        i = k+1
        f.write('insert into pokeMoves (id, pokemon, Bug, Dark, Dragon, Electric, Fairy, Fire, Flying, Ghost, Grass, Ground, Ice, Normal, Poison, Psychic, Rock, Steel, Water, Moves) values ({}, "{}", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, "{}");\n'.format(i, pokeFight[i]['name'], pokeFight[i]['Bug'], pokeFight[i]['Dark'], pokeFight[i]['Dragon'], pokeFight[i]['Electric'], pokeFight[i]['Fairy'], pokeFight[i]['Fire'], pokeFight[i]['Flying'], pokeFight[i]['Ghost'], pokeFight[i]['Grass'], pokeFight[i]['Ground'], pokeFight[i]['Ice'], pokeFight[i]['Normal'], pokeFight[i]['Poison'], pokeFight[i]['Psychic'], pokeFight[i]['Rock'], pokeFight[i]['Steel'], pokeFight[i]['Water'], pokeFight[i]['moves']))

    '''
    i = 1
    for k in moveDict:
        f.write("insert into moves (id, type, category, pp, power, acc) values ({}, '{}', '{}', {}, {}, {});\n".format(i, moveDict[k]['type'], moveDict[k]['category'], moveDict[k]['pp'], moveDict[k]['power'], moveDict[k]['acc']))
        i += 1
    '''

    

    