import csv
from sqlalchemy.sql import text
from main import engine


def readCSV():
    rows = []
    with open('/home/josee/Documents/Archivos/Practica/BlockbusterData.csv', "r") as archivo:
        next(archivo,None)
        for linea in archivo:
            linea = linea.rstrip()
            lista = linea.split(",")
            for x in range(len(lista)):
                if lista[x] == '-':
                    lista[x]=None
                if lista[2] == 'Si':
                    lista[2] = True
                elif lista[2] == 'No':
                    lista[2] = False
                if lista[15] =='Si':
                    lista[15] = True
                elif lista[15] == 'No':
                    lista[15] = False
        meterEnLaTemp(linea)
            
    return rows


def meterEnLaTemp(row):
    statement = text("""INSERT INTO "unique".Temporal VALUES(:NOMBRE_CLIENTE,
                     :CORREO_CLIENTE, :CLIENTE_ACTIVO,:FECHA_CREACION, :TIENDA_PREFERIDA,
                     :DIRECCION_CLIENTE, :CODIGO_POSTAL, :CIUDAD_CLIENTE, :PAIS_CLIENTE,
                     :FECHA_RENTA, :FECHA_RETORNO, :MONTO_A_PAGAR, :FECHA_PAGO, :NOMBRE_EMPLEADO,
                     :CORREO_EMPLEADO, :EMPLEADO_ACTIVO, :TIENDA_EMPLEADO, :USUARIO_EMPLEADO,
                     :CONTRASENA_EMPLEADO, :DIRECCION_EMPLEADO, :CODIGO_POSTAL_EMPLEADO,
                     :CIUDAD_EMPLEADO, :PAIS_EMPLEADO, :NOMBRE_TIENDA, :ENCARGADO_TIENDA,
                     :DIRECCION_TIENDA, :CODIGO_POSTAL_TIENDA, :CIUDAD_TIENDA, :PAIS_TIENDA,
                     :TIENDA_PELICULA, :NOMBRE_PELICULA, :DESCRIPCION_PELICULA, :ANO_LANZAMIENTO,
                     :DIAS_RENTA, :COSTO_RENTA, :DURACION, :COSTO_POR_DANO, :CLASIFICACION,
                     :LENGUAJE_PELICULA, :CATEGORIA_PELICULA, :ACTOR_PELICULA)""")    
    with engine.connect() as con:
        dato = {
                "NOMBRE_CLIENTE": row[0],
 	            "CORREO_CLIENTE": row[1],
 	            "CLIENTE_ACTIVO": row[2],
 	            "FECHA_CREACION" : row[3],
 	            "TIENDA_PREFERIDA": row[4],
 	            "DIRECCION_CLIENTE" : row[5],
 	            "CODIGO_POSTAL":int(row[6]) if row[6]!= None else None,
 	            "CIUDAD_CLIENTE": row[7],
 	            "PAIS_CLIENTE":row[8],
 	            "FECHA_RENTA":row[9],
 	            "FECHA_RETORNO":row[10],
 	            "MONTO_A_PAGAR": float(row[11]) if row[11]!= None else None,
 	            "FECHA_PAGO":row[12],
 	            "NOMBRE_EMPLEADO":row[13],
 	            "CORREO_EMPLEADO":row[14],
 	            "EMPLEADO_ACTIVO":row[15],
 	            "TIENDA_EMPLEADO":row[16],
 	            "USUARIO_EMPLEADO":row[17],
 	            "CONTRASENA_EMPLEADO":row[18],
 	            "DIRECCION_EMPLEADO":row[19],
 	            "CODIGO_POSTAL_EMPLEADO":int(row[20]) if row[20]!= None else None,
 	            "CIUDAD_EMPLEADO":row[21],
 	            "PAIS_EMPLEADO":row[22],
 	            "NOMBRE_TIENDA":row[23],
 	            "ENCARGADO_TIENDA":row[24],
 	            "DIRECCION_TIENDA":row[25],
 	            "CODIGO_POSTAL_TIENDA":row[26],
 	            "CIUDAD_TIENDA":row[27],
 	            "PAIS_TIENDA":row[28],
 	            "TIENDA_PELICULA":row[29],
 	            "NOMBRE_PELICULA":row[30],
 	            "DESCRIPCION_PELICULA":row[31],
 	            "ANO_LANZAMIENTO":row[32],
 	            "DIAS_RENTA":int(row[33]) if row[33]!= None else None,
 	            "COSTO_RENTA":float(row[34]) if row[34]!= None else None,
 	            "DURACION":int(row[35]) if row[35]!= None else None,
 	            "COSTO_POR_DANO":float(row[36]) if row[36]!= None else None,
 	            "CLASIFICACION":row[37],
 	            "LENGUAJE_PELICULA":row[38],
 	            "CATEGORIA_PELICULA":row[39],
 	            "ACTOR_PELICULA":row[40]
            }
        con.execute(statement, **dato)
        
    
            