from abc import ABCMeta
from abc import abstractmethod


class Concursante(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, nombre, edad, profesion, procedencia):
        self._nombre = nombre
        self._edad = edad
        self._profesion = profesion
        self._procedencia = procedencia    
    #   self.abtributo -> publico
    #   self._atributo -> protegido
    #   self.__atributo -> privado

    def setEdad(self, edad):
        if type(edad) in int:
            self._edad = edad

    def presentarse(self):
            print(self)
            
    @abstractmethod
    def ligarCon(self, concursante): ...


    @abstractmethod
    def hablar(self, mensaje): ...

    #GETTERS AND SETTERS
    def getNombre(self):
        return self._nombre


    def getEdad(self):
        return self._edad


    def getProfesion(self):
        return self._profesion


    def getProcedencia(self):
        return self._procedencia

    