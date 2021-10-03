--Inserciones a las tablas de la Entidad Relacion

-- Insert a la tabla de countries
INSERT INTO
    "unique".country(name)
    select distinct pais_cliente
    from "unique".temporal
    where pais_cliente is not null;

-- Insert a la tabla de Dubbing
INSERT INTO
    "unique".dubbing(name)
    select distinct lenguaje_pelicula
    from "unique".temporal
    where lenguaje_pelicula is not null;

--Inserta a la tabla de Actor
INSERT INTO
    "unique".actor(first_name, last_name)
    select distinct split_part(actor_pelicula,' ',1),split_part(actor_pelicula,' ',2)
    from "unique".temporal
    where actor_pelicula is not null;

--Inserta a la tabla de Categories
INSERT INTO
    "unique".category(name)
    select distinct categoria_pelicula
    from "unique".temporal
    where categoria_pelicula is not null;

--Inserta en la tabla de City


INSERT INTO
    "unique".city(country_id, name)
    select distinct (select id from "unique".country where temporal.pais_cliente = "unique".country.name),
                    ciudad_cliente
    from "unique".temporal
    where temporal.ciudad_cliente is not null and temporal.pais_cliente is not null ;

--Insertar en la tabla de Adress

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


--Insercion a la tabla de clientes


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

--Insercion de Stores

INSERT INTO "unique".store(name, name_boss, id_adress)
SELECT DISTINCT nombre_tienda,
                encargado_tienda,
                (select id from "unique".adress where temporal.direccion_tienda = "unique".adress.name)
FROM "unique".temporal
where nombre_tienda is not null and encargado_tienda is not null;

--Insercion de Employer

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

--Insercion de Movies


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


--Insercion tabla Rent


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


--Insercion tabla movie_actor

INSERT INTO "unique".movie_actor(id_actor, id_movie)
SELECT DISTINCT "unique".actor.id,"unique".movie.id
FROM "unique".actor
INNER JOIN ("unique".movie
            INNER JOIN "unique".temporal on "unique".movie.title = "unique".temporal.nombre_pelicula)
on concat("unique".actor.first_name,' ',"unique".actor.last_name) = "unique".temporal.actor_pelicula
GROUP BY "unique".actor.id, "unique".movie.id;


--Insercion tabla movie_cate

INSERT INTO "unique".movie_cate(id_movie, id_category)
SELECT DISTINCT "unique".movie.id,"unique".category.id
FROM "unique".category
INNER JOIN ("unique".movie
            INNER JOIN "unique".temporal on "unique".movie.title = "unique".temporal.nombre_pelicula)
on "unique".category.name = "unique".temporal.categoria_pelicula
GROUP BY "unique".movie.id, "unique".category.id;


--Insercion tabla movie_dub
INSERT INTO "unique".movie_dub(id_movie, id_dubbing)
SELECT DISTINCT "unique".movie.id,"unique".dubbing.id
FROM "unique".dubbing
INNER JOIN ("unique".movie
            INNER JOIN "unique".temporal on "unique".movie.title = "unique".temporal.nombre_pelicula)
on "unique".dubbing.name = "unique".temporal.lenguaje_pelicula
GROUP BY "unique".movie.id, "unique".dubbing.id;