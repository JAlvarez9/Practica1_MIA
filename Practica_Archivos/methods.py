
from sqlalchemy.sql import text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:contra@localhost:5432/blackbuster')
comitaso = engine.execution_options(isolation_level="AUTOCOMMIT")


def readCSV():
	statement = text("""create table "unique".Temporal (
 	NOMBRE_CLIENTE text,
 	CORREO_CLIENTE text,
 	CLIENTE_ACTIVO text,
 	FECHA_CREACION date,
 	TIENDA_PREFERIDA text,
 	DIRECCION_CLIENTE text,
 	CODIGO_POSTAL int,
 	CIUDAD_CLIENTE text,
 	PAIS_CLIENTE text,
 	FECHA_RENTA timestamp,
 	FECHA_RETORNO timestamp,
 	MONTO_A_PAGAR float,
 	FECHA_PAGO timestamp,
 	NOMBRE_EMPLEADO text,
 	CORREO_EMPLEADO text,
 	EMPLEADO_ACTIVO text,
 	TIENDA_EMPLEADO text,
 	USUARIO_EMPLEADO text,
 	CONTRASENA_EMPLEADO text,
 	DIRECCION_EMPLEADO text,
 	CODIGO_POSTAL_EMPLEADO int,
 	CIUDAD_EMPLEADO text,
 	PAIS_EMPLEADO text,
 	NOMBRE_TIENDA text,
 	ENCARGADO_TIENDA text,
 	DIRECCION_TIENDA text,
 	CODIGO_POSTAL_TIENDA int,
 	CIUDAD_TIENDA text,
 	PAIS_TIENDA text,
 	TIENDA_PELICULA text,
 	NOMBRE_PELICULA text,
 	DESCRIPCION_PELICULA text,
 	ANO_LANZAMIENTO int,
 	DIAS_RENTA int,
 	COSTO_RENTA float,
 	DURACION int,
 	COSTO_POR_DANO float,
 	CLASIFICACION text,
 	LENGUAJE_PELICULA text,
 	CATEGORIA_PELICULA text,
 	ACTOR_PELICULA text
);

COPY "unique".Temporal from '/home/josee/Documents/Archivos/Practica/BlockbusterData.csv' with DELIMITER ';' NULL '-' CSV HEADER ENCODING 'latin-1';""")
      
	engine.execute(statement)
	comitaso


