import csv
import pokemonDict
import movesReader
import battle

poke = pokemonDict.pokeDict()
moveDict = movesReader.import_moves()
pokeFight = pokemonDict.pokeFightDict(moveDict)

winners, losers, hp_remaining = battle.championship()

getMovesRanked = pokemonDict.getMovesRanked(moveDict)
topMoveDict = pokemonDict.topMoveDict(moveDict, pokeFight)


with open('insertPokemon.SQL', 'w', newline='') as f: 
    
    for k in range(len(poke)):
        i = k+1
        f.write("insert into pokemons (poke_dex, pokemon, type1, type2, hp, attack, defense, sp_att, sp_def, speed) values ({}, '{}', '{}', '{}', {}, {}, {}, {}, {}, {});\n".format(i, poke[i]['name'], poke[i]['type1'], poke[i]['type2'], poke[i]['hp'], poke[i]['attack'], poke[i]['defense'], poke[i]['sp_att'], poke[i]['sp_def'], poke[i]['speed']))
    
    for k in range(len(pokeFight)):
        i = k+1
        f.write("insert into pokeagainst (poke_dex, pokemon, Bug, Dark, Dragon, Electric, Fairy, Fire, Flying, Ghost, Grass, Ground, Ice, Normal, Poison, Psychic, Rock, Steel, Water) values ({}, '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});\n".format(i, pokeFight[i]['name'], pokeFight[i]['Bug'], pokeFight[i]['Dark'], pokeFight[i]['Dragon'], pokeFight[i]['Electric'], pokeFight[i]['Fairy'], pokeFight[i]['Fire'], pokeFight[i]['Flying'], pokeFight[i]['Ghost'], pokeFight[i]['Grass'], pokeFight[i]['Ground'], pokeFight[i]['Ice'], pokeFight[i]['Normal'], pokeFight[i]['Poison'], pokeFight[i]['Psychic'], pokeFight[i]['Rock'], pokeFight[i]['Steel'], pokeFight[i]['Water']))
    
    i = 0
    for k in moveDict:
        f.write("insert into moves (id, move, type, category, pp, power, acc) values ({}, '{}', '{}', '{}', {}, {}, {});\n".format(i, k, moveDict[k]['type'], moveDict[k]['category'], moveDict[k]['pp'], moveDict[k]['power'], moveDict[k]['acc']))
        i += 1
    '''
    for i in range(len(winners)):
        f.write("insert into topdawg (winners, losers, hp_remain) values ('{}', '{}', {});\n".format(winners[i], losers[i], hp_remaining[i])
    '''
    for i in 

    