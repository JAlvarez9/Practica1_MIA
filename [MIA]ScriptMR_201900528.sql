--Creacion de tablas de la Entidad Relacion

CREATE TABLE if not exists "unique".country
(
    id serial NOT NULL,
    name text NOT NULL,
    PRIMARY KEY (id)
);

create table if not exists "unique".dubbing
(
	id serial not null ,
	name text not null,
    PRIMARY KEY (id)
);
create table if not exists "unique".actor
(
	id serial not null,
	first_name text not null,
	last_name text not null,
	PRIMARY KEY (id)
);
create table if not exists "unique".category
(
	id serial not null,
	name text not null,
	PRIMARY KEY (id)
);

CREATE TABLE if not exists "unique".city
(
    id serial NOT NULL,
    country_id int NOT NULL,
    name text not null,
    PRIMARY KEY (id),
    FOREIGN KEY (country_id) REFERENCES "unique".country(id) on UPDATE CASCADE on DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "unique".adress
(
  id serial not null,
  name text,
  postal_code int ,
  id_city int,
  PRIMARY KEY (id),
  FOREIGN KEY (id_city) references "unique".city(id) on update cascade on delete cascade
);


CREATE TABLE if not exists "unique".client
(
  id serial not null ,
  first_name text not null ,
  last_name text not null ,
  email text not null ,
  create_date date not null ,
  active text not null ,
  fav_store text not null,
  id_adress int not null ,
  PRIMARY KEY (id),
  FOREIGN KEY (id_adress) references "unique".adress(id) on update cascade on delete cascade
);

CREATE TABLE if not exists "unique".store
(
  id serial not null ,
  name text not null,
  name_boss text not null,
  id_adress int not null ,
  PRIMARY KEY (id),
  FOREIGN KEY (id_adress) references "unique".adress(id) on update cascade on delete cascade

);

CREATE TABLE IF NOT EXISTS "unique".employer
(
  id serial not null ,
  first_name text not null,
  last_name text not null,
  email text not null,
  active text not null,
  username text not null,
  password text not null ,
  id_store int not null ,
  id_adress int not null ,
  PRIMARY KEY (id),
  FOREIGN KEY (id_store) references "unique".store(id) on update cascade on delete cascade ,
  FOREIGN KEY (id_adress) references  "unique".adress(id) on update cascade on delete cascade
);

CREATE TABLE IF NOT EXISTS "unique".movie
(
  id serial not null,
  title text not null ,
  description text not null ,
  release_date int not null,
  duration int not null ,
  available_days int not null ,
  price float not null ,
  damage_price float not null,
  clasificacion text not null ,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS "unique".inventario
(
  id_store int not null,
  id_movie int not null,
  exists int not null,
  PRIMARY KEY (id_store,id_movie),
  FOREIGN KEY (id_movie) references "unique".movie(id) on update cascade on delete cascade ,
  FOREIGN KEY (id_store) references "unique".store(id) on update cascade on delete cascade
);

CREATE TABLE IF NOT EXISTS "unique".rent
(
  id serial not null ,
  mount float not null ,
  date_start timestamp not null ,
  date_back timestamp ,
  pay_date timestamp,
  id_client int not null ,
  id_employer int not null,
  movie_name text not null,
  PRIMARY KEY (id),
  FOREIGN KEY (id_client) references "unique".client(id) on update cascade on delete cascade ,
  FOREIGN KEY (id_employer) references  "unique".employer(id) on update cascade on delete cascade
);

CREATE TABLE IF NOT EXISTS "unique".movie_dub
(
  id_movie int not null ,
  id_dubbing int not null ,
  PRIMARY KEY (id_movie,id_dubbing),
  FOREIGN KEY (id_movie) references "unique".movie(id) on update cascade on delete cascade ,
  FOREIGN KEY (id_dubbing)references "unique".dubbing(id) on update cascade on delete cascade
);

CREATE TABLE IF NOT EXISTS "unique".movie_actor
(
  id_movie int not null ,
  id_actor int not null ,
  PRIMARY KEY (id_movie,id_actor),
  FOREIGN KEY (id_movie) references "unique".movie(id) on update cascade on delete cascade ,
  FOREIGN KEY (id_actor) references "unique".actor(id) on update cascade on delete cascade
);

CREATE TABLE IF NOT EXISTS "unique".movie_cate
(
  id_movie int not null ,
  id_category int not null ,
  PRIMARY KEY (id_movie,id_category),
  FOREIGN KEY (id_movie) references "unique".movie(id) on update cascade on delete cascade ,
  FOREIGN KEY (id_category) references  "unique".category(id) on update cascade on delete cascade
);

--Drops te las tablas en orden

drop table "unique".movie_cate;
drop table "unique".movie_actor;
drop table "unique".movie_dub;
drop table "unique".rent;
drop table "unique".inventario;
drop table "unique".movie;
drop table "unique".employer;
drop table "unique".store;
drop table "unique".client;
drop table "unique".adress;
drop table "unique".city;
drop table "unique".category;
drop table "unique".actor;
drop table "unique".dubbing;
drop table "unique".country;