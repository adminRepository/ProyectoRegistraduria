from Modelos.Mesa import Mesa


class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todos las Mesas")
        unaMesa = {
            "numero": "123",
            "cantidad_inscritos": "600"
        }
        return [unaMesa]

    def create(self, infoMesa):
        print("Crear una Mesa")
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def show(self, numero):
        print("Mostrando un resultado con numero ", numero)
        laMesa = {
            "numero": numero,
            "cantidad_inscritos": "600"
        }
        return laMesa

    def update(self, numero, infoMesa):
        print("Actualizando mesa con numero", numero)
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def delete(self, numero):
        print("Eliminando mesa con numero ", numero)
        return {"deleted_count": 1}