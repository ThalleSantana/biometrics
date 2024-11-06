import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkFont
import os  # Import necessário para extrair o nome do arquivo
from functions import Functions

# Instanciando a classe Funcitons, para utilização das funções
functions = Functions()

# Classe criada para funções utilizadas mais de uma vez em outras classes
class BaseApp:
  # Função de configuração do frame, para que possa definir a lagura e altura, e para que fique centralizado na tela
  def configure_window(self, root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    posicao_x = (largura_tela // 2) - (largura // 2)
    posicao_y = (altura_tela // 2) - (altura // 2)
    root.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")
    root.resizable(False, False)

  # Função que carrega a imagem da biometria
  def subir_biometria(self):
    filepath = functions.subir_imagem()
    if filepath:
      nome_arquivo = os.path.basename(filepath)
      self.nome_biometria.config(text=nome_arquivo)
      self.biometria_filepath = filepath

class LoginApp(BaseApp):
  
  # Função para inicialização do Frame, com parametros iniciais e as funções utilizadas
  def __init__(self, root):
    self.root = root
    self.biometria_filepath = None
    root.title("Tela de Login")
    self.configure_window(root, 400, 300) 
        
    # Definindo uma fonte personalizada
    self.font_title = tkFont.Font(family="Helvetica", size=12, weight="bold")
    self.font_normal = tkFont.Font(family="Helvetica", size=10)

    self.create_widgets(root)

  # Função para criação dos itens presentes no Frame
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
    tk.Button(self.frame, text="Upload", command=self.subir_biometria, width=15).grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="WE")

    # Botões Login e Cadastro em nova linha
    self.btn_frame = tk.Frame(self.frame)
    self.btn_frame.grid(row=4, column=0, columnspan=3, pady=20)

    tk.Button(self.btn_frame, text="Login", command=self.verificar_login, width=12, height=2).pack(side=tk.LEFT, padx=10)
    tk.Button(self.btn_frame, text="Cadastrar", command=self.cadastro, width=12, height=2).pack(side=tk.LEFT, padx=10)

  # Função que realiza o login do usuario, pegando as informações presentes nos campos digitados e na variavel da biometria
  def verificar_login(self):
    email = self.entrada_email.get()
    senha = self.entrada_senha.get()
    biometria_texto = self.biometria_filepath
    login_success, cargo_nivel, nome = functions.login(email, senha, biometria_texto)

    # caso a variavel login_sucess seja True, irá para a tela de informações
    if login_success:
      self.root.destroy()
      root = tk.Tk()
      NivelApp(root, cargo_nivel, nome)
    else:
      print("Falha")

  # Função que carrega o Frame da tela de Cadastro
  def cadastro(self):
    self.root.destroy()
    root = tk.Tk()
    CadastroApp(root)

class CadastroApp(BaseApp):

  # Função para inicialização do Frame, com parametros iniciais e as funções utilizadas
  def __init__(self, root):
    self.root = root
    self.biometria_filepath = None
    root.title("Tela de Cadastro")
    self.configure_window(root, 400, 500)
    self.create_widgets(root)

  # Definindo uma fonte personalizada
  def create_widgets(self, root):
    
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
    self.cargo_var = tk.StringVar(value="Analista")
    tk.Radiobutton(self.frame, text="Analista - Nivel 1", variable=self.cargo_var, value="Analista", font=fonte_padrao).grid(row=4, column=1, sticky="W")
    tk.Radiobutton(self.frame, text="Diretor  - Nivel 2", variable=self.cargo_var, value="Diretor", font=fonte_padrao).grid(row=5, column=1, sticky="W")
    tk.Radiobutton(self.frame, text="Ministro - Nivel 3", variable=self.cargo_var, value="Ministro", font=fonte_padrao).grid(row=6, column=1, sticky="W")

    # Biometria Label e Nome do Arquivo
    tk.Label(self.frame, text="Biometria", font=fonte_padrao).grid(row=7, column=0, padx=10, pady=10, sticky="E")
    self.nome_biometria = tk.Label(self.frame, text="", anchor="w", font=fonte_padrao)
    self.nome_biometria.grid(row=7, column=1, padx=10, pady=10, sticky="WE")

    # Botão Subir Biometria
    tk.Button(self.frame, text="Upload", command=self.subir_biometria, font=fonte_padrao, width=15).grid(row=8, column=1, padx=10, pady=10, sticky="WE")

    # Frame para os botões
    self.btn_frame = tk.Frame(self.frame)
    self.btn_frame.grid(row=9, column=0, columnspan=2, pady=20)

    # Botões Cadastrar e Voltar
    tk.Button(self.btn_frame, text="Cadastrar", command=self.cadastrar_usuario, font=fonte_padrao, width=12, height=2).pack(side=tk.LEFT, padx=10)
    tk.Button(self.btn_frame, text="Voltar", command=self.voltar, font=fonte_padrao, width=12, height=2).pack(side=tk.LEFT, padx=10)

  # Função que realiza o cadastro do usuario
  def cadastrar_usuario(self):
    nome = self.entrada_nome.get()
    email = self.entrada_email.get()
    senha = self.entrada_senha.get()
    confirmar_senha = self.entrada_confirma_senha.get()
    cargo = self.cargo_var.get()
    biometria_texto = self.biometria_filepath

    # Verifica se as senhas são diferentes
    if senha != confirmar_senha:
      tk.messagebox.showerror("Erro", "As senhas não coincidem!")
    else:

      # Realiza o cadastro
      cadastro_sucesso = functions.cadastrar(nome, email, senha, cargo, biometria_texto)
      
      # Caso o cadastro seja concluido com sucesso, retornará para a tela de login
      if cadastro_sucesso:
        self.root.destroy()
        root = tk.Tk()
        LoginApp(root)

  # Função para retornar a tela de login
  def voltar(self):
    self.root.destroy()
    root = tk.Tk()
    LoginApp(root)

class NivelApp(BaseApp):
    # Função para inicialização do Frame, com parametros iniciais e as funções utilizadas
    def __init__(self, root, nivel_max, nome):
        self.root = root
        self.nivel_max = nivel_max
        self.current_frame = None
        self.current_property_id = None
        root.title("Tela de Acesso")
        self.configure_window(root, 550, 500)

        self.font_normal = tkFont.Font(family="Helvetica", size=10)
        self.font_bold = tkFont.Font(family="Helvetica", size=10, weight="bold")
        
        # Adiciona o texto "Bem-vindo, *Nome do Usuário*" no topo do frame
        self.welcome_label = tk.Label(root, text=f"Bem-vindo, {nome}", font=self.font_normal)
        self.welcome_label.pack(pady=10)

        # Adiciona o texto antes dos botões de ID
        self.info_label = tk.Label(root, text="Selecione o ID de propriedade a ser verificado", font=self.font_normal)
        self.info_label.pack(pady=10)

        # Cria os botões de propriedades no topo da janela
        self.create_property_buttons(root)
        
        # Cria o canvas com scroll
        self.create_scrollable_frame(root)

        # Cria o botão "Voltar para Login" no canto inferior direito
        self.create_back_to_login_button(root)

    # Função relacionada aos botões que realizam a seleção das informações, com o ID da propriedade
    def create_property_buttons(self, root):
      
      # Criação do frame para os botões
      self.button_frame = tk.Frame(root)
      self.button_frame.pack(pady=10)

      # Variavel que recebe os ids do banco de dados
      property_ids = functions.get_ids()
      
      # Laço de repetição para rodar a quantidade de "linhas" que o banco de dados tem
      for property_id in property_ids:
        
        # Criação do botão
        button = tk.Button(
          self.button_frame,
          
          # Texto do botão, puxando o id da propriedade
          text=f"ID {property_id}",
          
          # Comando para aparecer as informações com base no ID
          command=lambda property_id=property_id: self.show_property_info(property_id),
          width=10
        )
        button.pack(side=tk.LEFT, padx=5)

    # Função para criação do botão que retorna para a tela de login
    def create_back_to_login_button(self, root):
        back_button = tk.Button(
            root,
            text="Voltar para Login",
            command=self.voltar_para_login
        )
        back_button.pack(side=tk.BOTTOM, pady=10, padx=10, anchor='se')

    # Função que retorna para a tela de login
    def voltar_para_login(self):
        self.root.destroy()
        root = tk.Tk()
        LoginApp(root)

    # CFunção para que haja o scroll no frame
    def create_scrollable_frame(self, root):
        # Cria um canvas para o scroll
        self.canvas = tk.Canvas(root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Adiciona scrollbar ao canvas
        self.scrollbar = tk.Scrollbar(root, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # Cria um frame dentro do canvas
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Permite o scroll com o mouse
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

    # Função para o scroll do mouse funcionar no frame
    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    # Função para apararição das informações no frame
    def show_property_info(self, property_id):
        self.current_property_id = property_id
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(pady=20)

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        shown_titles = set()  # Conjunto para rastrear títulos exibidos

        for level in range(1, self.nivel_max + 1):
            data = functions.get_data_by_id(self.current_property_id)
            if data:
                nivel_data = data.get(f"Nível {level}")
                if nivel_data:
                    for key, value in nivel_data.items():
                        if isinstance(value, dict):
                            if key not in shown_titles:  # Verifica se o título já foi exibido
                                title_widget = tk.Label(self.scrollable_frame, text=f"{key}:", font=self.font_bold, anchor="w")
                                title_widget.pack(fill='x', padx=10, pady=2)
                                shown_titles.add(key)  # Adiciona título ao conjunto de títulos exibidos
                            for sub_key, sub_value in value.items():
                                self.add_text_widget(sub_key, sub_value)
                        else:
                            self.add_text_widget(key, value)

    # Função para adição do texto no frame
    def add_text_widget(self, key, value):
        if isinstance(value, list):
            value = ", ".join(value)
        padding_frame = tk.Frame(self.scrollable_frame, bg=self.root.cget('bg'))
        padding_frame.pack(fill='x', padx=10, pady=2)
        title_widget = tk.Label(padding_frame, text=f"{key}:", font=self.font_bold, anchor="w")
        title_widget.pack(anchor="w")
        text_widget = tk.Text(padding_frame, wrap="word", font=self.font_normal, bg=self.root.cget('bg'), relief="flat", width=50, height=5)
        text_widget.insert(tk.END, f"{value}\n")
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(anchor="w")





