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



#print(poke['Pikachu'])
#print(pokeFight['Pikachu']['moves'][42])
