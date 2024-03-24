from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

#photo = PhotoImage(file='person.png')

label = Label(window,
              text="bro, do you even code?",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED, #kabartma
              bd=10,
              padx=20,
              pady=20,
              #image=photo,
              compound='bottom') #girilen fotoğraf aşşağıda da mı üstte mi olucak
label.pack()
#label.place(x=0,y=0)

window.mainloop()