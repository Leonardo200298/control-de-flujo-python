dato = input("Ingrese un dato: ")

lista = ["Lucas", "Darren", "Aster", "pluto"]

#Esta linea verifica que el elemento que ingrese el usuario sea un valor del arreglo
if lista.count(dato) > 0:
    print("El dato " + dato + " aparece en la lista")
else:
    print("El dato " + dato + " no esta en la lista :(")
    