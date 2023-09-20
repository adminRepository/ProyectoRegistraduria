from Modelos.Candidatos import Candidatos
class ControladorCandidatos():
    def init (self):
         print("Creando ControladorCandidato")
    def index(self):
         print ("Listar todos los Candidatos")
         unCandidato = {
             "_id": "1" ,
             "nombre": " Juan Pablo ",
             "apellido":"Quinonez",
             "cedula":"12345678",
             "partido":"ColombiaBuenaFup"
         }
         return [unCandidato]

    def create(self,infoCandidato):
         print("Crear un Candidato")
         elCandidato = Candidato(infoCandidato)
         return elCandidato.dict

    def show(self,id):
         print("Mostrando un Candidato con id ",id)
         elCandidato = {
             "_id": id,
             "nombre": " Juan Pablo ",
             "apellido": "Quinonez",
             "cedula": "12345678",
             "partido": "ColombiaBuenaFup"
         }
         return elCandidato

    def update(self,id,infoCandidato):
         print("Actualizando Candidato con id",id)
         elCandidato = Candidato (infoCandidato)
         return elCandidato.dict

    def delete(self,id):
         print("Eliminando Candidato con id ",id)
         return {"deleted_count": 1}
