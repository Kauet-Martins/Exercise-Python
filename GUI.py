import tkinter as tk

# Cria a janela principal
root = tk.Tk()

root.title('First GUI')

root.geometry('300x300')

buton = tk.Button(root, text='Sair', command=root.destroy)

buton.pack()

root.mainloop()


