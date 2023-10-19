from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa


class ControladorMesa():
    def __init__(self):
        # Se crea una instancia del RepositorioMesa para interactuar con la base de datos
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        # Retorna todas las mesas existentes en la base de datos
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        # Crea un nuevo objeto mesa a partir de la información recibida
        nuevaMesa = Mesa(infoMesa)

        # Guarda la nueva mesa en la base de datos utilizando el repositorio
        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        # Obtiene una mesa por su ID desde la base de datos utilizando el repositorio
        laMesa = Mesa(self.repositorioMesa.findById(id))

        # Retorna los atributos de la mesa como un diccionario
        return laMesa.__dict__

    def update(self, id, infoMesa):
        # Obtiene la mesa actual por su ID desde la base de datos utilizando el repositorio
        mesaActual = Mesa(self.repositorioMesa.findById(id))

        # Actualiza los atributos del departamento con la información recibida
        mesaActual.numero = infoMesa["numero"]
        mesaActual.cantidad_inscritors = infoMesa["cantidad_inscritos"]


        # Guarda los cambios de la mesa actualizado en la base de datos utilizando el repositorio
        return self.repositorioMesa.save(mesaActual)

    def delete(self, id):
        # Elimina una mesa por su ID desde la base de datos utilizando el repositorio
        return self.repositorioMesa.delete(id)








