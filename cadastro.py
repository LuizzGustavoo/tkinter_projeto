import tkinter as tk
from cadastro_comunidade import open_cadastro_comunidade
from cadastro_alunos import open_cadastro_alunos

def open_cadastro(root):
    for widget in root.winfo_children():
        widget.destroy()

    box = tk.Frame(root, bg="black", bd=10)
    box.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=300, height=300)

    tk.Label(box, text="Escolha o Tipo de Cadastro", font=("Bebas Neue", 20), fg="white", bg="black").pack(pady=10)

    tk.Button(box, text="Cadastro Comunidade", command=lambda: open_cadastro_comunidade(root), bg="#568915", fg="white").pack(pady=10)
    tk.Button(box, text="Cadastro Alunos", command=lambda: open_cadastro_alunos(root), bg="#568915", fg="white").pack(pady=10)

    tk.Button(box, text="Voltar", command=lambda: create_home(root), bg="#568915", fg="white").pack(pady=10)

def create_home(root):
    from home import create_home
    create_home()
