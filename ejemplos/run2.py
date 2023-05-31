"""
Paula Montaño
"""
# Crear dos objetos de la clase 02
from mis_clases import Portatil

# objeto 01
# crear
portatil1 = Portatil("blanca", "hp", 2, 750.99)

# Presentar objeto; usar el método __st__
portatil1.__str__()



# objeto 02
# crear ingresando valores por teclado

color = input("Ingrese el color de su portatil: ")
marca = input("Ingrese la la marca de su portatil: ")
tiempo_duracion = int(input("Ingrese el tiempo de duracion de su portatil: "))
precio = float(input("Ingrese el precio de su portatil: "))

portatil2 = Portatil(color, marca, tiempo_duracion, precio)

# Presentar objeto; usar el método __st__
portatil2.__str__()

