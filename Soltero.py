from Concursante import Concursante
import time

class Soltero(Concursante):
    def __init__(self, nombre, edad, profesion, procedencia):
        super().__init__(nombre, edad, profesion, procedencia)
        self._ligues = []

    def __str__(self):
        return f"\n{self._nombre} ha venido a enamorarse a la isla de las tentaciones. Tiene {self._edad}, viene de {self._procedencia} y su trbajo es {self._profesion}\n"

    
    def addLigue(self, tentado):
        self._ligues.append(tentado)


    def ligarCon(self, tentado):
        self.addLigue(tentado)
        print(f"{self._nombre} ha conectado completamente con {tentado._nombre}. Esta es su {len(self._ligues)}a conquista")
        time.sleep(1)

    
    def hablar(self, mensaje):
        target = " "
        if len(self._ligues) > 0:
            target = f" (que ha conquistado a {self._ligues[-1]._nombre}) "
        print(f"\n[{self._nombre.upper()}]{target}: {mensaje}\n")
        time.sleep(1)

