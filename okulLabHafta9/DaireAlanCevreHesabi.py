import tkinter

def alanHesap():
    yaricap = float(myEntry.get())
    hesap = 3.14159 * (yaricap ** 2)
    myEntry2.delete(0 , 20)
    myEntry2.insert(0, hesap)

def cevreHesap():
    yaricap = float(myEntry.get())
    hesap = 3.14159 * 2 * yaricap
    myEntry.delete(0, 20)
    myEntry.insert(0, hesap)

def cikis():
    pencere.destroy()

pencere = tkinter.Tk()
pencere.title("DAİRE ALAN - ÇEVRE HESAPLAMA")
pencere.geometry("350x300")
pencere.config(background="black")

etiket1 = tkinter.Label(pencere, text="Dairenin Yarıçapını giriniz: ",
                        bg="black",
                        fg="#00FF00")
etiket1.place(x=10,y=10)

etiket2 = tkinter.Label(pencere, text="cm.",
                        bg="black",
                        fg="#00FF00")
etiket2.place(x=300,y=10)

etiket3 = tkinter.Label(pencere, text="cm^2",
                        bg="black",
                        fg="#00FF00")
etiket3.place(x=300,y=30)

myEntry = tkinter.Entry(pencere)
myEntry.place(x=160,y=10)

myEntry2 = tkinter.Entry(pencere)
myEntry2.place(x=160,y=30)

button1 = tkinter.Button(pencere, text="ALAN HESAPLA",
                         command=alanHesap,
                         bg="black",
                         fg="#00FF00")
button1.place(x=10,y=50)

button2 = tkinter.Button(pencere, text="ÇEVRE HESAPLA",
                         command=cevreHesap,
                         bg="black",
                         fg="#00FF00")
button2.place(x=150,y=50)

button3 = tkinter.Button(pencere, text="ÇIKIŞ",
                         command=cikis,
                         bg="black",
                         fg="#00FF00",
                         activebackground="black",
                         activeforeground="#00FF00")
button3.place(x=250,y=230)

pencere.mainloop()