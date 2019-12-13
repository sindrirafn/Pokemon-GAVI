import pokemonDict
import movesReader
import random
from collections import Counter
import time


moves = movesReader.import_moves()
pokeDict = pokemonDict.pokeDict(moves)
topMoves = pokemonDict.topMoveDict(moves, pokeDict)

def accuracy(accuracy):                         # Fall sem skilar true/false sem ákvedur hvort ad pokemon hitti eda ekki
    return(random.randint(1,100)<accuracy)


#   = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


def battle(A, B):                               # Fall sem hermir bardagana á milli pokémona
    
    # Special_types er listi af move types sem falla undir special. 
    special_types = ['Water', 'Grass', 'Fire', 'Ice', 'Electric', 'Psychic', 'Dragon', 'Dark'] 

    if pokeDict.get(A)['speed'] > pokeDict.get(B)['speed']:     # Ákvedur hvada pokémon byrjar útfrá thví hvor er med haerra speed.
        fighterA = pokeDict.get(A); fighterB = pokeDict.get(B)
        movesA = pokeDict.get(A); movesB = pokeDict.get(B)
        fighterA_id = A; fighterB_id = B
    else:
        fighterA = pokeDict.get(B); fighterB = pokeDict.get(A)
        movesA = pokeDict.get(B); movesB = pokeDict.get(A)
        fighterA_id = B; fighterB_id = A

    hpA = fighterA.get('hp'); hpB = fighterB.get('hp')              # Núllstillir Hp 

    # Velur random hvada move pokémoninn notar í bardaganum. Til thess ad minnka keyrslutíma var alltaf notad sama move í gegnum hvern
    # bardaga í stad thess ad velja nytt í hverju roundi.
    pick = random.randint(0,len(topMoves[A].get('top_moves'))-1)    
    moveA = topMoves[A].get('top_moves')[pick] 
    pick = random.randint(0,len(topMoves[B].get('top_moves'))-1)
    moveB = topMoves[B].get('top_moves')[pick]

    # Thegar special move er notad er dmg reiknad útfrá special attack/defense, annars venjulega attack/defense
    if moveA in special_types:
        attackA = fighterA.get('sp_att'); defenseB = fighterB.get('sp_def')
    else:
        attackA = fighterA.get('attack'); defenseB = fighterB.get('defense')

    if moveB in special_types:
        attackB = fighterB.get('sp_att'); defenseA = fighterA.get('sp_def')
    else:
        attackB = fighterB.get('attack'); defenseA = fighterA.get('defense')
     
    # Finnur attack power fyrir thad move sem er notad
    attPowA =  moves[moveA].get('power'); attPowB =  moves[moveB].get('power')
                    
    # Modifier reiknadur. That er studull á advantage útfrá af hvada type pokémonarnir eru, t.d. Electric hafa advantage yfir Water
    modA = movesB.get(fighterA.get('type1')) * movesB.get(fighterA.get('type2'))
    if modA == 0.0:
        modA = 0.1      # Ef modifier er 0 er hann settur í 0.1 til ad fordast ad bardagar geti haldid endalaust áfram
    dmgA = round(((((2/5 + 2)*attPowA*attackA/defenseB) / 50) + 2) * modA)
    
    modB = movesA.get(fighterB.get('type1')) * movesA.get(fighterB.get('type2'))
    if modB == 0.0:
        modB = 0.1
    dmgB = round(((((2/5 + 2)*attPowB*attackB/defenseA) / 50) + 2) * modB)


    # Bardaginnn sjálfur. Heldur áfram thar til hp annars pokémons klárast
    while hpA > 0 and hpB > 0:
        # Fighter 1 gerir
        if accuracy(moves[moveA].get('acc')):
            hpB -= dmgA
            if hpB <= 0:
                break

        # Fighter 2 gerir
        if accuracy(moves[moveB].get('acc')):
            hpA -= dmgB

    # Skilar gildum í eftirfarandi rod: sigurvegari, id sigurvegara, tapari, id tapara, hp sem sigurvegari á eftir
    if hpA <= 0:    
        return fighterB, fighterB_id, fighterA, fighterA_id, hpB
    elif hpB <= 0:
        return fighterA, fighterA_id, fighterB, fighterB_id, hpA


