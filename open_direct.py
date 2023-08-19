from tkinter.filedialog import *
from tkinter import *

root = Tk()

def config():
    root.title('Open Direct x Open File')
    root.config(background= "#1F1F1F")
    root.geometry("600x200")
    labels()

def labels():

    global txt_path_dict, txt_path_file

    txt_title = Label(root,
                      text="Selected Path",
                      font="arial 15",
                      background="#1F1F1F",
                      fg="White")
    txt_title.place(relx=0.35)

    button_dict = Button(root,
                         text="path direct",
                         font="arial 10",
                         command=select_direct)
    button_dict.place(relheight=0.12,relwidth=0.15,relx=0.03,rely=0.25)

    button_file = Button(root,
                         text="path file",
                         font="arial 10",
                         command=select_file)
    button_file.place(relheight=0.12,relwidth=0.15,relx=0.03,rely=0.50)

    txt_path_file = Label(text="",
                      font="arial 10",
                      background="#1F1F1F")
    txt_path_file.place(relheight=0.10,relx=0.20,rely=0.50)

    txt_path_dict = Label(text="",
                      font="arial 10",
                      background="#1F1F1F")
    txt_path_dict.place(relheight=0.10,relx=0.20,rely=0.25)

def select_direct():
    path_d = askdirectory()
    txt_path_dict.config(text=path_d,fg="red")

def select_file():
    path_f = askopenfilename()
    txt_path_file.config(text=path_f,fg="red")

config()

root.mainloop()