from tkinter import *

window = Tk()
window.title("Tkinter python")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

# label
my_label = Label(text="my label")
my_label.config(bg="black", fg="white")
my_label.config(padx=10, pady=10)
my_label.pack()


# button
def button_clicked():
    print("button clicked")
    print(my_text.get("1.0", END))


my_button = Button(text="button", command=button_clicked)
my_button.config(padx=10, pady=10)
my_button.pack()

# entry
my_entry = Entry(width=20)
my_entry.pack()

# multiline
# text
my_text = Text(width=30, height=10)
my_text.focus()
my_text.pack()


#scale
def scale_Selected(value):
    print(value)

my_scale = Scale(from_=0, to=50 , command=scale_Selected) #bir yerden bir yere
my_scale.pack()

#spinbox

def spinbox_Selected():
    print(my_spinbox.get())
my_spinbox = Spinbox(from_=0, to=50 , command=spinbox_Selected)
my_spinbox.pack()


#checkbutton

def checkbutton_Selected():
    print(check_state.get())

check_state = IntVar() #bununla 1 - 0 değerleri tutuluyor check e basınca 1 yoksa 0
my_checkbutton = Checkbutton(text="check", variable=check_state,command=checkbutton_Selected)
my_checkbutton.pack()

#raido button
def radio_Selected():
    print(radio_checked_state.get())

radio_checked_state = IntVar()
my_radiobutton = Radiobutton(text="1. option",value=10, variable=radio_checked_state,command=radio_Selected)
my_radiobutton_2 = Radiobutton(text="2. option",value=20, variable=radio_checked_state,command=radio_Selected)
my_radiobutton.pack()
my_radiobutton_2.pack()

#listbox

def listbox_Selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ["John", "Smith"]
for name in name_list:
    my_listbox.insert(0,name)

my_listbox.bind('<<ListboxSelect>>',listbox_Selected)
my_listbox.pack()






window.mainloop()
