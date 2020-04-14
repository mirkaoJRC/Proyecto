#Autor: Mirko  Ramirez C.
menu='''
---------------------------
--------Calculadora--------
---------------------------
Menu:
1- Suma
2- Resta
3- Multiplicacion
4- Division
5- Salir
'''

def suma():
    print('------Suma--------')
    a = int(input('Ingrese primer numero: '))
    b = int(input('Ingrese segundo numero: '))
    c=a+b
    print(f'La suma de: {a} + {b}  = {c}')
def resta():
    print('------Resta--------')
    a = int(input('Ingrese primer numero: '))
    b = int(input('Ingrese segundo numero: '))
    c = a - b
    print(f'La resta de: {a} - {b}  = {c}')
def multiplicacion():
    print('------Multipliccion--------')
    a = int(input('Ingrese primer numero: '))
    b = int(input('Ingrese segundo numero: '))
    c = a * b
    print(f'La multiplicacion de: {a} * {b}  = {c}')
def division():
    print('------Division--------')
    a = int(input('Ingrese primer numero: '))
    b = int(input('Ingrese segundo numero: '))
    c = a / b
    d = a // b
    e = a % b
    print(f'La division de: {a} / {b}  = {c}')
    print(f'El cociente es:  {d}')
    print(f'El resto:        {e}')
sw=True
while sw:
    print(menu)
    opc=int(input('Seleccione una opcion para ejecutar: '))

    if opc == 1:
        suma()
    elif opc == 2:
        resta()
    elif opc == 3:
        multiplicacion()
    elif opc == 4:
        division()
    elif opc == 5:
        sw=False
    else:
        print('Opcion no valida...\nVuelva a introducir la opcion...')
