"""
Paula Montaño
"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Perro:

    def __init__(self, nom, edad):
        self.nom = nom
        self.edad = edad

    def __str__(self):
        if self.edad > 1:
            print(self.nom, "ya es un adulto.")
        else:
            print(self.nom, "aún es un cachorro.")



# clase 02

class Portatil:

    def __init__(self, color, marca, tiempo_duracion, precio):
        self.color = color
        self.marca = marca
        self.tiempo_duracion = tiempo_duracion
        self.precio = precio


    def __str__(self):
        if self.tiempo_duracion >= 3:
            msj = "necesita un revicion de bateria"
        else:
            msj = "aún funiona bien"

        informe= "La portatil {} de color {} con un tiempo de duracíón de {} años, {}"\
            .format(self.marca,
                    self.color,
                    self.tiempo_duracion,
                    msj)
        print(informe)
