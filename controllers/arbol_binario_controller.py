
from .templates.arbol_controller_template import ArbolBinarioControllerTemplate


class ArbolBinarioController(ArbolBinarioControllerTemplate):
    def __init__(self, model, view):
        super().__init__(model, view)

    def insertar_izquierda(self, dato, padre):
        try:
            informacion_arbol = self.model.insertar_izquierda(dato, padre)
            self.view.mostrar_arbol(informacion_arbol)

        except Exception as e:
            print("Error:", e)

    def insertar_derecha(self, dato, padre):
        try:
            informacion_arbol = self.model.insertar_derecha(dato, padre)
            self.view.mostrar_arbol(informacion_arbol)

        except Exception as e:
            print("Error:", e)

    def eliminar(self, nombre):
        try:
            # Intentamos mostrar la información
            informacion_cola = self.model.eliminar(nombre)
            self.view.actualizar_caja_opciones(informacion_cola)

        except Exception as e:
            print("Error: ", e)

    def remove(self):
        try:
            # Intentamos mostrar la información
            informacion_cola = self.model.dequeue()
            self.view.actualizar(informacion_cola)

        except Exception as e:
            print(e)