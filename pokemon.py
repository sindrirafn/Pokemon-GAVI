import csv
import pokemonDict
import movesReader

poke = pokemonDict.pokeDict()
moveDict = movesReader.import_moves()
pokeFight = pokemonDict.pokeFightDict(moveDict)



print(poke['Pikachu'])
print(pokeFight['Pikachu']['moves'][42])
