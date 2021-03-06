from particula import Particula
import json

# Administrador de Particulas

class Particulas:
    def __init__(self):
        self.__particulas = [] # Lista
    
    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
    
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
    
    def __str__(self):
        return "".join(
            str(particula) + "\n" for particula in self.__particulas
        )
    
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, "w") as archivo:
                Lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(Lista, archivo, indent=5)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, "r") as archivo:
                Lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in Lista]
            return 1
        except:
            return 0