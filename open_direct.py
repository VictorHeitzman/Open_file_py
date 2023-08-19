from tkinter.filedialog import *
from tkinter import *

# Criando objeto GUI
root = Tk()

# Configurações da tela GUI
def config():
    root.title('Open Direct x Open File')
    root.config(background= "#1F1F1F")
    root.geometry("600x200")
    labels()

# Configurações da Label na tela GUI
def labels():

    global txt_path_dict, txt_path_file

    # Criando título na GUI 
    txt_title = Label(root,
                      text="Selected Path",
                      font="arial 15",
                      background="#1F1F1F",
                      fg="White")
    txt_title.place(relx=0.35)

    # Criando botão na GUI selecionar diretorio na GUI
    button_dict = Button(root,
                         text="path direct",
                         font="arial 10",
                         command=select_direct)
    button_dict.place(relheight=0.12,relwidth=0.15,relx=0.03,rely=0.25)

    # Criando botão na GUI selecionar arquivo na GUI
    button_file = Button(root,
                         text="path file",
                         font="arial 10",
                         command=select_file)
    button_file.place(relheight=0.12,relwidth=0.15,relx=0.03,rely=0.50)

    # Criando caixa de texto para inserir o caminho escolhido
    txt_path_file = Label(text="",
                      font="arial 10",
                      background="#1F1F1F")
    txt_path_file.place(relheight=0.10,relx=0.20,rely=0.50)

    # Criando caixa de texto para inserir o caminho escolhido
    txt_path_dict = Label(text="",
                      font="arial 10",
                      background="#1F1F1F")
    txt_path_dict.place(relheight=0.10,relx=0.20,rely=0.25)

# Selecionando diretorio
def select_direct():
    path_d = askdirectory() # Abrindo diretorio para escolher caminho da pasta
    txt_path_dict.config(text=path_d,fg="red") # escrevendo caminho selecionado na gui

# Selecionando arquivo
def select_file():
    path_f = askopenfilename() # Abrindo diretorio para escolher caminho do arquivo
    txt_path_file.config(text=path_f,fg="red") # escrevendo caminho selecionado na gui

config()

# Apresentando objeto GUI
root.mainloop()