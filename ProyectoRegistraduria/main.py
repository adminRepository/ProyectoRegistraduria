from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve


from Controladores.ControladorCandidatos import ControladorCandidatos
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultados import ControladorResultados


app = Flask(__name__)
cors = CORS(app)

miControladorMesa = ControladorMesa()

miControladorCandidatos = ControladorCandidatos()
miControladorResultados=ControladorResultados()
miControladorPartido= ControladorPartido()
@app.route("/partidos",methods=['GET'])
def getPartido():
    json=miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['GET'])
def getPartidos(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)

@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = miControladorCandidatos.index()
    return jsonify(json)

    
@app.route("/candidato", methods=['POST'])
def crearCandidato():
    data = request.get_json()    
    json = miControladorCandidatos.create(data)
    return jsonify(json)

@app.route("/candidato/<string:id>", methods=['GET'])
def getCandidato(id):
    json = miControladorCandidatos.show(id)
    return jsonify(json)

@app.route("/candidato/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidatos.update(id, data)
    return jsonify(json)

@app.route("/candidato/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidatos.delete(id)
    return jsonify(json)

@app.route("/candidato/<string:id>/partido/<string:id_partido>", methods=['PUT'])
def asignarPartidoa(id,id_partido):
    json=miControladorCandidatos.asignarPartido(id, id_partido)
    return  jsonify(json)




@app.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorResultados.index()
    return jsonify(json)

@app.route("/resultados",methods=['POST'])
def crearResultados():
    data = request.get_json()
    json=miControladorResultados.create(data)
    return jsonify(json)

@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultados.show(id)
    return jsonify(json)

@app.route("/resultados/<string:id>",methods=['PUT'])
def modificarResultados(id):
    data = request.get_json()
    json=miControladorResultados.update(id,data)
    return jsonify(json)

@app.route("/resultados/<string:id>",methods=['DELETE'])
def eliminarResultados(id):
    json=miControladorResultados.delete(id)
    return jsonify(json)

@app.route("/mesa", methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesa/<string:id>", methods=['GET'])
def getMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)    
    
@app.route("/mesa", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)
    
@app.route("/mesa/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)
    
@app.route("/mesa/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)

"--------------------------------------------------------------"


# Servicio que el servidor ofrecerá, y este consiste en retornar un JSON el cual
# tiene un mensaje que dice que el servidor está corriendo.
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)


# Método leer el archivo de configuración del proyecto,
# retornará un diccionario el cual posee la información dentro del
# JSON y se podrá acceder a los atributos necesarios.
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()                   #Se asigna lo que retorna el metodo a la variable dataConfig
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))



# Se crea la instancia del servidor con la url del backend y puerto especificado
# en el archivo de configuración.
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])




