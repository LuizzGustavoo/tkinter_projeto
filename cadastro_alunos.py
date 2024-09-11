import tkinter as tk

def open_cadastro_alunos(root):
    for widget in root.winfo_children():
        widget.destroy()

    box = tk.Frame(root, bg="black", bd=10)
    box.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=300, height=400)

    tk.Label(box, text="Cadastro Alunos", font=("Bebas Neue", 20), fg="white", bg="black").pack(pady=10)

    tk.Label(box, text="Nome:", fg="white", bg="black").pack(pady=5)
    entry_nome = tk.Entry(box)
    entry_nome.pack(pady=5)

    tk.Label(box, text="Matrícula:", fg="white", bg="black").pack(pady=5)
    entry_matricula = tk.Entry(box)
    entry_matricula.pack(pady=5)

    tk.Label(box, text="Senha:", fg="white", bg="black").pack(pady=5)
    entry_senha = tk.Entry(box, show="*")
    entry_senha.pack(pady=5)

    tk.Button(box, text="Cadastrar", command=lambda: print("Aluno cadastrado!"), bg="#568915", fg="white").pack(pady=10)

    tk.Button(box, text="Voltar", command=lambda: create_home(root), bg="#568915", fg="white").pack(pady=10)

def create_home(root):
    from cadastro import open_cadastro
    open_cadastro(root)
