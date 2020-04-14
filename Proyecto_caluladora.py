#Autor: Mirko Ramirez C.
#tkinter
import tkinter as tk
# Declarando los recursos que se van a utilizar en el programa
root = tk.Tk()
primer_numero=tk.StringVar()
segundo_numero=tk.StringVar()
fruta_agregada = tk.StringVar()
fruta_buscada = tk.StringVar()
fruta_comprada = tk.StringVar()
mensaje = tk.StringVar()

def suma():
    print('------Suma--------')
    a = int(primer_numero.get())
    b = int(segundo_numero.get())
    c=a+b
    mensaje.set(f'La suma de: {a} + {b}  = {c}')
    primer_numero.set('')
    segundo_numero.set('')
def resta():
    print('------Resta--------')
    a = int(primer_numero.get())
    b = int(segundo_numero.get())
    c = a - b
    mensaje.set(f'La resta de: {a} - {b}  = {c}')
    primer_numero.set('')
    segundo_numero.set('')
def multiplicacion():
    print('------Multipliccion--------')
    a = int(primer_numero.get())
    b = int(segundo_numero.get())
    c = a * b
    mensaje.set(f'La multiplicacion de: {a} * {b}  = {c}')
    primer_numero.set('')
    segundo_numero.set('')
def division():
    print('------Division--------')
    a = int(primer_numero.get())
    b = int(segundo_numero.get())
    c = a / b
    d = a // b
    e = a % b
    mensaje.set(f'La division de: {a} / {b}  = {c}\nEl cociente es:  {d}\nEl resto:        {e}')
    primer_numero.set('')
    segundo_numero.set('')
root.geometry('800x500')
root.title('...Calculadora...')
root.configure(bg="#AF3D1E")
tk.Label(root, text='Operaciones basicas', bg="#AF3D1E", fg='#110502', font=('Helvetica', 32)).place(x=250, y=30)
#Ingresar Numeros
tk.Label(root, text='Ingrese numero 1:', bg="#AF3D1E", fg='#fff', font=('Helvetica', 24)).place(x=30, y=100)
tk.Entry(root, justify='center', textvariable=primer_numero).place(x=340, y=110)
tk.Label(root, text='Ingrese numero 2:', bg="#AF3D1E", fg='#fff', font=('Helvetica', 24)).place(x=30, y=140)
tk.Entry(root, justify='center', textvariable=segundo_numero).place(x=340, y=150)
#Suma
tk.Button(root, text='Sumar (+)', bd=10, command=suma).place(x=100, y=200)

#Resta
tk.Button(root, text='Restar (-)', bd=10, command=resta).place(x=250, y=200)

#Multiplicacion
tk.Button(root, text='Multiplicar (x)', bd=10, command=multiplicacion).place(x=400, y=200)

#Division
tk.Button(root, text='Dividir (/)', bd=10, command=division).place(x=550, y=200)

tk.Label(root, textvariable=mensaje, bg="#AF3D1E", fg='white', font=('', 24)).place(x=200, y=280)
tk.Button(root, text='Salir', bd=20, command=root.destroy).place(x=350, y=420)

root.mainloop()
