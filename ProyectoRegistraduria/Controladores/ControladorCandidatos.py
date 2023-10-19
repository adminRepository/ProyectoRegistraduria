from Modelos.Candidatos import Candidatos
from Repositorios.RepositorioCandidato import RepositorioCandidato
class ControladorCandidatos():
    def __init__(self):
        # Se crea una instancia del RepositorioEstudiante para interactuar con la base de datos
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        # Retorna todos los estudiantes existentes en la base de datos
        return self.repositorioCandidato.findAll()
    def create(self, infoCandidato):
        # Crea un nuevo objeto Estudiante a partir de la información recibida
        nuevoCandidato = Candidatos(infoCandidato)

        # Guarda el nuevo estudiante en la base de datos utilizando el repositorio
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        # Obtiene un estudiante por su ID desde la base de datos utilizando el repositorio
        elCandidato = Candidatos(self.repositorioCandidato.findById(id))

        # Retorna los atributos del estudiante como un diccionario
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        # Obtiene el estudiante actual por su ID desde la base de datos utilizando el repositorio
        candidatoActual = Candidatos(self.repositorioCandidato.findById(id))
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.partido = infoCandidato["partido"]

        # Guarda los cambios del estudiante actualizado en la base de datos utilizando el repositorio
        return self.repositorioCandidato.save(candidatoActual)

    def delete(self, id):
        # Elimina un estudiante por su ID desde la base de datos utilizando el repositorio
        return self.repositorioCandidato.delete(id)