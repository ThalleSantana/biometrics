from base import Funcionario
from tkinter import messagebox, filedialog
import cv2
import hashlib

class Functions:

  # Função que realiza o login do usuario
  def login(self, email, password, biometria):
    self.email = email
    self.password = password
    self.biometria = biometria
    
    # Verificação para que os campos não venham vazios
    if email != '' and password != '' and biometria is not None:
      
      # realiza o login do usuario com o codigo da base.py
      funcionario = Funcionario.logar(email, password)
      
      # Verifica se o "login" existe
      if funcionario:
        
        # autenticação da biometria do usuario
        auth_result = self.authenticate(biometria, funcionario.biometria, 'l')
        
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

  # Função para pegar a imagem
  def load_image(self, path):
    image = cv2.imread(path)
    if image is None:
      messagebox.showerror("Erro", "Erro ao carregar a imagem.")
    return image
  
  # Função para processar a imagem (converter para cinza e aplicar desfoque)
  def process_image(self, image):
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred

  # Função para segmentar a imagem (binarização)
  def segment_image(self, image):
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    return binary

  # Função para extrair características usando Canny
  def extract_features(self, image):
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image
    features = cv2.Canny(gray_image, 100, 200)
    return features

  # Função para gerar um hash consistente das características extraídas
  def generate_consistent_hash(self, features):
    hasher = hashlib.sha256()
    hasher.update(features.tobytes())
    return hasher.hexdigest()

  # Função para autenticar a biometria
  def authenticate(self, image_path, auth, option):
    image = self.load_image(image_path)
    if image is not None:
      processed_image = self.process_image(image)
      segmented_image = self.segment_image(processed_image)
      features = self.extract_features(segmented_image)
      new_hash = self.generate_consistent_hash(features)
      
      # Opção para cadastro, gerará uma hash para o banco de dados
      if option == 'c':
        return new_hash

      # Opção para o login, no qual verificará se a hash gerada é igual a hash no banco de dados
      elif option == 'l':
        if auth == new_hash:
          return True
        else:
          return False
    else:
      messagebox.showerror("Erro", "Imagem não carregada. Verifique o caminho e tente novamente.")

  # Função para cadastro de usuario
  def cadastrar(self, nome, email, senha, cargo, biometria):

    # Verificação para que os campos não venham vazios
    if nome != '' and email != '' and senha != '' and cargo != '' and biometria is not None:
      
      # Autenticação para geração da hash para biometria
      auth = self.authenticate(biometria, None, 'c')

      # Cadastro do usuario no banco de dados
      novo_funcionario = Funcionario(nome, email,senha, cargo, auth)
      novo_funcionario.create()
      messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
      return True
    else:
      messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
      return False