import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height= 300)


#label

my_label = tkinter.Label(text= "I Am A Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"


#button

def button_clicked():
    my_label["text"] = input.get()



button = tkinter.Button(text = "Click Me", command = button_clicked)
button.pack()

#entry

input = tkinter.Entry(width= 10)
input.pack()








window.mainloop()