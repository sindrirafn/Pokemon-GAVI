select p.poke_dex, p.pokemon, (p.attack + p.hp + p.defense + p.speed + p.sp_att + p.sp_def) as total
from pokemons p
group by p.poke_dex, p.pokemon, total
order by total desc;

select m.id, m.move, (m.power * m.acc / 100.0) as total
from moves m
group by m.id, m.move, total
order by total desc;

select m.id, m.move, (m.power + m.acc) as total
from moves m
group by m.id, m.move, total
order by total desc;

select p.poke_dex,
       p.pokemon,
       (p.bug + p.dark
           + p.dragon + p.electric
           + p.fairy + p.fire
           + p.flying + p.ghost
           + p.grass + p.ground
           + p.ice + p.normal
           + p.poison + p.psychic
           + p.rock + p.steel +
        p.water) as total
from pokeagainst p
group by p.poke_dex, p.pokemon, total
order by total desc;


select c.winners,
       p.type1,
       p.type2,
       count(c.winners) / 20.0                    as Avgwins,
       (sum(c.hp_remaining) / (count(c.winners))) as avgHP
from champ c,
     pokemons p
where p.pokemon = c.winners
group by c.winners, p.type1, p.type2
order by Avgwins desc;

-- top moves hjá öllum pokemon eftir hvað það kemur oft fyrir.
select m.move, (count(m.move)) snakes, m.power, m.acc
from bestmoves b,
     moves m
where m.move = b.best
   or m.move = b.second
   or m.move = b.third
group by m.move, m.power, m.acc
order by snakes desc;

-- Herna er eg að prenta út lista sem sýnir hver var með flestu avgWins í hverju "roundi" og hvað avgHP hann er með eftir
-- hvern einasta fight.
select c.winners,
       p.type1,
       p.type2,
       count(c.winners) / 20.0                    as Avgwins,
       (sum(c.hp_remaining) / (count(c.winners))) as avgHP
from champ c,
     pokemons p
where p.pokemon = c.winners
group by c.winners, p.type1, p.type2
order by Avgwins desc;

-- Herna er haegt ad sja hvada "Type1" er með yfirburði í top20 í championship.

select win.type1, count(win.type1) as fjolditype1
from (select c.winners,
             p2.type1,
             count(c.winners) / 20.0 as Avgwins,
             p2.type2
      from champ c,
           pokemons p2
      where c.winners = p2.pokemon
      group by c.winners, p2.type1, p2.type2
      order by Avgwins desc
      limit 20) as win
group by win.type1
order by fjolditype1 desc;

-- Herna er haegt ad sja hvada "Type2" er með yfirburði í top20 í championship.

select win.type2, count(win.type2) as fjolditype1
from (select c.winners,
             count(c.winners) / 20.0 as Avgwins,
             p2.type2
      from champ c,
           pokemons p2
      where c.winners = p2.pokemon
      group by c.winners, p2.type1, p2.type2
      order by Avgwins desc
      limit 20) as win
group by win.type2
order by fjolditype1 desc;


select win.type1, count(win.type1) as fjolditype1
from (select c.winners,
             p2.type1,
             count(c.winners) / 20.0 as Avgwins
      from champ c,
           pokemons p2
      where c.winners = p2.pokemon
      group by c.winners, p2.type1, p2.type2
      order by Avgwins desc
      limit 20) as win,
     (select win2.type2, count(win2.type2) as fjolditype1
      from (select c.winners,
                   p2.type2,
                   count(c.winners) / 20.0 as Avgwins
            from champ c,
                 pokemons p2
            where c.winners = p2.pokemon
            group by c.winners, p2.type1, p2.type2
            order by Avgwins desc
            limit 20) as win2
      group by win2.type2
      order by fjolditype1 desc) as win3
group by win.type1
order by fjolditype1 desc;