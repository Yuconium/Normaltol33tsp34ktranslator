from tkinter import *

class App:
    def __init__(self, window):
        self.Eingabe = Entry(window, width = 30)
        self.Eingabe.pack()
        self.Ausgabe = Entry(window, width = 30)
        self.Ausgabe.pack()
        self.Changer = Button(window, text = "lets l33t!", command = lambda: self.l33tfunktion())
        self.Changer.pack()
        


   
       

    
    def l33tfunktion(self):
        if self.Eingabe.get() == "":
            self.Ausgabe.insert(INSERT, "Couldnt find any words")
        else:
            self.normal = self.Eingabe.get()
            self.Ausgabe.insert(INSERT, self.normal.replace("e", "3").replace("k", " |<").replace("a", "4").replace("S", "5").replace("o", "0").replace("O", "0")


if __name__ == "__main__":
    window = Tk()
    window.geometry("300x300")
    window.title("L33tsp33k")
    leetapp = App(window)
    window.mainloop()