

""" Los valores ingresados por la funcion input seran string por eso deberemos transformarlos
en enteros, para ello utilizaremos la funcion int """
numero_uno = input("Ingrese un numero: ")

try:
    numero_uno = int(numero_uno)
except:
    numero_uno = "Es string"

if numero_uno == "Es string":
    print("Ingresaste mal un dato, solo valores numericos")
    exit()
numero_dos = input("Ingrese otro numero: ")

try:
    numero_dos = int(numero_dos)
except:
    numero_dos = "Es un string"

if numero_dos == "Es un string":
    print("Ingresaste mal un dato, solo valores numericos")
    exit()

simbolo = input("Ingrese un simbolo para realizar alguna operacion matematica: ")

if simbolo == '+':
    print('Suma',numero_uno + numero_dos)
elif simbolo == '-':
    print('Resta', numero_uno - numero_dos)
elif simbolo == '*':
    print('Multiplicacion', numero_uno * numero_dos)
elif simbolo == '/':
    print('Division', numero_uno / numero_dos)
else:
    print('Ninguno de los simbolos ingresados corresponde con una operacion matematica')