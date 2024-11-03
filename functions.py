from base import Funcionario
from tkinter import messagebox, filedialog
import cv2
import hashlib

class Functions:

  # Função que realiza o login do usuario
  def login(self, email, password, biometria_path):
    self.email = email
    self.password = password
    self.biometria_path = biometria_path
    
    # Verificação para que os campos não venham vazios
    if email != '' and password != '' and biometria_path is not None:
      
      # realiza o login do usuario com o codigo da base.py
      funcionario = Funcionario.logar(email, password)
      
      # Verifica se o "login" existe
      if funcionario:
        
        # autenticação da biometria do usuario
        auth_result = self.authenticate(biometria_path, funcionario.biometria, 'l')
        
        # verifica se a biometria é igual
        if auth_result:
          messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
          messagebox.showerror("Erro", "Informações incorretas.")
      else:
        messagebox.showerror("Erro", "Informações incorretas.")
    else:
      messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

  # Função para pegar o caminho da imagem imagem (biomentria)
  def subir_imagem(self):
    filepath = filedialog.askopenfilename(
      filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
    )
    if filepath:
      return filepath

  def gerar_hash_biometria(self, image_path):
    # 1. Aquisição da imagem
    image = cv2.imread(image_path)
    
    # 2. Pré-processamento
    # 2.1. Conversão para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 2.2. Equalização do histograma
    equalized_image = cv2.equalizeHist(gray_image)
    
    # 2.3. Filtro de suavização
    smoothed_image = cv2.GaussianBlur(equalized_image, (5, 5), 0)
    
    # 3. Segmentação (Filtro de bordas)
    edges = cv2.Canny(smoothed_image, 100, 200)

    # 4. Extração de Características com ORB
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(edges, None)

    # 5. Classificação/Interpretação - Gera a hash baseada nos descritores
    # 5.1. Concatena as coordenadas dos pontos-chave para gerar um hash
    keypoints_data = ""
    for kp in keypoints:
      keypoints_data += f"{kp.pt}-{kp.angle}-{kp.size};"

    # 5.2. Gera uma hash constante a partir dos pontos detectados
    hash_value = hashlib.sha256(keypoints_data.encode()).hexdigest()

    return hash_value

  # Função para autenticar a biometria
  def authenticate(self, image_path, auth, option):
    new_hash = self.gerar_hash_biometria(image_path)
      
    # Opção para cadastro, gerará uma hash para o banco de dados
    if option == 'c':
      return new_hash

    # Opção para o login, no qual verificará se a hash gerada é igual a hash no banco de dados
    elif option == 'l':
      if auth == new_hash:
        return True
      else:
        return False

  # Função para cadastro de usuario
  def cadastrar(self, nome, email, senha, cargo, biometria_path):

    # Verificação para que os campos não venham vazios
    if nome != '' and email != '' and senha != '' and cargo != '' and biometria_path is not None:
      
      # Autenticação para geração da hash para biometria
      auth = self.authenticate(biometria_path, None, 'c')

      # Cadastro do usuario no banco de dados
      novo_funcionario = Funcionario(nome, email,senha, cargo, auth)
      novo_funcionario.create()
      messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
      return True
    else:
      messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
      return False
    
