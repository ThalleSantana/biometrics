import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkFont
import os  # Import necessário para extrair o nome do arquivo
from functions import Functions

functions = Functions()

def configure_window(root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    posicao_x = (largura_tela // 2) - (largura // 2)
    posicao_y = (altura_tela // 2) - (altura // 2)
    root.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")
    root.resizable(False, False)

class LoginApp:
    def __init__(self, root):
        self.root = root
        root.title("Tela de Login")
        configure_window(root, 400, 300)  # Aumentei a altura da janela para acomodar os novos elementos
        
        # Definindo uma fonte personalizada
        self.font_title = tkFont.Font(family="Helvetica", size=12, weight="bold")
        self.font_normal = tkFont.Font(family="Helvetica", size=10)

        self.create_widgets(root)

    def create_widgets(self, root):
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        # Rótulos e Entradas
        tk.Label(self.frame, text="Email", font=self.font_normal).grid(row=0, column=0, padx=10, pady=10, sticky="E")
        self.entrada_email = tk.Entry(self.frame, width=30)
        self.entrada_email.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="WE")

        tk.Label(self.frame, text="Senha", font=self.font_normal).grid(row=1, column=0, padx=10, pady=10, sticky="E")
        self.entrada_senha = tk.Entry(self.frame, show="*", width=30)
        self.entrada_senha.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="WE")

        # Biometria Label e Nome do Arquivo
        tk.Label(self.frame, text="Biometria", font=self.font_normal).grid(row=2, column=0, padx=10, pady=10, sticky="E")
        self.nome_biometria = tk.Label(self.frame, text="", font=self.font_normal, anchor="w")
        self.nome_biometria.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="WE")

        # Botão Subir Biometria em nova linha
        tk.Button(self.frame, text="Subir Biometria", command=self.subir_biometria, width=15).grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="WE")

        # Botões Login e Cadastro em nova linha
        self.btn_frame = tk.Frame(self.frame)
        self.btn_frame.grid(row=4, column=0, columnspan=3, pady=20)

        tk.Button(self.btn_frame, text="Login", command=self.verificar_login, width=12, height=2).pack(side=tk.LEFT, padx=10)
        tk.Button(self.btn_frame, text="Cadastrar", command=self.cadastro, width=12, height=2).pack(side=tk.LEFT, padx=10)

    def verificar_login(self):
        functions.login(self.entrada_email.get(), self.entrada_senha.get())

    def cadastro(self):
        self.root.destroy()
        root = tk.Tk()
        CadastroApp(root)

    def subir_biometria(self):
        filepath = functions.subir_imagem()
        if filepath:
          nome_arquivo = os.path.basename(filepath)
          self.nome_biometria.config(text=nome_arquivo)

class CadastroApp:
    def __init__(self, root):
        self.root = root
        root.title("Tela de Cadastro")
        configure_window(root, 400, 500)  # Ajuste da altura para mais espaço
        self.create_widgets(root)

    def create_widgets(self, root):
        # Fonte personalizada
        fonte_padrao = tkFont.Font(family="Arial", size=10)

        # Frame principal com padding para centralizar melhor os itens
        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack(expand=True)

        # Campo Nome
        tk.Label(self.frame, text="Nome", font=fonte_padrao).grid(row=0, column=0, padx=10, pady=10, sticky="E")
        self.entrada_nome = tk.Entry(self.frame, width=30)
        self.entrada_nome.grid(row=0, column=1, padx=10, pady=10, sticky="WE")

        # Campo Email
        tk.Label(self.frame, text="Email", font=fonte_padrao).grid(row=1, column=0, padx=10, pady=10, sticky="E")
        self.entrada_email = tk.Entry(self.frame, width=30)
        self.entrada_email.grid(row=1, column=1, padx=10, pady=10, sticky="WE")

        # Campo Senha
        tk.Label(self.frame, text="Senha", font=fonte_padrao).grid(row=2, column=0, padx=10, pady=10, sticky="E")
        self.entrada_senha = tk.Entry(self.frame, show="*", width=30)
        self.entrada_senha.grid(row=2, column=1, padx=10, pady=10, sticky="WE")

        # Campo Confirmação de Senha
        tk.Label(self.frame, text="Confirmar Senha", font=fonte_padrao).grid(row=3, column=0, padx=10, pady=10, sticky="E")
        self.entrada_confirma_senha = tk.Entry(self.frame, show="*", width=30)
        self.entrada_confirma_senha.grid(row=3, column=1, padx=10, pady=10, sticky="WE")

        # Campo Cargo (Radiobuttons)
        tk.Label(self.frame, text="Cargo", font=fonte_padrao).grid(row=4, column=0, padx=10, pady=10, sticky="E")
        self.cargo_var = tk.StringVar(value="Desenvolvedor")
        tk.Radiobutton(self.frame, text="Desenvolvedor", variable=self.cargo_var, value="Desenvolvedor", font=fonte_padrao).grid(row=4, column=1, sticky="W")
        tk.Radiobutton(self.frame, text="Gerente", variable=self.cargo_var, value="Gerente", font=fonte_padrao).grid(row=5, column=1, sticky="W")
        tk.Radiobutton(self.frame, text="Tester", variable=self.cargo_var, value="Tester", font=fonte_padrao).grid(row=6, column=1, sticky="W")

        # Biometria Label e Nome do Arquivo
        tk.Label(self.frame, text="Biometria", font=fonte_padrao).grid(row=7, column=0, padx=10, pady=10, sticky="E")
        self.nome_biometria = tk.Label(self.frame, text="", anchor="w", font=fonte_padrao)
        self.nome_biometria.grid(row=7, column=1, padx=10, pady=10, sticky="WE")

        # Botão Subir Biometria
        tk.Button(self.frame, text="Subir Biometria", command=self.subir_biometria, font=fonte_padrao, width=15).grid(row=8, column=1, padx=10, pady=10, sticky="WE")

        # Frame para os botões
        self.btn_frame = tk.Frame(self.frame)
        self.btn_frame.grid(row=9, column=0, columnspan=2, pady=20)

        # Botões Cadastrar e Voltar
        tk.Button(self.btn_frame, text="Cadastrar", command=self.cadastrar_usuario, font=fonte_padrao, width=12, height=2).pack(side=tk.LEFT, padx=10)
        tk.Button(self.btn_frame, text="Voltar", command=self.voltar, font=fonte_padrao, width=12, height=2).pack(side=tk.LEFT, padx=10)

    def cadastrar_usuario(self):
        nome = self.entrada_nome.get()
        email = self.entrada_email.get()
        senha = self.entrada_senha.get()
        confirmar_senha = self.entrada_confirma_senha.get()
        cargo = self.cargo_var.get()

        if senha != confirmar_senha:
            tk.messagebox.showerror("Erro", "As senhas não coincidem!")
        else:
            functions.cadastrar(nome, email, senha, cargo)
            tk.messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

    def voltar(self):
        self.root.destroy()
        root = tk.Tk()
        LoginApp(root)

    def subir_biometria(self):
        caminho_arquivo = filedialog.askopenfilename(title="Selecione o arquivo de biometria", filetypes=[("Todos os arquivos", "*.*")])
        if caminho_arquivo:
            nome_arquivo = os.path.basename(caminho_arquivo)
            self.nome_biometria.config(text=nome_arquivo)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
