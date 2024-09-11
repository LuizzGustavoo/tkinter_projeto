import tkinter as tk

def open_login_comunidade(root):
    for widget in root.winfo_children():
        widget.destroy()

    box = tk.Frame(root, bg="black", bd=10)
    box.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=300, height=300)

    tk.Label(box, text="Login Comunidade", font=("Bebas Neue", 20), fg="white", bg="black").pack(pady=10)
    tk.Label(box, text="CPF:", fg="white", bg="black").pack(pady=5)
    entry_cpf = tk.Entry(box)
    entry_cpf.pack(pady=5)
    
    tk.Label(box, text="Senha:", fg="white", bg="black").pack(pady=5)
    entry_senha = tk.Entry(box, show="*")
    entry_senha.pack(pady=5)

    tk.Button(box, text="Login", command=lambda: print("Autenticando Comunidade..."), bg="#568915", fg="white").pack(pady=10)

    tk.Button(box, text="Voltar", command=lambda: create_home(root), bg="#568915", fg="white").pack(pady=10)

def create_home(root):
    from home import create_home
    create_home()
