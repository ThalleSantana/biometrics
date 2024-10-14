# import das bibliotecas utilizadas
import cv2
import hashlib

# criação de uma classe Usuario, para realização de testes
class Usuario:
    def __init__(self, nome, senha, biometria):
        self.nome = nome
        self.senha = senha
        self.biometria = biometria

# criação dos usuarios para teste
usuario1 = Usuario('Thalles', '1234', 'd499e628fd3aeeff3a1d74827c6012d5d1a2bfc3de8045ff9b3b31a57c5625fb')
usuario2 = Usuario('Bruna', '1234', '23ab69d225990be01cd795a92337bcd5fa6d8192e77357f2a495da4b5a770847')
usuario3 = Usuario('Luan', '1234', '8e49c33838bef5de3cc90a9272716b88c77da15b7e206cab0558c0dabca15b08')

# criação de um dicionario, para a utilização do nome do usuario (testes)
usuarios = {
    usuario1.nome: usuario1,
    usuario2.nome: usuario2,
    usuario3.nome: usuario3
}

# Função para carregar a imagem a partir de um caminho no computador
def load_image(path):
    image = cv2.imread(path)
    if image is None:
        print(f"Erro ao carregar a imagem em: {path}")
    return image

# Função para processar a imagem (converter para cinza e aplicar desfoque)
def process_image(image):
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred

# Função para segmentar a imagem (binarização)
def segment_image(image):
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    return binary

# Função para extrair características usando Canny
def extract_features(image):
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image
    features = cv2.Canny(gray_image, 100, 200)
    return features

# Função para gerar um hash consistente das características extraídas
def generate_consistent_hash(features):
    hasher = hashlib.sha256()
    hasher.update(features.tobytes())
    return hasher.hexdigest()

# Função para autenticar a biometria
def authenticate(image_path, stored_hash):
    image = load_image(image_path)
    if image is not None:
        processed_image = process_image(image)
        segmented_image = segment_image(processed_image)
        features = extract_features(segmented_image)
        new_hash = generate_consistent_hash(features)
        if new_hash == stored_hash:
            return "Autenticação bem-sucedida"
        else:
            return "Autenticação falhou"
    else:
        print("Imagem não carregada. Verifique o caminho e tente novamente.")
        return "Erro ao carregar a imagem"

# Função principal para login
def login(nome, senha, imagem_biometria):
    usuario = usuarios.get(nome)
    if usuario and usuario.senha == senha:
        resultado = authenticate(imagem_biometria, usuario.biometria)
        print(resultado)
    else:
        print("Nome ou senha incorretos")

# Exemplo de uso
nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")
imagem_biometria = input("Digite o caminho da biometria: ")

login(nome, senha, imagem_biometria)

# caso for testar, de um print na função generate_consistent_hash(), para que possa colocar o valor da imagem na criação do usuario