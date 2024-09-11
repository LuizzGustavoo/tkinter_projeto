import tkinter as tk
from alunos_login import open_login_alunos
from comunidade_login import open_login_comunidade
from admin_login import open_login_admin
from cadastro import open_cadastro

# Função para criar a interface principal (home)
def create_home():
    # Caixa principal
    box = tk.Frame(root, bg="black", bd=10)
    box.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=300, height=300)

    # Título
    tk.Label(box, text="Bem-vindo ao Kaiman System!", font=("Bebas Neue", 20), fg="white", bg="black").pack(pady=10)

    # Subtítulo
    tk.Label(box, text="Escolha o Tipo de Login ou faça o cadastro", font=("Bebas Neue", 14), fg="white", bg="black").pack(pady=5)

    # Botões de login e cadastro
    tk.Button(box, text="Alunos", command=lambda: open_login_alunos(root), bg="#568915", fg="white").pack(pady=5)
    tk.Button(box, text="Servidores", command=lambda: open_login_admin(root), bg="#568915", fg="white").pack(pady=5)
    tk.Button(box, text="Comunidade", command=lambda: open_login_comunidade(root), bg="#568915", fg="white").pack(pady=5)
    tk.Button(box, text="Cadastre-se", command=lambda: open_cadastro(root), bg="#568915", fg="white").pack(pady=5)

# Inicializando a janela principal
root = tk.Tk()
root.title("HOME | Kaiman System")
root.geometry("190x940")
root.configure(bg='#3a6925')

create_home()  # Inicializa a tela principal
root.mainloop()
