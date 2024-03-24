from tkinter import *
from tkinter import messagebox

def giris():
    if (myEntry1.get() == "Eren Karakus" and myEntry2.get() == "123456"):
        etiket3['text'] = "Giriş Başarılı:)) "
        messagebox.showinfo("Başlık", "Giriş Başarılı")
        print("Başarılı!!! ")
    else:
        etiket3['text'] = "Giriş Başarısız:(( "
        messagebox.showerror("Başlık", "Giriş Başarısız!!! ")
        print("Başarısız!: ")

pencere = Tk()
pencere.title("Kullanıcı Giriş Ekranı")
pencere.geometry("480x320")
pencere.config(bg="blue")
pencere.resizable(width=False, height=False)

etiket1 = Label(pencere, text="Kullanıcı Adı",
                font=("Arial", 15),
                background="purple",
                foreground="black")
etiket1.place(x=50,y=50)

etiket2 = Label(pencere, text="Şifre",
                font=("Arial", 15),
                background="purple",
                foreground="black")
etiket2.place(x=50,y=100)

etiket3 = Label(pencere, text="",
                font=("Arial",15),
                background="black",
                foreground="purple")
etiket3.place(x=200,y=270)

myEntry1 = Entry(pencere,
              font=("Arial",15),
              fg="purple",
              bg="black")
myEntry1.place(x=200,y=50)

myEntry2 = Entry(pencere,
              font=("Arial",15),
              fg="purple",
              bg="black")
myEntry2.place(x=200,y=100)

myButton1 = Button(pencere, text="Giriş Yap",
                   font=("Arial", 15),
                   command=giris,
                   background="black",
                   foreground="purple")
myButton1.place(x=300,y=200)

pencere.mainloop()