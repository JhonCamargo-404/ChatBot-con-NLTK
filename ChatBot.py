import nltk
from nltk.corpus import gutenberg
import tkinter as tk
from tkinter import simpledialog, messagebox

nltk.download('gutenberg')

def obtener_titulos():
    return [titulo.replace('.txt', '').replace('-', ' ').title() for titulo in gutenberg.fileids()]

def obtener_autor(titulo):
    for fileid in gutenberg.fileids():
        if titulo.lower() in fileid.lower():
            return gutenberg.raw(fileid).split('\n')[0]
    return "No se encontró el título en el corpus de Gutenberg."

def obtener_resumen(titulo):
    for fileid in gutenberg.fileids():
        if titulo.lower() in fileid.lower():
            text = gutenberg.raw(fileid)
            return ' '.join(nltk.sent_tokenize(text)[:2])
    return "No se encontró el título en el corpus de Gutenberg."

def mostrar_titulos():
    titulos = obtener_titulos()
    lista_titulos.delete(0, tk.END)
    for titulo in titulos:
        lista_titulos.insert(tk.END, titulo)

def obtener_autor_interfaz():
    titulo_input = simpledialog.askstring("Obtener autor", "Ingrese el nombre del libro")
    autor = obtener_autor(titulo_input)
    messagebox.showinfo("Autor del libro", autor)

def obtener_resumen_interfaz():
    titulo_input = simpledialog.askstring("Obtener resumen", "Ingrese el nombre del libro")
    resumen = obtener_resumen(titulo_input)
    messagebox.showinfo("Resumen del libro", resumen)

root = tk.Tk()
root.title("Consulta de libros de Gutenberg")

label_titulos = tk.Label(root, text="Títulos:")
label_titulos.grid(row=0, column=0, padx=10, pady=10)

lista_titulos = tk.Listbox(root, height=10, width=40)
lista_titulos.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

button_obtener_titulos = tk.Button(root, text="Mostrar títulos", command=mostrar_titulos)
button_obtener_titulos.grid(row=3, column=1, pady=10)

button_obtener_autor = tk.Button(root, text="Obtener autor del libro", command=obtener_autor_interfaz)
button_obtener_autor.grid(row=4, column=0, padx=10, pady=10)

button_obtener_resumen = tk.Button(root, text="Obtener resumen del libro", command=obtener_resumen_interfaz)
button_obtener_resumen.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
