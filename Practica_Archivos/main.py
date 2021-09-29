from methods import readCSV
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
    infos = []
    infos = readCSV()
    print(infos[89470])
    #app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:contra@localhost:5432/blackbuster"

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
    return 'Es la consulta 1'

@app.route('/consulta2')
def consult2():
    return 'Es la consulta 2'    

@app.route('/consulta3')
def consult3():
    return 'Es la consulta 3'

@app.route('/consulta4')
def consult4():
    return 'Es la consulta 4'

@app.route('/consulta5')
def consult5():
    return 'Es la consulta 5'

@app.route('/consulta6')
def consult6():
    return 'Es la consulta 6'

@app.route('/consulta7')
def consult7():
    return 'Es la consulta 7'

@app.route('/consulta8')
def consult8():
    return 'Es la consulta 8'

@app.route('/consulta9')
def consult9():
    return 'Es la consulta 9'

@app.route('/consulta10')
def consult10():
    return 'Es la consulta 10'

@app.route('/eliminarTemporal')
def elimnartemp():
    return 'Elimino el temporal'

@app.route('/eliminarModelo')
def eliminarER():
    return 'Elimino el Modelo'

@app.route('/cargarTemporal')
def cargartemp():
    infos = []
    infos = readCSV()
    

    
    return 'holis'

@app.route('/cargarModelo')
def cargarER():
    return 'Cargo el Modelo'
    
    
    
    