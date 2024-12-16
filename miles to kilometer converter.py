from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result.config(text=f"{km}")

window = Tk()
window.title("Miles to kilomter converter")
window.minsize(width = 500, height=500)
window.config(padx=100,pady=200)

#Add the entry field
miles_input = Entry()
miles_input.grid(column=1,row=0)

#Add the miles label
miles_label = Label(text = "Miles")
miles_label.grid(column=2, row = 0)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0,row=1)

kilometer_result = Label(text = "0")
kilometer_result.grid(column=1,row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)




window.mainloop()