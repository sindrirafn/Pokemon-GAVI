import csv

print('hallo')

f = open('pokemon.csv')
dreader = csv.DictReader(f, delimiter=',')
gen1 = 0
data = []
for i in dreader:
    data.append(i)
    if gen1 == 167:
        break
    gen1 += 1

name_set = []
type1_set = []
type2_set = []
#,Name,Type 1,Type 2,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
for i in data:
    name = i['Name']
    name_set.append(name)
f.close()