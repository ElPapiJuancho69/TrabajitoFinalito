import tkinter as tk

# Funciones de cálculo
def suma():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 + num2
    label_resultado.config(text="El resultado de la suma es: " + str(resultado))

def resta():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 - num2
    label_resultado.config(text="El resultado de la resta es: " + str(resultado))

def multiplicacion():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 * num2
    label_resultado.config(text="El resultado de la multiplicación es: " + str(resultado))

def division():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 != 0:
        resultado = num1 / num2
        label_resultado.config(text="El resultado de la división es: " + str(resultado))
    else:
        label_resultado.config(text="Error: No se puede dividir entre cero.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora minimalista - Hecho por: CEX")
ventana.geometry("300x300")
ventana.configure(bg="#ECECEC")

# Etiquetas
label_num1 = tk.Label(ventana, text="Primer número:", bg="#ECECEC")
label_num1.pack()

entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Segundo número:", bg="#ECECEC")
label_num2.pack()

entry_num2 = tk.Entry(ventana)
entry_num2.pack()

label_resultado = tk.Label(ventana, text="", bg="#ECECEC")
label_resultado.pack()

# Botones
button_suma = tk.Button(ventana, text="Suma", command=suma, bg="#CCCCCC", width=10)
button_suma.pack(pady=5)

button_resta = tk.Button(ventana, text="Resta", command=resta, bg="#CCCCCC", width=10)
button_resta.pack(pady=5)

button_multiplicacion = tk.Button(ventana, text="Multiplicación", command=multiplicacion, bg="#CCCCCC", width=10)
button_multiplicacion.pack(pady=5)

button_division = tk.Button(ventana, text="División", command=division, bg="#CCCCCC", width=10)
button_division.pack(pady=5)

ventana.mainloop()
