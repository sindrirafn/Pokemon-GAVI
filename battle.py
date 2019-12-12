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



def battle(A, B): # ATH beata mogulega inn val milli att og sp_att

    if pokeInfo.get(A)['speed'] > pokeInfo.get(B)['speed']:
        fighterA = pokeInfo.get(A); fighterB = pokeInfo.get(B)
        movesA = pokeFight.get(A); movesB = pokeFight.get(B)
        fighterA_id = A; fighterB_id = B
    else:
        fighterA = pokeInfo.get(B); fighterB = pokeInfo.get(A)
        movesA = pokeFight.get(B); movesB = pokeFight.get(A)
        fighterA_id = B; fighterB_id = A

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
        return fighterB, fighterB_id, fighterA, fighterA_id, hpB
    elif hpB <= 0:
        return fighterA, fighterA_id, fighterB, fighterB_id, hpA
    

def championship(): 
    winners = []; losers=[]
    hp_remaining = []
    for i in range(1,len(pokeInfo)):
        for j in range(i+1,len(pokeInfo)+1):
            winner, winner_id, loser, loser_id, hp = battle(i,j)
            winners.append(winner.get('name'))
            losers.append(loser.get('name'))
            hp_remaining.append(hp)
    return winners, losers, hp_remaining


def championshipRankingAvg(n):
    winners_total = []
    losers_total = []
    hp_remaining_total = []
    for i in range(n):
        winners, losers, hp_remaining = championship()
        winners_total.extend(winners)
        losers_total.extend(losers)
        hp_remaining_total.extend(hp_remaining)
        print(i)
    return winners_total, losers_total, hp_remaining_total




def round_one_draft(pokeInfo):
    brackets = []; bracket = []
    pokemon_id_list = [i for i in range(1,152)]
    picks = random.sample(pokemon_id_list,6)
    for i in range(len(picks)):
        bracket.append(picks[i]) 
        pokemon_id_list.remove(picks[i])
    brackets.append(bracket)
    while pokemon_id_list != []:
        bracket = [] 
        picks = random.sample(pokemon_id_list,5)
        for i in range(len(picks)):
            bracket.append(picks[i]) 
            pokemon_id_list.remove(picks[i])
        brackets.append(bracket)
    return brackets

def round_one_comp(brackets): 
    losers=[]; winners_overall=[]
    hp_remaining = []
    for k in range(len(brackets)):
        winners = []
        for i in range(len(brackets[k])):
            for j in range(i+1, len(brackets[k])):
                winner, winner_id, loser, loser_id, hp = battle(brackets[k][i],brackets[k][j])
                winners.append(winner_id)
        count = Counter(winners).most_common(2)
        for i  in range(len(count)):
            winners_overall.append(count[i][0])

    losers = [i for i in range(1,152)]

    for i in winners_overall:
        losers.remove(i)

    winners = []
    for i in range(len(losers)-1):
        for j in range(i+1, len(losers)):
            winner, winner_id, loser, loser_id, hp = battle(losers[i],losers[j])
            winners.append(winner_id)
    count = Counter(winners).most_common(4)
    for i  in range(len(count)):
        winners_overall.append(count[i][0])

    return winners_overall

def tournament_comps(contestants):
    winners = []
    for i in range(0,len(contestants),2):
        winner, winner_id, loser, loser_id, hp = battle(contestants[i], contestants[i+1])
        winners.append(winner_id)

    return winners

def tournament(contestants):
    winners = [tournament_comps(contestants)]
    for i in range(1,6):
        winners.append(tournament_comps(winners[i-1]))
    return winners


'''

brackets = round_one_draft(pokeInfo)
contestants = round_one_comp(brackets)
champs = tournament(contestants)

for i in range(3,6):
    for j in range(len(champs[i])):
        print(pokeInfo[champs[i][j]].get('name'))

'''
winners, losers, hp_remaining = championship()

winners_total, losers_total, hp_remaining_total = championshipRankingAvg(100)

'''
championRankingDict = {}
for i, row in enumerate(pokeInfo):
    championRankingDict[i] = {
        'name' : row['name'].replace("'",''),
        'wins' : 0,
        'loss' : 0,
        'win/lose_ratio' : 0.0,
        'hp_remaining' : 0.0,
        'hp_percentage' : 0.0}
            
for i in range(n):
    winners, losers, hp_remaining = championship()
    for i in range(len(winners)):
        championRankingDict[winners[i]]['wins'] += 1
'''