from Concursante import Concursante
import time


class Tentado(Concursante):
    def __init__(self, nombre, edad, profesion, procedencia):
        super().__init__(nombre, edad, profesion, procedencia)
        self._inifidelidades = []
        self._pareja = None

    def __str__(self):
        return f"\n{self._nombre} es la pareja de {self._pareja._nombre}. Tiene {self._edad} años, viene de {self._procedencia} y su trabajo es {self._profesion}\n"


    def setPareja(self, pareja):
        self._pareja = pareja


    def addInfidelidad(self, soltero):
        self._inifidelidades.append(soltero)
    

    def ligarCon(self, soltero):
        self.addInfidelidad(soltero)
        soltero.addLigue(self)
        print(f"¡NIIIIIII NOOOOOO NIIIIII NOOO! SUENA LA ALARMA. {self._nombre} ha sido infiel a {self._pareja._nombre} con {soltero._nombre}")
        time.sleep(1)


    def hablar(self, mensaje):
        print(f"\n[{self._nombre.upper()}] (pareja de {self._pareja._nombre}): {mensaje}\n")