def generarER():

	statement1 = text("""
					
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

	""")
	engine.execute(statement1)
	comitaso
	
	statement = text("""
					
				INSERT INTO
			"unique".country(name)
			select distinct pais_cliente
			from "unique".temporal
			where pais_cliente is not null;


		INSERT INTO
			"unique".dubbing(name)
			select distinct lenguaje_pelicula
			from "unique".temporal
			where lenguaje_pelicula is not null;


		INSERT INTO
			"unique".actor(first_name, last_name)
			select distinct split_part(actor_pelicula,' ',1),split_part(actor_pelicula,' ',2)
			from "unique".temporal
			where actor_pelicula is not null;


		INSERT INTO
			"unique".category(name)
			select distinct categoria_pelicula
			from "unique".temporal
			where categoria_pelicula is not null;


		INSERT INTO
			"unique".city(country_id, name)
			select distinct (select id from "unique".country where temporal.pais_cliente = "unique".country.name),
							ciudad_cliente
			from "unique".temporal
			where temporal.ciudad_cliente is not null and temporal.pais_cliente is not null ;


		INSERT INTO
			"unique".adress(name, postal_code, id_city)
			select distinct direccion as dierct, code_postl as code, code_ciudad2 as code_ciudad
							from (SELECT direccion_cliente as direccion, pais_cliente as pais, codigo_postal as code_postl, ciudad_cliente as ciudad FROM "unique".temporal
								UNION
								SELECT direccion_empleado, pais_empleado, codigo_postal_empleado, ciudad_empleado  FROM "unique".temporal
								UNION
								SELECT direccion_tienda, pais_tienda, codigo_postal_tienda, ciudad_tienda FROM "unique".temporal) as asd
								inner join (select "unique".country.name as pais2,"unique".city.country_id as pais_code2,"unique".city.name as ciudad2,"unique".city.id as code_ciudad2
									from "unique".country
									inner join "unique".city
									on "unique".country.id = "unique".city.country_id) as asd2
									on asd.ciudad = asd2.ciudad2 and asd.pais = asd2.pais2;


		INSERT INTO
			"unique".client(first_name, last_name, email, create_date, active, fav_store, id_adress)
			SELECT DISTINCT  split_part(nombre_cliente,' ',1), split_part(nombre_cliente,' ',2),
							correo_cliente,
							fecha_creacion,
							cliente_activo,
							tienda_preferida,
							(select id from "unique".adress where temporal.direccion_cliente = "unique".adress.name)
			FROM "unique".temporal
			WHERE nombre_cliente is not null and
				correo_cliente is not null and
				fecha_creacion is not null and
				cliente_activo is not null and
				tienda_preferida is not null;

		update "unique".client
		set active = case active when 'Si' then '1' when 'No' then '0' end;
		ALTER TABLE "unique".client ALTER COLUMN active SET DATA TYPE boolean USING active::boolean;

		INSERT INTO "unique".store(name, name_boss, id_adress)
		SELECT DISTINCT nombre_tienda,
						encargado_tienda,
						(select id from "unique".adress where temporal.direccion_tienda = "unique".adress.name)
		FROM "unique".temporal
		where nombre_tienda is not null and encargado_tienda is not null;


		INSERT INTO "unique".employer(first_name, last_name, email, active, username, password, id_store, id_adress)
		SELECT DISTINCT split_part(nombre_empleado,' ',1),
						split_part(nombre_empleado,' ',2),
						correo_empleado,
						empleado_activo,
						usuario_empleado,
						contrasena_empleado,
						(select id from "unique".store where temporal.nombre_tienda = "unique".store.name),
						(select id from "unique".adress where temporal.direccion_empleado = "unique".adress.name)
		FROM "unique".temporal
		WHERE nombre_tienda is not null and correo_empleado is not null and empleado_activo is not null
				and  usuario_empleado is not null and contrasena_empleado is not null;


		INSERT INTO "unique".movie(title, description, release_date, duration, available_days, price, damage_price, clasificacion)
		SELECT DISTINCT nombre_pelicula,
						descripcion_pelicula,
						ano_lanzamiento,
						duracion,
						dias_renta,
						costo_renta,
						costo_por_dano,
						clasificacion
		FROM "unique".temporal
		WHERE nombre_pelicula is not null and descripcion_pelicula is not null and ano_lanzamiento is not null
				and duracion is not null and dias_renta is not null and costo_renta is not null and costo_por_dano is not null
				and clasificacion is not null;


		INSERT INTO "unique".rent(mount, date_start, date_back,pay_date , movie_name ,id_client, id_employer)
		SELECT DISTINCT monto_a_pagar,
						fecha_renta,
						fecha_retorno,
						fecha_pago,
						nombre_pelicula,
						(select id from "unique".client where temporal.nombre_cliente = concat("unique".client.first_name,' ', "unique".client.last_name) ),
						(select id from "unique".employer where temporal.nombre_empleado = concat("unique".employer.first_name,' ',"unique".employer.last_name) )
		FROM "unique".temporal
		WHERE monto_a_pagar is not null and fecha_renta is not null and nombre_cliente is not null and nombre_empleado is not null;

		--Insercion tabla Inventario

		INSERT INTO "unique".inventario(id_store, id_movie,exists)
		SELECT DISTINCT "unique".store.id, "unique".movie.id , count(nombre_pelicula) from "unique".store inner join ("unique".movie
					inner join "unique".temporal on "unique".movie.title = "unique".temporal.nombre_pelicula) on "unique".store.name = "unique".temporal.nombre_tienda
					group by "unique".store.id, "unique".movie.id;


		INSERT INTO "unique".movie_actor(id_actor, id_movie)
		SELECT DISTINCT "unique".actor.id,"unique".movie.id
		FROM "unique".actor
		INNER JOIN ("unique".movie
					INNER JOIN "unique".temporal on "unique".movie.title = "unique".temporal.nombre_pelicula)
		on concat("unique".actor.first_name,' ',"unique".actor.last_name) = "unique".temporal.actor_pelicula
		GROUP BY "unique".actor.id, "unique".movie.id;


		INSERT INTO "unique".movie_cate(id_movie, id_category)
		SELECT DISTINCT "unique".movie.id,"unique".category.id
		FROM "unique".category
		INNER JOIN ("unique".movie
					INNER JOIN "unique".temporal on "unique".movie.title = "unique".temporal.nombre_pelicula)
		on "unique".category.name = "unique".temporal.categoria_pelicula
		GROUP BY "unique".movie.id, "unique".category.id;

		INSERT INTO "unique".movie_dub(id_movie, id_dubbing)
		SELECT DISTINCT "unique".movie.id,"unique".dubbing.id
		FROM "unique".dubbing
		INNER JOIN ("unique".movie
					INNER JOIN "unique".temporal on "unique".movie.title = "unique".temporal.nombre_pelicula)
		on "unique".dubbing.name = "unique".temporal.lenguaje_pelicula
		GROUP BY "unique".movie.id, "unique".dubbing.id;

	""")
	engine.execute(statement)
	comitaso
	
