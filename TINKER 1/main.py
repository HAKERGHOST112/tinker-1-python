from tkinter import *

class Calc:
    def __init__(self, master):
        self.master = master
        self.txt = Entry(master, width=15)
        self.txt2 = Entry(master, width=15)
        self.resul = Label(master, text=" ", width=15,)

        self.slojeniet=Button(master, text="+", width=20, command=self.slojenie)
        self.vicitaniet = Button(master, text="-", width=20, command=self.vicitanie)
        self.ymnt = Button(master, text="*", width=20, command=self.ymn)
        self.dellt = Button(master, text="/", width=20, command=self.dell)

        self.txt.pack(side=TOP, padx=10, pady=10)
        self.txt2.pack(side=TOP, padx=10, pady=10)
        self.resul.pack(side=BOTTOM, padx=10, pady=10)

        self.slojeniet.pack(side=BOTTOM, padx=10, pady=10)
        self.vicitaniet.pack(side=BOTTOM, padx=10, pady=10)
        self.ymnt.pack(side=BOTTOM, padx=10, pady=10)
        self.dellt.pack(side=BOTTOM, padx=10, pady=10)

    def slojenie(self):
        self.Calc(lambda a,b: a+b)

    def vicitanie(self):
        self.Calc(lambda a,b: a-b)

    def ymn(self):
        self.Calc(lambda a,b: a*b)

    def dell(self):
        self.Calc(lambda a,b: a/b)

    def Calc(self, operation):
        N1=float(self.txt.get())
        N2=float(self.txt2.get())
        resul=operation(N1,N2)
        self.resul['text']=str(resul)


root=Tk()
root.title("Калькулятор")
root.geometry("300x300")
pril =Calc(root)

root.mainloop()




