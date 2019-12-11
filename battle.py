import pokemonDict
import movesReader

pokeInfo = pokemonDict.pokeDict()
pokeFight = pokemonDict.pokeFightDict()
moves = movesReader.import_moves()

fighterA = pokeInfo.get(3)
fighterB = pokeInfo.get(6)

statsA = pokeFight.get(3)
print(fighterA)
print(fighterB)
print(statsA)