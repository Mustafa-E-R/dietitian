from tkinter import *
from tkinter import ttk
import result_retriever as retriever

window = Tk()
window.title('The Dietitian')
window.config(padx=150, pady=100)

# Labels
weight_label = Label(window, text='Weight in KG').grid(row=0, column=0)
height_label = Label(window, text='Height in CM').grid(row=1, column=0)
age_label = Label(window, text='Age in YEARS').grid(row=2, column=0)
gender_label = Label(window, text='Gender').grid(row=3, column=0)
lifestyle_label = Label(window, text='Physical Activity').grid(row=4, column=0)

# Entries
wght = IntVar()
weight_entry = Scale(window, orient=HORIZONTAL, from_=40, to=120, variable=wght).grid(row=0, column=1, columnspan=6,
                                                                                      sticky='we')
hght = IntVar()
height_entry = Scale(window, orient=HORIZONTAL, from_=140, to=220, variable=hght).grid(row=1, column=1, columnspan=6,
                                                                                       sticky='we')

agt = IntVar()
age_entry = Scale(window, from_=16, to=120, orient=HORIZONTAL, variable=agt).grid(row=2, column=1, columnspan=6,
                                                                                  sticky='we')

gender_var = StringVar()
gender_entry = ttk.Combobox(window, textvariable=gender_var, values=['Female', 'Male']).grid(row=3, column=1,
                                                                                             columnspan=2, sticky='we',
                                                                                             pady=10)

lifestyle_var = StringVar()
lifestyle_entry = ttk.Combobox(window, textvariable=lifestyle_var,
                               values=retriever.lifestyles).grid(row=4, column=1, columnspan=4, sticky='we', pady=7)

# Buttons
get_results_button = Button(window, text='Get Results', borderwidth=5,
                            command=lambda: retriever.get_results(window, wght, hght, agt, gender_var, lifestyle_var)
                            ).grid(row=6, column=1, pady=7)
print(type(agt))
window.mainloop()
