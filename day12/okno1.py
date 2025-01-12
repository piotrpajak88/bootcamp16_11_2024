import tkinter

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk() # tworzenie okienka

        self.label1 = tkinter.Label(self.main_window, text = 'W')
        self.label2 = tkinter.Label(self.main_window, text = 'E')
        self.label3 = tkinter.Label(self.main_window, text = 'N')
        self.label4 = tkinter.Label(self.main_window, text = 'S')

        self.label1.pack(side='left') # umieszczenie etykiety w oknie
        self.label2.pack(side='right')
        self.label3.pack(side='top')
        self.label4.pack(side=tkinter.BOTTOM)

        tkinter.mainloop()

my_gui = MyGui()
