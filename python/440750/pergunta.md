olá, queria fazer uma progressbar em tkinter que quando chegasse ao fim ela parasse, o andamento da progressbar seria ativado por um botão, porém quando o botão é ativado, não acontece o andamento da progressbar. Estou usando o seguinte código:

```from tkinter import *

janela = Tk()
janela.geometry('500x500')
def iniciar():   
    import tkinter as tk
    from tkinter import ttk

    class SampleApp(tk.Tk):
        def __init__(self,*args, **kwargs):

            tk.Tk.__init__(self,*args, **kwargs)
            
            self.button = ttk.Button(self, text = 'play', command = self.start)
            self.button.pack()

            self.var_aux = tk.IntVar()

            self.progress = ttk.Progressbar(
                self, orient = "horizontal",
                length = 500, mode = "determinate",
                variable = self.var_aux
                )

            self.progress.place(x = 0, y = 50)
            self.bytes = 0
            self.maxbytes = 0

        def start(self):

            self.maxbytes = 50000
            self.progress['maximum'] = self.maxbytes
            self.read_bytes()


        def read_bytes(self):

            self.bytes += 500
            self.var_aux.set(self.bytes)

            if self.bytes < self.maxbytes:
                self.after(10, self.read_bytes)

    app = SampleApp()
    app.geometry('500x100')
    app.mainloop()

lb = Button(janela, text = 'começar', command = iniciar)
lb.place(x = 10, y = 10)

janela.mainloop()

