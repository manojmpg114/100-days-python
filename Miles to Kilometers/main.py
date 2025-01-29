from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

def convert():
    try:
        # return int(input.get() * 1.60934)
        # result_label.config(text=f"is equal to {int(input.get() * 1.60934)} Km")
        result_label.config(text=input.get())
        # result_label.config(text= str(input.get() * 1.60934))
    except:
        pass
    # return int(input.get() * 1.60934)
    # result_label.config(text="TESTER")

#Entry
input = Entry(width=30)
input.insert(END, "Enter Miles to Convert")
input.grid(column=1,row=1)

#Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

result_label = Label()
result_label.grid(column=1,row=2)
#Button
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=3)


window.mainloop()