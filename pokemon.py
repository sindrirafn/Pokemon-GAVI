import csv
import pokemonDict

f = open('pokemon.csv')
dreader = csv.DictReader(f, delimiter=',')
gen1 = 0
pokeData = []
for i in dreader:
    pokeData.append(i)
    if gen1 == 167:
        break
    gen1 += 1

f.close()

poke = pokemonDict.pokeDict(pokeData)