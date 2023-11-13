from tkinter import *
import tkinter.messagebox
from tkinter.font import Font

root = Tk()
root.title('DkDTL.com - To Do List')
root.geometry("600x600")

m_font  = Font(
    family = "Terminal",
    size=30,
    weight="bold",

)
my_frame = Frame(root)
my_frame.pack(pady=15)

#List Box

my_list = Listbox(
    my_frame,
    font= m_font,
    width=30,
    height=7,
    bg="SystemButtonFace",
    bd=0,
    fg="#009999",
    highlightthickness=0,
    selectbackground="#009900",
    activestyle="none"
)


#
my_list.pack()

#Create List
stuff = ["Walk The Dog", "Sale something", "Arround The world",]
for i in stuff:
    my_list.insert(END, i)

#Create a Scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill= BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#
app_entry = Entry(root, font=("Halvetica", 24))
app_entry.pack(pady=15)

# Create a button
button_f =Frame(root)
button_f.pack()


#FUNCTION For Buttons
def add_note():
    pass

def delete_note():
    selected=my_list.curselection()
    my_list.delete(selected[0])

def completed_mark():
    pass

def uncross_mark():
    pass

#Button widget 
add_button=Button(root,text="Add Note",command=add_note)
# add_button.pack(pady=15, padx=15,side=tkinter.LEFT)
add_button.place(x=112,y=450)

delete_button=Button(root,text="Delete Note",command=delete_note)
# delete_button.pack(pady=15, padx=15, side=tkinter.LEFT, )
delete_button.place(x=187,y=450)

mark_button=Button(root,text="Completed Mark ",command=completed_mark)
# mark_button.pack(pady=15, padx=15,side=tkinter.LEFT,)
mark_button.place(x=272,y=450)

uncross_button=Button(root,text="Uncrossed Note ",command=uncross_mark)
# uncross_button.pack(pady=15, padx=15, side=tkinter.LEFT)
uncross_button.place(x=387,y=450)

#If we use method pack() then grid() method doesn't work 
#
# delete_button.grid(row=0,column=0)
# add_button.grid(row=0,column=1, padx=15)
# mark_button.grid(row=0,column=2)
# uncross_button.grid(row=0,column=3, padx=15)


root.mainloop()