def caso1():
	statement = text("""SELECT sum(t2.exists)
		FROM (SELECT exists
		FROM (SELECT *
				FROM "unique".inventario
				INNER JOIN "unique".movie on inventario.id_movie = movie.id) as t
		WHERE t.title = 'SUGAR WONKA') as t2;""")
      
	variable = engine.execute(statement)
	comitaso
	return variable

def caso2():
	statement = text("""SELECT *
				FROM "unique".rent
				INNER JOIN "unique".client on rent.id_client = client.id;


		SELECT
			concat(t.first_name,' ',t.last_name) as Nombre,
			COUNT (t.id_client) as compras,
			round(CAST(sum(t.mount) as numeric),2) as monto_total
		FROM
			(SELECT *
				FROM "unique".rent
				INNER JOIN "unique".client on rent.id_client = client.id) as t
		GROUP BY
			concat(t.first_name,' ',t.last_name)
		HAVING
			COUNT (t.id_client) >= 40;""")
      
	variable = engine.execute(statement)
	comitaso
	return variable

def caso3():
	statement = text("""SELECT concat(first_name,' ',last_name) as name
			FROM "unique".actor
			WHERE  actor.last_name like '%son%'
			ORDER BY concat(first_name,' ',last_name);""")
      
	variable = engine.execute(statement)
	comitaso
	return variable

def caso4():
	statement = text("""SELECT concat(t.first_name,' ',t.last_name) as nombre, t.release_date as anio_lanzamiento
		FROM(SELECT *
			FROM (SELECT *
					FROM "unique".movie_actor
					INNER JOIN "unique".actor a on a.id = movie_actor.id_actor) as t2
			INNER JOIN "unique".movie m on m.id = t2.id_movie) as t
		WHERE  t.description like '%Crocodile%' and t.description like '%Shark%'
		ORDER BY nombre asc ;""")
      
	variable = engine.execute(statement)
	comitaso
	return variable

