from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

def convert():
    try:
        
        result_label.config(text=f"is equal to {(int(input.get()) * 1.60934):.2f} Km") #f-string formating for 2 decimal points {(result:.2f)}
        
    except:
        pass
   

#Entry
input = Entry(width=7)
# input.insert(END, "Enter Miles to Convert")
input.grid(column=1,row=1)

#Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

result_label = Label(text="is equal to 0 Km")
result_label.grid(column=1,row=2)
#Button
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=3)


window.mainloop()