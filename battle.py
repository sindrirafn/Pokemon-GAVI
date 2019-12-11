import pokemonDict
import movesReader
import random
from collections import Counter


moves = movesReader.import_moves()
pokeInfo = pokemonDict.pokeDict()
pokeFight = pokemonDict.pokeFightDict(moves)
topMoves = pokemonDict.topMoveDict(moves, pokeFight)

def accuracy(accuracy):
    return(random.randint(1,100)<accuracy)



def battle(A, B):

    if pokeInfo.get(A)['speed'] > pokeInfo.get(B)['speed']:
        fighterA = pokeInfo.get(A); fighterB = pokeInfo.get(B)
        movesA = pokeFight.get(A); movesB = pokeFight.get(B)
    else:
        fighterA = pokeInfo.get(B); fighterB = pokeInfo.get(A)
        movesA = pokeFight.get(B); movesB = pokeFight.get(A)

    attackA = fighterA.get('attack'); attackB = fighterB.get('attack')
    defenceA = fighterA.get('defense'); defenceB = fighterB.get('defense')
    hpA = fighterA.get('hp'); hpB = fighterB.get('hp')
    pick = random.randint(0,len(topMoves[A].get('top_moves'))-1)
    moveA = topMoves[A].get('top_moves')[pick] 
    pick = random.randint(0,len(topMoves[B].get('top_moves'))-1)
    moveB = topMoves[B].get('top_moves')[pick]
 
    attPowA =  moves[moveA].get('power'); attPowB =  moves[moveB].get('power')
                         
    modA = movesB.get(fighterA.get('type1')) * movesB.get(fighterA.get('type2'))
    if modA == 0.0:
        modA = 0.25
    dmgA = round(((((2/5 + 2)*attPowA*attackA/defenceB) / 50) + 2) * modA)
    
    modB = movesA.get(fighterB.get('type1')) * movesA.get(fighterB.get('type2'))
    if modB == 0.0:
        modB = 0.25
    dmgB = round(((((2/5 + 2)*attPowB*attackB/defenceA) / 50) + 2) * modB)



    while hpA > 0 and hpB > 0:
        # Fighter 1 turn
        if accuracy(moves[moveA].get('acc')):
            hpB -= dmgA
            if hpB <= 0:
                break

        # Fighter 2 turn
        if accuracy(moves[moveB].get('acc')):
            hpA -= dmgB

    if hpA <= 0:
        #print(fighterB.get('name'), 'wins with ', hpB, "HP remaining!")
        #print(fighterA.get('name'), 'loses')
        return fighterB.get('name'), fighterA.get('name'), hpB
    elif hpB <= 0:
        #print(fighterA.get('name'), 'wins with ', hpA, "HP remaining!")
        #print(fighterB.get('name'), 'loses')
        return fighterA.get('name'), fighterB.get('name'), hpA


def championship():
    winners = []; losers=[]
    hp_remaining = []
    for i in range(1,len(pokeInfo)):
        for j in range(i+1,len(pokeInfo)+1):
            winner, loser, hp = battle(i,j)
            winners.append(winner)
            losers.append(loser)
            hp_remaining.append(hp)
    return winners, losers, hp_remaining


winners, losers, hp_remaining = championship()
for i in range(len(winners)):
    print(winners[i], losers[i], hp_remaining[i])