def caso5():
	statement = text("""SELECT t.Country, t.nombre,  t.contador, (t.contador/(SELECT sum(t.contador)
			FROM (SELECT *
					FROM (SELECT
							t.nombre as nombre,
							t.pais  as Country,
							count(t.id_client) as contador
							FROM
								(SELECT id_client, concat(first_name,' ',last_name) as nombre,c2.name as pais
								FROM "unique".rent
								INNER JOIN "unique".client on rent.id_client = client.id
								INNER JOIN "unique".adress a on a.id = client.id_adress
								INNER JOIN "unique".city c on c.id = a.id_city
								INNER JOIN "unique".country c2 on c2.id = c.country_id) as t
							GROUP BY
								t.pais, t.nombre
							ORDER BY
								COUNT ( t.id_client) DESC) as t
						WHERE Country = (Select t2.Country
										FROM (SELECT DISTINCT
											t.nombre as Nombre,
											t.pais  as Country,
											COUNT (t.id_client) as Contador
											FROM
												(SELECT id_client, concat(first_name,' ',last_name) as nombre,c2.name as pais
												FROM "unique".rent
												INNER JOIN "unique".client on rent.id_client = client.id
												INNER JOIN "unique".adress a on a.id = client.id_adress
												INNER JOIN "unique".city c on c.id = a.id_city
												INNER JOIN "unique".country c2 on c2.id = c.country_id) as t
											GROUP BY
												t.nombre, t.pais
											ORDER BY
												COUNT ( t.id_client) DESC
												LIMIT 1) as t2
										))as t) * 100)as porcentaje
			FROM (SELECT *
			FROM (SELECT
					t.nombre as nombre,
					t.pais  as Country,
					count(t.id_client) as contador
				FROM
					(SELECT id_client, concat(first_name,' ',last_name) as nombre,c2.name as pais
					FROM "unique".rent
					INNER JOIN "unique".client on rent.id_client = client.id
					INNER JOIN "unique".adress a on a.id = client.id_adress
					INNER JOIN "unique".city c on c.id = a.id_city
					INNER JOIN "unique".country c2 on c2.id = c.country_id) as t
				GROUP BY
					t.pais, t.nombre
				ORDER BY
					COUNT ( t.id_client) DESC) as t
			WHERE Country = (Select t2.Country
							FROM (SELECT DISTINCT
								t.nombre as Nombre,
								t.pais  as Country,
								COUNT (t.id_client) as Contador
								FROM
									(SELECT id_client, concat(first_name,' ',last_name) as nombre,c2.name as pais
									FROM "unique".rent
									INNER JOIN "unique".client on rent.id_client = client.id
									INNER JOIN "unique".adress a on a.id = client.id_adress
									INNER JOIN "unique".city c on c.id = a.id_city
									INNER JOIN "unique".country c2 on c2.id = c.country_id) as t
								GROUP BY
									t.nombre, t.pais
								ORDER BY
									COUNT ( t.id_client) DESC
									LIMIT 1) as t2
							)) as t;""")
      
	variable = engine.execute(statement)
	comitaso
	return variable

def caso6():
	statement = text("""WITH ciudad_pais_cont as(SELECT c2.name as pais,c.name as ciudad,count(c2.name) as contador_cliente
                    FROM "unique".client b
					INNER JOIN "unique".adress a on a.id = b.id_adress
					INNER JOIN "unique".city c on c.id = a.id_city
					INNER JOIN "unique".country c2 on c2.id = c.country_id
					group by c.name, c2.name),
					contadores as (SELECT ciudad_pais_cont.pais,
						count(ciudad_pais_cont.pais) as contador
					FROM ciudad_pais_cont
					group by ciudad_pais_cont.pais),
					tablita_final as (SELECT ciudad_pais_cont.pais as pais, ciudad_pais_cont.ciudad as ciudad, CAST(ciudad_pais_cont.contador_cliente as numeric) as cliente, CAST(contadores.contador as numeric) as totales
										,ciudad_pais_cont.contador_cliente as total_clientes
					FROM ciudad_pais_cont
					INNER JOIN  contadores on ciudad_pais_cont.pais = contadores.pais)
					SELECT pais, ciudad, total_clientes ,round(CAST((cliente/totales)*100 as numeric),2) as Porcentaje
					FROM tablita_final
					ORDER BY pais,ciudad desc
					;""")
      
	variable = engine.execute(statement)
	comitaso
	return variable

def caso7():
	statement = text("""WITH rentid_ciudad_pais as (SELECT count(c2.name) as renta,c.name as ciudad,c2.name as pais
                            FROM "unique".rent r
                            INNER JOIN "unique".client on r.id_client = client.id
                            INNER JOIN "unique".adress a on a.id = client.id_adress
                            INNER JOIN "unique".city c on c.id = a.id_city
                            INNER JOIN "unique".country c2 on c2.id = c.country_id
                            group by c.name, c2.name
							),
							contadores as (SELECT pais,
								count(pais) as contador,
									sum(renta) as merotoal
							FROM rentid_ciudad_pais
							group by pais),
							tablita_final as (SELECT rentid_ciudad_pais.pais as pais, rentid_ciudad_pais.ciudad as ciudad, CAST(rentid_ciudad_pais.renta as numeric) as cliente, CAST(contadores.contador as numeric) as totales
							FROM rentid_ciudad_pais
							INNER JOIN  contadores on rentid_ciudad_pais.pais = contadores.pais)
							SELECT pais, ciudad, round(CAST((cliente/totales) as numeric),2) as promedio
							FROM tablita_final
							ORDER BY pais asc; """)
      
	variable = engine.execute(statement)
	comitaso
	return variable

