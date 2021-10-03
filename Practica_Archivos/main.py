from re import T
from sqlalchemy.sql.expression import table
from methods import caso1, caso10, caso2, caso3, caso4, caso5, caso6, caso7, caso8, caso9, dropER, readCSV,generarER, truncateTemp
from flask import Flask
from sqlalchemy.sql import text

import csv
import json
import sqlalchemy as db
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine('postgresql://postgres:contra@localhost:5432/blackbuster')


@app.route('/')
def primercomandito():  

    return 'Bienvenido al inicio'

@app.route('/temp')
def temp():
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM "Unique".cliente')
        clientes = []
        stringmientras= ''
        for row in rs:
            clientes.append(row)
        json_info = json.dumps(clientes)
    return json_info


@app.route('/consulta1')
def consult1():
    table = caso1()
    tablita = []
    for row in table:
        biblio = {
            "Cantidad":row[0]
        }
        tablita.append(biblio)
    json_info = json.dumps(tablita)
    return json_info

@app.route('/consulta2')
def consult2():
    table = caso2()
    tablit = []
    for row in table:
        biblio = {
            'Nombre':row[0],
            'Compras':row[1],
            'Monto Total':float(row[2])
        }
        tablit.append(biblio)
    json_info = json.dumps(tablit)
    return json_info   

@app.route('/consulta3')
def consult3():
    table=caso3()
    tablit = []
    for row in table:
        biblio = {
            'Nombre':row[0]
        }
        tablit.append(biblio)
    json_info = json.dumps(tablit)
    return json_info

@app.route('/consulta4')
def consult4():
    table = caso4()
    tablit = []
    for row in table:
        biblio = {
            'Nombre':str(row[0]),
            'Anio de Lanzamietno':int(row[1])
        }
        tablit.append(biblio)
    json_info = json.dumps(tablit)
    return json_info

@app.route('/consulta5')
def consult5():
    table = caso5()
    tablit = []
    for row in table:
        biblio = {
            'Pais':row[0],
            'Ciudad':row[1],
            'Contador': row[2],
            'Porcentaje': float(row[3])
        }
        tablit.append(biblio)
    json_info = json.dumps(tablit)
    return json_info

@app.route('/consulta6')
def consult6():
    table = caso6()
    tablit = []
    for row in table:
        biblio = {
            'Pais':row[0],
            'Ciudad':row[1],
            'Total de Clientes': row[2],
            'Porcentaje': float(row[3])
        }
        tablit.append(biblio)
    json_info = json.dumps(tablit)
    return json_info

@app.route('/consulta7')
def consult7():
    table = caso7()
    tablit = []
    for row in table:
        biblio = {
            'Pais':row[0],
            'Ciudad':row[1],
            'Promedio':float(row[2])
        }
        tablit.append(biblio)
    json_info = json.dumps(tablit)
    return json_info

@app.route('/consulta8')
def consult8():
    table = caso8()
    tablit = []
    for row in table:
        biblio = {
            'Pais':row[0],
            'Porcentaje':float(row[1])
        }
        tablit.append(biblio)
    json_info = json.dumps(tablit)
    return json_info

@app.route('/consulta9')
def consult9():
    table = caso9()
    tablit = []
    for row in table:
        biblio = {
            'Renta':row[0],
            'Ciudad':row[1],
            'Pais':row[2]
        }
        tablit.append(biblio)
    json_info = json.dumps(tablit)
    return json_info

@app.route('/consulta10')
def consult10():
    table = caso10()
    tablit = []
    for row in table:
        biblio = {
            'Pais':row[0],
            'Ciudad':row[1],
            'Categoria':row[2],
            'Rentas': row[3]
        }
        tablit.append(biblio)
    json_info = json.dumps(tablit)
    return json_info

@app.route('/eliminarTemporal')
def elimnartemp():
    truncateTemp()
    return 'Elimino registro de la temporal'

@app.route('/eliminarModelo')
def eliminarER():
    dropER()
    return 'Elimino el Modelo'

@app.route('/cargarTemporal')
def cargartemp():
    readCSV()
    return 'holis'

@app.route('/cargarModelo')
def cargarER():
    generarER()
    return 'Cargo el Modelo'
    
    
    
    