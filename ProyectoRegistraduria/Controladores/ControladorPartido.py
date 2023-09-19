from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")

    def index(self):
        print("Listar todos los Partidos")
        unPartido={
            "_id": "abc50",
            "nombre": "cambio Radical",
            "lema": "Juntos somos el cambio"
        }
        return [unPartido]


    def create(self,infoPartido):
        print("Crear un Partido")
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def show(self,id):
        print("Mostrando un Partido con id ", id)
        elPartido = {
            "_id": "abc50",
            "nombre": "cambio Radical",
            "lema": "Juntos somos el cambio"

        }
        return elPartido

    def update(self, id,infoPartido):
        print("Actualizando partido con id",id)
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def delete(self, id):
        print("Elimiando Partido con id ", id)
        return {"deleted_count": 1}