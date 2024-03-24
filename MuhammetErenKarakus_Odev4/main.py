import tkinter as tk

def cizim_yap():
    secilen_sekil = secim.get()
    if secilen_sekil == "Daire":
        canvas.create_oval(50, 50, 150, 150, outline="black")
    elif secilen_sekil == "Kare":
        canvas.create_rectangle(50, 50, 150, 150, outline='black')
    elif secilen_sekil == "Üçgen":
        canvas.create_polygon(50, 150, 150, 150, 100, 50, outline='black')

pencere = tk.Tk()
pencere.title("Şekil Çizdirme Uygulaması")

secim = tk.StringVar()
secim.set("Daire")

secim_menu = tk.OptionMenu(pencere, secim, "Daire", "Kare", "Üçgen")
secim_menu.pack()

cizim_butonu = tk.Button(pencere, text="Çizim Yap", command=cizim_yap)
cizim_butonu.pack()

canvas = tk.Canvas(pencere, width=200, height=200)
canvas.pack()

pencere.mainloop()
