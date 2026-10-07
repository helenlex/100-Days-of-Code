import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height= 300)
window.config(padx= 20, pady= 20) # more padding


#label

my_label = tkinter.Label(text= "I Am A Label", font=("Arial", 24, "bold"))
#my_label.pack()
my_label["text"] = "New Text"
#my_label.place(x= 0, y = 0)
my_label.grid(column= 0, row = 0)
my_label.config(padx= 50, pady= 50)


#button

def button_clicked():
    my_label["text"] = input.get()



button = tkinter.Button(text = "Click Me", command = button_clicked)
#button.pack()
button.grid(column=1, row=1)

#entry

input = tkinter.Entry(width= 10)
#input.pack()
input.grid(column=3, row=2)

new_button = tkinter.Button(text = "New Button")
new_button.grid(column=2, row= 0)








window.mainloop()