#   = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Fallid sem vid gerdum fyrir demo í kynningu
# Eins og hitt battle fallid ad flestu leyti
# Í thessu er ekki alltaf sama move í gegnnum allan bardagann, heldur er nytt valid í hverju roundi
# Thar fyrir utan er allt eins nema print skipunum baett vid
def battle_showcase(): 
    print(' \n')
    nameA = input("Enter the first pokémon's name: ")
    nameB = input("Enter the second pokémon's name: ")
    print('\n\n- - -\n')
    for i in range(1,152):
        if nameA == pokeDict[i].get('name'): A = i
        if nameB == pokeDict[i].get('name'): B = i

    print(pokeDict[A].get('name'),'vs.', pokeDict[B].get('name'),'!!\n')
    time.sleep(2)

    special_types = ['Water', 'Grass', 'Fire', 'Ice', 'Electric', 'Psychic', 'Dragon', 'Dark']

    if pokeDict.get(A)['speed'] > pokeDict.get(B)['speed']:
        fighterA = pokeDict.get(A); fighterB = pokeDict.get(B)
        movesA = pokeDict.get(A); movesB = pokeDict.get(B)
        fighterA_id = A; fighterB_id = B
    else:
        fighterA = pokeDict.get(B); fighterB = pokeDict.get(A)
        movesA = pokeDict.get(B); movesB = pokeDict.get(A)
        fighterA_id = B; fighterB_id = A

    hpA = fighterA.get('hp'); hpB = fighterB.get('hp')

    while hpA > 0 and hpB > 0:

        pick = random.randint(0,len(topMoves[A].get('top_moves'))-1)
        moveA = topMoves[A].get('top_moves')[pick] 
        pick = random.randint(0,len(topMoves[B].get('top_moves'))-1)
        moveB = topMoves[B].get('top_moves')[pick]

        if moveA in special_types:
            attackA = fighterA.get('sp_att'); defenseB = fighterB.get('sp_def')
        else:
            attackA = fighterA.get('attack'); defenseB = fighterB.get('defense')

        if moveB in special_types:
            attackB = fighterB.get('sp_att'); defenseA = fighterA.get('sp_def')
        else:
            attackB = fighterB.get('attack'); defenseA = fighterA.get('defense')
        

        attPowA =  moves[moveA].get('power'); attPowB =  moves[moveB].get('power')
                            
        modA = movesB.get(fighterA.get('type1')) * movesB.get(fighterA.get('type2'))
        if modA == 0.0:
            modA = 0.1
        dmgA = round(((((2/5 + 2)*attPowA*attackA/defenseB) / 50) + 2) * modA)
        
        modB = movesA.get(fighterB.get('type1')) * movesA.get(fighterB.get('type2'))
        if modB == 0.0:
            modB = 0.1
        dmgB = round(((((2/5 + 2)*attPowB*attackB/defenseA) / 50) + 2) * modB)

        # Fighter 1 turn
        print('- - -\n\n')
        time.sleep(1)
        print(fighterA.get('name'), 'uses', moveA,'. ',end='')
        if accuracy(moves[moveA].get('acc')):
            hpB -= dmgA
            print('It hurts ', fighterB.get('name'), ' by ', str(dmgA), 'HP! \n\n')

            time.sleep(1)
            if hpB <= 0:
                hpB = 0
                print(fighterA.get('name'),': ', str(int(hpA)),'HP  - ',fighterB.get('name'),': ', str(int(hpB)),'HP\n')
                time.sleep(1)
                break
        else:
            print('It misses \n\n')
            time.sleep(1)
        

        # Fighter 2 turn
        print(fighterB.get('name'), 'uses', moveB,'. ',end='')

        if accuracy(moves[moveB].get('acc')):
            hpA -= dmgB
            print('It hurts ', fighterA.get('name'), ' by ', str(dmgB), 'HP!\n\n')
            time.sleep(1)
        else:
            print('It misses \n\n')
            time.sleep(1)

        
 
        if hpA < 0 : hpA = 0
        if hpB < 0 : hpB = 0
        print(fighterA.get('name'),': ', str(int(hpA)),'HP  - ',fighterB.get('name'),': ', str(int(hpB)),'HP\n')
        time.sleep(1)

    if hpA <= 0:
        print('- - -\n\n')
        time.sleep(1)
        print(fighterA.get('name'), 'fainted... \n')
        time.sleep(1)
        print(fighterB.get('name'), 'wins!! \n')
        time.sleep(3)
        return
    elif hpB <= 0:
        print('- - -\n\n')
        time.sleep(1)
        print(fighterB.get('name'), 'fainted... \n')
        time.sleep(1)
        print(fighterA.get('name'), 'wins!! \n')
        time.sleep(3)
        return   


#   = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


def championship():                     # Fall sem hermir bardaga thar sem allir keppa gegn ollum
    winners = []; losers=[]
    hp_remaining = []
    for i in range(1,len(pokeDict)):
        for j in range(i+1,len(pokeDict)+1):
            winner, winner_id, loser, loser_id, hp = battle(i,j)
            winners.append(winner.get('name'))
            losers.append(loser.get('name'))
            hp_remaining.append(hp)
    return winners, losers, hp_remaining        # Skilar lista af sigurvegurum, topurum og hp sem sigurvegari á eftir


#   = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Ítrar n sinnum í gegnum championship() og skilar listum med ollum nidurstodum
def championshipRankingAvg(n): 
    winners_total = []
    losers_total = []
    hp_remaining_total = []
    for i in range(n):
        winners, losers, hp_remaining = championship()
        winners_total.extend(winners)
        losers_total.extend(losers)
        hp_remaining_total.extend(hp_remaining)
    return winners_total, losers_total, hp_remaining_total


