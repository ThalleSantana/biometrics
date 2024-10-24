from base import Funcionario
from tkinter import messagebox, filedialog
import cv2

class Functions:
  def login(self, email, password):
    self.email = email
    self.password = password
    if email and password != '':
      funcionario = Funcionario.logar(email, password)
      if funcionario:
        messagebox.showinfo("Login", "Login bem-sucedido!")
      else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")
    else:
      messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

  def subir_imagem(self):
    filepath = filedialog.askopenfilename(
      filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
    )
    if filepath:
      print(f"Arquivo selecionado: {filepath}")
      return filepath
  
  def load_image(path):
    image = cv2.imread(path)
    if image is None:
        print(f"Erro ao carregar a imagem em: {path}")
    return image

  def cadastrar(self, nome, email, password, cargo):
    print