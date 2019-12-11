import pokemonDict
import movesReader

#def pokeBattle(pokemon1_id, pokemon2_id):
pokeInfo = pokemonDict.pokeDict()
pokeFight = pokemonDict.pokeFightDict()
moves = movesReader.import_moves()

fighterA = pokeInfo.get(1)
fighterB = pokeInfo.get(4)

movesA = pokeFight.get(1)
movesB = pokeFight.get(4)

level = 1
attack = fighterA.get('attack')
attPow = 40 
defence = fighterB.get('defense')
mod = movesB.get(fighterA.get('type1')) * movesB.get(fighterA.get('type2'))
dmg = ((((2*level/5 + 2)*attPow*attack/defence) / 50) + 2) * mod

print(pokeFight[1])


'''
((2A/5+2)*B*C)/D)/50)+2)*X)*Y/10)*Z)/255

A = attacker's Level
B = attacker's Attack or Special
C = attack Power
D = defender's Defense or Special
X = same-Type attack bonus (1 or 1.5)
Y = Type modifiers (40, 20, 10, 5, 2.5, or 0)
Z = a random number between 217 and 255
'''