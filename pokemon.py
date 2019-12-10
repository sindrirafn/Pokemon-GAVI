import csv
import pokemonDict
import movesReader

poke = pokemonDict.pokeDict()

pokeFight = pokemonDict.pokeFightDict()

moveDict = movesReader.import_moves()

print(poke['Pikachu'])
print(pokeFight['Pikachu']['moves'][42])