def caso8():
	statement = text("""WITH rent_cat_country as (SELECT c2.name as pais, c3.name as categoria, count(c2.name) as renta
                          FROM "unique".rent r
						INNER JOIN "unique".client on r.id_client = client.id
						INNER JOIN "unique".adress a on a.id = client.id_adress
						INNER JOIN "unique".city c on c.id = a.id_city
						INNER JOIN "unique".country c2 on c2.id = c.country_id
						INNER JOIN "unique".movie m on m.title = r.movie_name
						INNER JOIN "unique".movie_cate mo_ca on mo_ca.id_movie = m.id
						INNER JOIN "unique".category c3 on c3.id = mo_ca.id_category
												group by c2.name,c3.name
						),
						total_rentas_pais as (SELECT pais,
								sum(renta) as merotoal
						FROM rent_cat_country
						group by pais),
						just_sports as (SELECT *
						FROM rent_cat_country
						WHERE rent_cat_country.categoria = 'Sports'
						),
						tablita_final as (SELECT just_sports.pais as pais, CAST(just_sports.renta as numeric) as cliente, CAST(total_rentas_pais.merotoal as numeric) as totales
						FROM just_sports
						INNER JOIN  total_rentas_pais on total_rentas_pais.pais = just_sports.pais)
						SELECT pais, round(CAST((cliente/totales)*100 as numeric),2) as porcentaje
						FROM tablita_final
						;""")
      
	variable = engine.execute(statement)
	comitaso
	return variable

def caso9():
	statement = text("""WITH rentid_ciudad_pais as (SELECT count(c2.name) as renta,c.name as ciudad,c2.name as pais
                            FROM "unique".rent r
                            INNER JOIN "unique".client on r.id_client = client.id
                            INNER JOIN "unique".adress a on a.id = client.id_adress
                            INNER JOIN "unique".city c on c.id = a.id_city
                            INNER JOIN "unique".country c2 on c2.id = c.country_id
                            group by c.name, c2.name
							),
							renta_dayton as (SELECT *
							FROM rentid_ciudad_pais
							WHERE rentid_ciudad_pais.pais = 'United States')
							SELECT *
							FROM renta_dayton
							WHERE renta_dayton.renta > (SELECT renta
							FROM rentid_ciudad_pais
							WHERE rentid_ciudad_pais.ciudad = 'Dayton');""")
      
	variable = engine.execute(statement)
	comitaso
	return variable

def caso10():
	statement = text("""WITH primera as (SELECT c2.name as pais, c.name as ciudad, c3.name as categoria, count(c3.name) as rentas
			FROM "unique".rent r
			INNER JOIN "unique".client on r.id_client = client.id
			INNER JOIN "unique".adress a on a.id = client.id_adress
			INNER JOIN "unique".city c on c.id = a.id_city
			INNER JOIN "unique".country c2 on c2.id = c.country_id
			INNER JOIN "unique".movie m on m.title = r.movie_name
			INNER JOIN "unique".movie_cate mo_ca on mo_ca.id_movie = m.id
			INNER JOIN "unique".category c3 on c3.id = mo_ca.id_category
				GROUP BY c.name, c2.name, c3.name
				ORDER BY pais,ciudad,rentas DESC ),
			cates as (SELECT categoria,
				count(categoria) as contador
			FROM primera
			GROUP BY categoria)
			SELECT pais,ciudad,categoria,rentas
			FROM primera tb1
			WHERE tb1.rentas = (SELECT DISTINCT max(tb2.rentas)
								FROM primera tb2
								WHERE tb2.ciudad=tb1.ciudad) AND tb1.categoria='Horror';""")
      
	variable = engine.execute(statement)
	comitaso
	return variable

def truncateTemp():
	statement = text("""TRUNCATE "unique".temporal;""")
	engine.execute(statement)
	comitaso
	return 

def dropER():
	statement = text("""
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
		drop table "unique".country;""")
	engine.execute(statement)
	comitaso
	return 