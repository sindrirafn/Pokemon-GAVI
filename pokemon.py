import csv
import pokemonDict
import movesReader

poke = pokemonDict.pokeDict()

moveDict = movesReader.import_moves()

print(poke['Pikachu'])