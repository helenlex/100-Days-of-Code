from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window["padx"] = 20
window["pady"] = 20



# initialising objects
is_equal_to = Label(text = "is equal to")
miles = Label(text = "Miles")
km = Label(text = "Km")
miles_input = Entry(width= 20)
km_result = Label(text = "")

#function

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result["text"] = f"{km}"

calculate_button = Button(text= "Calculate", command= calculate)


# viewing them temporarily
#is_equal_to.pack()
# miles.pack()
# km.pack()
# miles_input.pack()
# km_result.pack()
# calculate_button.pack()


#laying out objects in a grid
is_equal_to.grid(column=0, row= 1)
miles.grid(column=2, row=0)
km.grid(column=2, row=1)
miles_input.grid(column=1, row=0)
km_result.grid(column=1, row=1)
calculate_button.grid(column=1, row=2)


window.mainloop()