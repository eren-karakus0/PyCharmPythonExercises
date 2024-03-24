import tkinter

def hesapla():
    kgIndex = myEntry.get()
    boyIndex = myEntry2.get()
    if myEntry != "" and myEntry2 != "":
        sonuc = float(float(kgIndex) / ((float(boyIndex) / 100) * (float(boyIndex) / 100)))
    else:
        myLabel3["text"] = "Lütfen değerleri giriniz: "

    if sonuc < 18.5:
        myLabel3["text"] = "Zayıfsınız!"
        myEntry3.insert(0,str(sonuc))
    elif 18.5 <= sonuc < 24.9:
        myLabel3["text"] = "Normal kilonuzdasınız! "
        myEntry3.insert(0, str(sonuc))
    elif 24.9 <= sonuc < 29.9:
        myLabel3["text"] = "Kilolusunuz! Egzersiz yapın:"
        myEntry3.insert(0, str(sonuc))
    elif 29.9 <= sonuc < 34.9:
        myLabel3["text"] = "Biraz daha yersen obez olucan.Egzersiz yap!"
        myEntry3.insert(0, str(sonuc))
    else:
        myLabel3["text"] = "Tam anlamıyla bir obezsin!!!"
        myEntry3.insert(0, str(sonuc))



pencere = tkinter.Tk()
pencere.title("BMI Hesaplama")
pencere.geometry("300x300")
pencere.config(background="light blue")

myLabel = tkinter.Label(pencere, text="Kilonuzu giriniz: (kg)",
                        background="light blue",
                        font=("Arial",15))
myLabel.pack()

myEntry = tkinter.Entry(pencere, background="black", foreground="yellow",
                        font=("Helvetica",15))
myEntry.pack()

myLabel2 = tkinter.Label(pencere, text="Boyunuzu giriniz: (cm)",
                        background="light blue",
                        font=("Helvetica",15))
myLabel2.pack()

myEntry2 = tkinter.Entry(pencere, background="black", foreground="yellow",
                        font=("Helvetica",15))
myEntry2.pack()

button = tkinter.Button(pencere, text="Hesapla", background="light blue",command=hesapla,
                        font=("Helvetica",15))
button.pack()

myLabel3 = tkinter.Label(pencere, text="Sonuc:",
                         background="light blue",
                         font=("Helvetica", 15))
myLabel3.pack()
myEntry3 = tkinter.Entry(pencere,
                         background="light blue",
                         font=("Helvetica", 15))
myEntry3.pack()

pencere.mainloop()