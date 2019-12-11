select p.poke_dex, p.pokemon, (p.attack + p.hp + p.defense + p.speed + p.sp_att + p.sp_def) as total
from pokemons p
group by p.poke_dex, p.pokemon, total
order by total desc;

select m.id, m.move, (m.power*m.acc/100.0) as total
from moves m
group by m.id, m.move, total
order by total desc ;

select m.id, m.move, (m.power + m.acc) as total
from moves m
group by m.id, m.move, total
order by total desc ;

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
