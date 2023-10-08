from Repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Resultado import Resultado


class ControladorResultados():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()

    def index(self):
        return self.repositorioResultado.findAll()

    def create(self, infoDepartamento):
        nuevoResultado = Resultado(infoDepartamento)
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    def update(self, id, infoResultado):
        # Obtiene la mesa actual por su ID desde la base de datos utilizando el repositorio
        resultadoActual = Resultado(self.repositorioResultado.findById(id))

        # Actualiza los atributos del departamento con la información recibida
        resultadoActual.numero_mesa = infoResultado["numero_mesa"]
        resultadoActual.id_partido = infoResultado["id_partido"]

        # Guarda los cambios de la mesa actualizado en la base de datos utilizando el repositorio
        return self.repositorioResultado.save(resultadoActual)

    def delete(self, id):
        return self.repositorioResultado.delete(id)