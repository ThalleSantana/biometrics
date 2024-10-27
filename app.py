import tkinter as tk
from interface import LoginApp

def main():
  root = tk.Tk()
  app = LoginApp(root)
  root.mainloop()

# Código no qual executo o projeto, para que comece a funcionar
if __name__ == "__main__":
  main()