from Modelos.Resultados import Resultados
class ControladorResultados():
    def __init__(self):
         print("Creando ControladorResultados")
    def index(self):
         print("Listar todos los Resultados")
         unResultado = {
             "_id": "1",
             "numero_mesa": "123",
             "id_partido": "P1"

         }
         return [unResultado]

    def create(self,infoResultado):
         print("Crear un resultado")
         elResultado = Resultados(infoResultado)
         return elResultado.__dict__

    def show(self,id):
         print("Mostrando un resultado con id ",id)
         elResultado = {
             "_id": id,
             "numero_mesa": "123",
             "id_partido": "P1"
         }
         return elResultado

    def update(self,id,infoResultado):
         print("Actualizando resultados con id",id)
         elResultado = Resultados(infoResultado)
         return elResultado.__dict__

    def delete(self,id):
         print("Eliminando resulatdos con id ",id)
         return {"deleted_count": 1}