import tkinter as tk

def open_cadastro_comunidade(root):
    for widget in root.winfo_children():
        widget.destroy()

    box = tk.Frame(root, bg="black", bd=10)
    box.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=300, height=400)

    tk.Label(box, text="Cadastro Comunidade", font=("Bebas Neue", 20), fg="white", bg="black").pack(pady=10)

    tk.Label(box, text="Nome:", fg="white", bg="black").pack(pady=5)
    entry_nome = tk.Entry(box)
    entry_nome.pack(pady=5)

    tk.Label(box, text="E-mail:", fg="white", bg="black").pack(pady=5)
    entry_email = tk.Entry(box)
    entry_email.pack(pady=5)

    tk.Label(box, text="CPF:", fg="white", bg="black").pack(pady=5)
    entry_cpf = tk.Entry(box)
    entry_cpf.pack(pady=5)

    tk.Label(box, text="Telefone:", fg="white", bg="black").pack(pady=5)
    entry_telefone = tk.Entry(box)
    entry_telefone.pack(pady=5)

    tk.Button(box, text="Cadastrar", command=lambda: print("Comunidade cadastrada!"), bg="#568915", fg="white").pack(pady=10)

    tk.Button(box, text="Voltar", command=lambda: create_home(root), bg="#568915", fg="white").pack(pady=10)

def create_home(root):
    from cadastro import open_cadastro
    open_cadastro(root)
