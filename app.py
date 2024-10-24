import tkinter as tk
from interface import LoginApp, configure_window

def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# import tkinter as tk
# from tkinter import filedialog

# def upload_image():
#     filepath = filedialog.askopenfilename(
#         filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
#     if filepath:
#         print(f"Arquivo selecionado: {filepath}")
#         # Aqui você pode adicionar o código para manipular a imagem

# class App:
#     def __init__(self, root):
#         self.root = root
#         root.title("Upload de Imagem")
#         self.create_widgets(root)

#     def create_widgets(self, root):
#         self.upload_button = tk.Button(
#             root, text="Subir Imagem", command=upload_image)
#         self.upload_button.pack(pady=20)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
