import tkinter

def hesapla():
    bilgi1 = ent1.get()
    bilgi2 = ent2.get()

    if bilgi1 == "" and bilgi2 != "":
        e3.config(text="")
        fah = (int(bilgi2) * 1.8) + 32
        ent1.insert(0, fah)

    elif bilgi1 != "" and bilgi2 == "":
        e3.config(text="")
        cel = (int(bilgi1) - 32) / 8
        ent2.insert(0, cel)

    elif bilgi1 == "" and bilgi2 == "":
        e3.config(text="İki alan da boş bırakılamaz: ")

    elif bilgi1 != "" and bilgi2 != "":
        e3.config(text="İki alan da dolu olamaz: ")

def temizle():
    ent1.delete(0, tkinter.END)
    ent2.delete(0, tkinter.END)


pencere = tkinter.Tk()
pencere.title("Sıcaklık hesaplama")
pencere.geometry("300x300")

e1 = tkinter.Label(pencere, text="Fahrenheit")
e1.place(x=10,y=10)

e2 = tkinter.Label(pencere, text="Celcius")
e2.place(x=10,y=50)

ent1 = tkinter.Entry(pencere)
ent1.place(x=120,y=10)

ent2 = tkinter.Entry(pencere)
ent2.place(x=120,y=50)

button = tkinter.Button(pencere, text="Hesapla",command=hesapla)
button.place(x=10,y=100)

button2 = tkinter.Button(pencere, text="Temizle",command=temizle)
button2.place(x=120,y=100)

e3 = tkinter.Label(pencere, text=" ")
e3.place(x=10,y=150)


pencere.mainloop()