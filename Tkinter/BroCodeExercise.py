import tkinter

window = tkinter.Tk()
window.geometry("480x480") #pencere boyutu
window.title("Hi Bro")

# icon = tkinter.PhotoImage(file='indir.jpg') sol üstte bulunan ikonu değiştirebiliyorsun
# window.iconphoto(True, icon)
window.config(background="blue")

window.mainloop()