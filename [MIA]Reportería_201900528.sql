--Consulta 1

--Si es 85
SELECT sum(t2.exists)
FROM (SELECT exists
FROM (SELECT *
        FROM "unique".inventario
        INNER JOIN "unique".movie on inventario.id_movie = movie.id) as t
WHERE t.title = 'SUGAR WONKA') as t2;


--Consulta 2
SELECT *
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
	COUNT (t.id_client) >= 40;


--Consulta 3

SELECT concat(first_name,' ',last_name) as name
FROM "unique".actor
WHERE  actor.last_name like '%son%'
ORDER BY concat(first_name,' ',last_name);

--Consulta 4

SELECT concat(t.first_name,' ',t.last_name) as nombre, t.release_date as anio_lanzamiento
FROM(SELECT *
    FROM (SELECT *
            FROM "unique".movie_actor
            INNER JOIN "unique".actor a on a.id = movie_actor.id_actor) as t2
    INNER JOIN "unique".movie m on m.id = t2.id_movie) as t
WHERE  t.description like '%Crocodile%' and t.description like '%Shark%'
ORDER BY nombre asc ;

--Consulta 5

SELECT t.Country, t.nombre,  t.contador, (t.contador/(SELECT sum(t.contador)
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
                )) as t;

--Consulta 6

WITH ciudad_pais_cont as(SELECT c2.name as pais,c.name as ciudad,count(c2.name) as contador_cliente
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
;


--Consulta 7

WITH rentid_ciudad_pais as (SELECT count(c2.name) as renta,c.name as ciudad,c2.name as pais
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
ORDER BY pais asc ;

--Consulta8

WITH rent_cat_country as (SELECT c2.name as pais, c3.name as categoria, count(c2.name) as renta
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
;

--Consulta 9

WITH rentid_ciudad_pais as (SELECT count(c2.name) as renta,c.name as ciudad,c2.name as pais
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
WHERE rentid_ciudad_pais.ciudad = 'Dayton');

--Consulta 10

WITH primera as (SELECT c2.name as pais, c.name as ciudad, c3.name as categoria, count(c3.name) as rentas
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
                    WHERE tb2.ciudad=tb1.ciudad) AND tb1.categoria='Horror';






