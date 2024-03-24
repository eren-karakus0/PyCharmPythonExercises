import tkinter as tk
def e_posta_gonder():
    if e_posta_var.get() == 1:
        print("E-posta gönderilecek")
    else:
        print("E-posta gönderilmeyecek")

def boyama():
    canvas.create_rectangle(50, 50, 200, 150, fill='white')

pencere = tk.Tk()
pencere.title("Hatırlatma Uygulaması")
pencere.geometry("1080x480")
pencere.config(bg="#79bedf",borderwidth=10, relief="groove")

canvas = tk.Canvas(pencere,width=10, height=10, bg="white")
canvas.place(x=0,y=90,width=1100, height=10)

canvas = tk.Canvas(pencere,width=10, height=10, bg="white")
canvas.place(x=300,y=100,width=10, height=1000)

hatirlatma_tipi_label = tk.Label(pencere, text="Hatırlatma Tipi:",
                                 font=("Consolas",15),
                                 background="#79bedf")
hatirlatma_tipi_label.place(x=10,y=20)

hatirlatma_tipi_entry = tk.Entry(pencere ,font=("Consolas", 15))
hatirlatma_tipi_entry.place(x=250,y=20)

hatirlatma_tarihi_label = tk.Label(pencere, text="Hatırlatma Tarihi:",
                                   font=("Consolas",15),
                                   background="#79bedf")
hatirlatma_tarihi_label.place(x=600,y=20)

hatirlatma_tarihi_entry = tk.Entry(pencere ,font=("Consolas",15))
hatirlatma_tarihi_entry.place(x=820,y=20)
hatirlatma_tarihi_entry.insert(0,"21.11.20")


hatirlatma_yontemi_label = tk.Label(pencere, text="Hatırlatma Yöntemi:",
                                    font=("Consolas",15),
                                    background="#79bedf")
hatirlatma_yontemi_label.place(x=10,y=120)

sisteme_kaydet = tk.Checkbutton(pencere, text="Sisteme Kaydet",
                                font=("Consolas",15),
                                background="#79bedf")
sisteme_kaydet.place(x=10,y=150)

e_posta_var = tk.IntVar()
e_posta_checkbox = tk.Checkbutton(pencere, text="E-posta gönder", variable=e_posta_var,
                                  font=("Consolas",15),
                                  background="#79bedf")
e_posta_checkbox.place(x=10,y=180)

hatirlatma_sure_ayni_gun = tk.Radiobutton(pencere, text="Aynı Gün", value="Aynı Gün",
                                          font=("Consolas",15),
                                          background="#79bedf")
hatirlatma_sure_ayni_gun.place(x=30,y=310)

hatirlatma_sure_bir_hafta = tk.Radiobutton(pencere, text="Bir Hafta Önce", value="Bir Hafta Önce",
                                           font=("Consolas",15),
                                           background="#79bedf")
hatirlatma_sure_bir_hafta.place(x=30,y=230)

hatirlatma_sure_bir_hafta = tk.Radiobutton(pencere, text="Bir Hafta Önce", value="Bir Hafta Önce",
                                           font=("Consolas",15),
                                           background="#79bedf")
hatirlatma_sure_bir_hafta.place(x=30,y=270)

# Üçüncü ızgara
hatirlatma_mesaji_label = tk.Label(pencere, text="Hatırlatma Mesajı:",
                                   font=("Consolas",15),
                                   background="#79bedf")
hatirlatma_mesaji_label.place(x=350,y=120)

hatirlatma_mesaji_entry = tk.Text(pencere, height=14, width=78,
                                  font=("Consolas",12),
                                  background="light yellow")
hatirlatma_mesaji_entry.place(x=350,y=150)


gonder_butonu = tk.Button(pencere, text="Gönder", command=e_posta_gonder,
                          font=("Consolas",15))
gonder_butonu.place(x=600,y=425)

pencere.mainloop()
