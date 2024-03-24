import tkinter

#window --> pencere oluşturma , isim verme , boyutunu ayarlama gibi...
window = tkinter.Tk()
window.title("Python tkinter")
window.minsize(300,200)

#label --> kullanıcıya metin göstermek için kullanırız.

my_label = tkinter.Label(text="this is a label")
#my_label.config(bg="black",fg="white",font=("Arial",20,"italic"))
#my_label.pack(side="top") #pack ortaya konumlandır gibi bir anlam veriyor daha farklı fonksiyonlar da var görecez
#my_label.place(x=0,y=0) #koordinat
my_label.grid(column=0,row=0) #ızgara sistemi satır kolon

def click_button():
    user_input = my_entry.get()
    print(user_input)
#button
my_button =tkinter.Button(text="Click me!", command=click_button)
#my_button.pack(side="top")
#my_button.place(x=100,y=100)
#my_button.update()
#print(my_button.winfo_height())
my_button.grid(column=1,row=0)

#entry
my_entry = tkinter.Entry(width=20)
#my_entry.pack(side="top")
#my_entry.place(x=50,y=40)
my_entry.grid(column=1,row=1)


window.mainloop()