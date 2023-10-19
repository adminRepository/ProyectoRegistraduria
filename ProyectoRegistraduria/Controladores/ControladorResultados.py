from Repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidatos import Candidatos
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato


class ControladorResultados():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        return self.repositorioResultado.findAll()

    """ 
    Asignacion  Candidato y Mesa a Resultado 
    
    """
    def create(self , infoResultado, id_candidato, id_mesa):
        nuevoResultado = Resultado(infoResultado)
        elCandidato = Candidatos(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.candidato = elCandidato
        nuevoResultado.mesa = laMesa
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    """
    Modificacion de Resultados de Candidato y mesa 
    """
    def update(self, id, infoResultado, id_candidato, id_mesa):
        # Obtiene la mesa actual por su ID desde la base de datos utilizando el repositorio
        resultadoActual = Resultado(self.repositorioResultado.findById(id))
        # Actualiza los atributos del departamento con la información recibida
        resultadoActual.numero_mesa = infoResultado["numero_mesa"]
        resultadoActual.id_partido = infoResultado["id_partido"]
        elCandidato= Candidatos(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        resultadoActual.candidato = elCandidato
        resultadoActual.mesa = laMesa
        # Guarda los cambios de la mesa actualizado en la base de datos utilizando el repositorio
        return self.repositorioResultado.save(resultadoActual)

    def delete(self, id):
        return self.repositorioResultado.delete(id)