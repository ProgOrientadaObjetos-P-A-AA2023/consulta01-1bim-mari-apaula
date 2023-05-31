"""
Maria Paula Montaño 
"""
# Crear dos objetos de la clase 01
from mis_clases import Perro

# objeto 01
# crear
p1 = Perro("Flofy", 1)

# Presentar objeto; usar el método __st__
p1.__str__()


# objeto 02
# crear ingresando valores por teclado


nom = input("Ingrese el nombre de su perro:\n")

edad = int(input("Ingrese la edad de su perro:\n"))

p2 = Perro(nom, edad)

# Presentar objeto; usar el método __st__
p2.__str__()