#   = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Fall sem ad skila ridlaskiptingu úr ollum pokemonum
def round_one_draft(pokeDict):
    brackets = []; bracket = []
    pokemon_id_list = [i for i in range(1,152)]     # Listi af ollum mogulegum id
    picks = random.sample(pokemon_id_list,6)        # Velur 6 random id
    for i in range(len(picks)):                     # Baetir thessum id í fyrsta ridil og tekur úr id listanum
        bracket.append(picks[i]) 
        pokemon_id_list.remove(picks[i])
    brackets.append(bracket)
    while pokemon_id_list != []:                    # gerir thad sama og var gert fyrir ofan thar til id listi taemist
        bracket = [] 
        picks = random.sample(pokemon_id_list,5)    # Nuna er urtakid adeins 5
        for i in range(len(picks)):
            bracket.append(picks[i]) 
            pokemon_id_list.remove(picks[i])
        brackets.append(bracket)
    return brackets                                 # Skilar ridlum


#   = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Fall sem fer í gegnum hvern ridil og skilar út 2 stigahaestu úr hverjum
def round_one_comp(brackets):                       
    losers=[]; winners_overall=[]

    for k in range(len(brackets)):      # Her er ítrad í gegnum hvern ridil
        winners = []
        for i in range(len(brackets[k])):
            for j in range(i+1, len(brackets[k])):
                winner_id = battle(brackets[k][i],brackets[k][j])[1]
                winners.append(winner_id)
        count = Counter(winners).most_common(2)
        for i  in range(len(count)):
            winners_overall.append(count[i][0])

    losers = [i for i in range(1,152)]  # Listi af ollum id sem er notadur til ad sigta ut tapara

    for i in winners_overall:
        losers.remove(i)                # Sigurvegarar eru teknir úr listanum svo eftir standa bara taparar

    winners = []
    for i in range(len(losers)-1):      # Allir á móti ollum á milli taparanna. Top 4 baetast svo á sigurvegaralistann og halda áfram
        for j in range(i+1, len(losers)):
            winner_id = battle(losers[i],losers[j])[1]
            winners.append(winner_id)
    count = Counter(winners).most_common(4)
    for i  in range(len(count)):
        winners_overall.append(count[i][0])

    return winners_overall              # Skilar lista af sigurvegurum sem halda svo áfram í útsláttarkeppni


#   = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Fall sem ítrar í gegnnum lista af keppendum og tekur fyrir tvo í einu sem berjast. Thad skilar svo sigurvegurum.
# Thar sem thad eru tveir teknir fyrir í einu helmingast listinn thegar thetta fall er notad
def tournament_comps(contestants):          
    winners = []
    for i in range(0,len(contestants),2):
        winner_id = battle(contestants[i], contestants[i+1])[1]
        winners.append(winner_id)
    return winners


#   = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Hér er endurtekin tournament_comp() thangad til ad einn sigurvegari stendur eftir
# Haldid er utanum hversu langt hver keppandi kemst
def tournament(contestants):
    winners = [tournament_comps(contestants)]
    for i in range(1,6):
        winners.append(tournament_comps(winners[i-1]))
    return winners


#   = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Í thessu falli eru haldin n morg tournament. 
# Fallid byr til dict útfrá id og nafni keppenda og thannig haldid utan um stigin theirra
def tournamentRankingDict(n):
    tournamentRankingDict = {}
    for i in range(len(pokeDict)):          # Nullstilling á dict
        tournamentRankingDict[i+1] = {
            'name' : pokeDict[i+1].get('name'),
            'points' : 0
            }
    for i in range(n):                          # Ítrad n sinnum
        brackets = round_one_draft(pokeDict)
        contestants = round_one_comp(brackets)
        champs = tournament(contestants)        # Tournament haldid sem skilar lista med nidurstodum
        champs.reverse()                        # Lista snuid vid svo fyrsta saeti se fremst
        rankings = []
         # Hér er farid í gegnum listann af nidurstodum. Their sem komust áfram eru fjarlaegdir
         # úr listanum fyrir nedan til thess ad vera koma ekki tvisvar fyrir
        rankings.append(champs[0])              
        for i in range(1,len(champs)):         
            rankings.append([x for x in champs[i] if x not in champs[i-1]])
        rankings.append([x for x in contestants if x not in champs[5]])
        rankings.reverse()
        # Stigagjof. Hér er farid í gegnum rankings og gefin stig, sem leggjast svo saman í dict.
        # gefid er 1 stig fyrir ad komast upp í útsláttarkeppni, 2 stig fyrir ad komast uppúr fyrstu umferd o.s.frv.
        for i, rank in enumerate(rankings):
            for j in rank:
                tournamentRankingDict[j]['points'] += i+1
    return tournamentRankingDict
