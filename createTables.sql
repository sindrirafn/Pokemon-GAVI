-- insert into pokemon (id, pokemon, type1, type2, hp, attack, defense, sp_att, sp_def, speed, legendary) values (1, "Bulbasaur", "Grass", "Poison", 45.0, 49.0, 49.0, 65.0, 65.0, 45.0, "False");


create table pokemons(
  poke_dex serial,
  pokemon varchar(50),
  type1 varchar(15),
  type2 varchar(15),
  hp float,
  attack float,
  defense float,
  sp_att float,
  sp_def float,
  speed float,
  primary key (poke_dex)
);
-- insert into pokeMoves (id, pokemon, Bug, Dark, Dragon, Electric, Fairy, Fire, Flying, Ghost, Grass, Ground, Ice, Normal, Poison, Psychic, Rock, Steel, Water) values (1, 'Bulbasaur', 1.0, 1.0, 1.0, 0.5, 0.5, 2.0, 2.0, 1.0, 0.25, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.5);

create table pokeAgainst(
  poke_dex serial references pokemons(poke_dex),
  pokemon varchar(50),
  Bug float,
  Dark float,
  Dragon float,
  Electric float,
  Fairy float,
  Fire float,
  Flying float,
  Ghost float,
  Grass float,
  Ground Float,
  Ice Float,
  Normal Float,
  Poison float,
  Psychic float,
  Rock float,
  Steel float,
  Water float,
  primary key (poke_dex)
);

-- create table students(
--     id serial,
--     country varchar(250) references countries(country),
--     study varchar(250) references studies(study)
--     year int,
--     female int,
--     male int,
--     primary key (id)
-- );
-- insert into moves (id, type, category, pp, power, acc) values (2, 'Normal', 'Physical', 10, 15, 85);

create table moves(
  id serial,
  move varchar(20),
  type varchar(15),
  category varchar(15),
  pp float,
  power float,
  acc float,
  primary key (id)
);

drop table pokeAgainst;
drop table pokemons;
drop table moves;
