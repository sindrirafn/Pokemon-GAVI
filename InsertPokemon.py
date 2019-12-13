import csv
import pokemonDict
import movesReader          # importa odrum skram sem innihalda functions sem setja upp mismunandi dict eda herma bardaga.
import battle

#poke = pokemonDict.pokeDict()
moveDict = movesReader.import_moves()
poke = pokemonDict.pokeDict(moveDict)                   #herna erum vid ad skyra foll til einfalda skrift.
getMovesRanked = pokemonDict.getMovesRanked(moveDict)
topMoveDict = pokemonDict.topMoveDict(moveDict, poke)
tournDict = battle.tournamentRankingDict(20)            # gerum 20 itranir af utslattarkeppninni.
winners, losers, hp_remaining = battle.championshipRankingAvg(20)   # 20 itranir af allir keppa vid alla.



with open('insertPokemon.SQL', 'w', newline='') as f: 
    
    for k in range(len(poke)):
        i = k+1
        f.write("insert into pokemons (poke_dex, pokemon, type1, type2, hp, attack, defense, sp_att, sp_def, speed) values ({}, '{}', '{}', '{}', {}, {}, {}, {}, {}, {});\n".format(i, poke[i]['name'], poke[i]['type1'], poke[i]['type2'], poke[i]['hp'], poke[i]['attack'], poke[i]['defense'], poke[i]['sp_att'], poke[i]['sp_def'], poke[i]['speed']))
    
    for k in range(len(poke)):
        i = k+1
        f.write("insert into pokeagainst (poke_dex, pokemon, Bug, Dark, Dragon, Electric, Fairy, Fire, Flying, Ghost, Grass, Ground, Ice, Normal, Poison, Psychic, Rock, Steel, Water) values ({}, '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});\n".format(i, poke[i]['name'], poke[i]['bug'], poke[i]['dark'], poke[i]['dragon'], poke[i]['electric'], poke[i]['fairy'], poke[i]['fire'], poke[i]['flying'], poke[i]['ghost'], poke[i]['grass'], poke[i]['ground'], poke[i]['ice'], poke[i]['normal'], poke[i]['poison'], poke[i]['psychic'], poke[i]['rock'], poke[i]['steel'], poke[i]['water']))
    
    for k in moveDict:
        f.write("insert into moves (id, move, type, category, pp, power, acc) values ({}, '{}', '{}', '{}', {}, {}, {});\n".format(i, k, moveDict[k]['type'], moveDict[k]['category'], moveDict[k]['pp'], moveDict[k]['power'], moveDict[k]['acc']))
        i += 1

    for i in range(len(winners)):
        f.write("insert into champ (id, winners, losers, hp_remaining) values ({}, '{}', '{}', {});\n".format(i+1, winners[i], losers[i], hp_remaining[i]))
    
    for k in range(len(topMoveDict)):
        j = k+1
        f.write("insert into bestmoves (pokemon, best, second, third) values ('{}'".format(topMoveDict[j]['name']))
        for i in range(len(topMoveDict[j]['top_moves'])):
            f.write(", '{}'".format(topMoveDict[j]['top_moves'][i]))
        fixer = 3 - len(topMoveDict[j]['top_moves'])   # herna er eg ad sja til thess ad pokemons sem eru med faerri en 3 'bestMoves', fylli uppi tofluna.
        for a in range(fixer):
            f.write(", '{}'".format(topMoveDict[j]['top_moves'][0]))    # thar sem vid erum ekki ad gera neitt med best moves i SQL that leyfdum vid okkur
        f.write(");\n")                                                 # ad endurtaka sama move til ad fylla i toflur.

    for k in range(len(tournDict)):
        f.write("insert into tourney (id, pokemon, points) values ({}, '{}', {});\n".format(k+1, tournDict[k+1]['name'], tournDict[k+1]['points']))
    