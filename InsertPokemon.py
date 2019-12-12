import csv
import pokemonDict
import movesReader
import battle

poke = pokemonDict.pokeDict()
moveDict = movesReader.import_moves()
pokeFight = pokemonDict.pokeFightDict(moveDict)



getMovesRanked = pokemonDict.getMovesRanked(moveDict)
topMoveDict = pokemonDict.topMoveDict(moveDict, pokeFight)

winners, losers, hp_remaining = battle.championshipRankingAvg(20)



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
    for i in range(len(winners)):
        f.write("insert into topdawg (id, winners, losers, hp_remaining) values ({}, '{}', '{}', {});\n".format(i+1, winners[i], losers[i], hp_remaining[i]))
    
    for k in range(len(topMoveDict)):
        j = k+1
        f.write("insert into topmoves (pokemon, best, second, third) values ('{}'".format(topMoveDict[j]['name']))
        for i in range(len(topMoveDict[j]['top_moves'])):
            f.write(", '{}'".format(topMoveDict[j]['top_moves'][i]))
        fixer = 3 - len(topMoveDict[j]['top_moves'])   #herna er eg ad sja til thess ad pokemons sem eru med faerri en 3 spells, fylli uppi tofluna.
        for a in range(fixer):
            f.write(", '{}'".format(topMoveDict[j]['top_moves'][0]))
        f.write(");\n")

    