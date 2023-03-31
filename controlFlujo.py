perfiles = {
    "usuario1":{
        "nombre":"roger",
        "apellido":"waters",
        "edad":23
    },
        "usuario2":{
        "nombre":"frank",
        "apellido":"cuesta",
        "edad":21
    },    "usuario3":{
        "nombre":"Lionel",
        "apellido":"Rijak",
        "edad":26
    }
}

""" Probamos metodo len que es para saber la longitud de los diccionarios """
""" if len(perfiles)>2:
    print("El diccionario es mayor a dos")
 """

if (perfiles["usuario1"]["edad"] > perfiles["usuario2"]["edad"]):
    print("La edad del usuario 1 es mayor a edad del usuario 2")
else:
    print("Ninguna de las dos condiciones anteriores es verdad")



""" Agregar elemento a un diccionario anidado """
""" perfiles["usuario4"] = {
    "nombre":"David",
    "apellido":"trezeguet",
    "edad":31
}
print(perfiles) """