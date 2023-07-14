from tkinter import *
from translator import *
from customtkinter import *


set_appearance_mode('dark')
set_default_color_theme('green')

def print_table(final):
    for i in final:
        if i == ' ':
            continue
        else:
            my_tableText.insert(END, f'{i} - \n')
            my_valueText.insert(END, f'{bbylist.mapping[i]}\n')
 


def translates():
    my_wordText.configure(state = NORMAL)
    my_valueText.configure(state = NORMAL)
    my_tableText.configure(state = NORMAL)

     # Check if the my_wordText widget is empty before deleting its contents
    if len(my_wordText.get()) > 0:
        my_wordText.delete(0, END)
        my_valueText.delete(0.0, END)
        my_tableText.delete(0.0, END)
    
    my_wordText.configure(font=('Tagalog Doctrina 1593', 34, 'bold'))

    input_text = (my_text.get())
    input_text = input_text.lower()
    print(f'\n\nText input: {input_text}')

    new = pagpapantig(input_text)
    final = stringToArray(new)
    baybayinchars = fetchbaybayinchars(final)

    print(f'Baybayin syllabication: {final}')
    print(f'Mapping equivalence: {baybayinchars}\n\n')

    result = ''.join(baybayinchars)
    my_wordText.insert(END, result)
    my_wordText.bind("<Key>", "Break")
    my_valueText.bind("<Key>", "Break")
    my_tableText.bind("<Key>", "Break")
    print_table(final)


def multiple_yview(*args):
    my_valueText.yview(*args)
    my_tableText.yview(*args)


root = CTk()
root.geometry("650x500")
root.title("Translator")


text_var = StringVar(value="CTkLabel123")
# Text
my_frame = CTkFrame(root, fg_color='gray10')
my_frame.place(relx=0.5, y=100, anchor=CENTER)

my_text = CTkEntry(my_frame, height=2.5, width=350, placeholder_text = 'Tagalog Word', placeholder_text_color='gray75')
my_text.grid(row=0, column=0, pady=20, padx= 20)
my_text.configure(font=('Normal', 32, 'bold'))

my_button = CTkButton(my_frame,height=45, width = 150, corner_radius = 8,text= "Translate", command = translates)
my_button.grid(row=0, column=1, pady=15, padx=40)
my_button.configure(font=('Normal', 25, 'normal'))

my_wordText = CTkEntry(my_frame, height=2.5, width=350, placeholder_text = 'Baybayin Translation', placeholder_text_color='gray75')
my_wordText.grid(row=1, column=0, pady=20, padx= 20)
my_wordText.configure(font=('Normal', 32, 'bold'))

# Table
my_frame1 = CTkFrame(root, fg_color = 'gray10')
my_frame1.place(relx=0.5, y=350, anchor=CENTER)

scrollable_frame = CTkScrollbar(root)
scrollable_frame.pack(side=RIGHT, fill=Y)


my_tableText = CTkTextbox(my_frame1, height=250, width=175, font=('default', 32, 'bold'), yscrollcommand= scrollable_frame.set, state=DISABLED)
my_tableText.grid(row=0, column=0, pady=20, padx=25)

my_valueText = CTkTextbox(my_frame1, height=250, width=350, font=('Tagalog Doctrina 1593', 38, 'bold'), yscrollcommand= scrollable_frame.set,state = DISABLED)
my_valueText.grid(row=0, column=1, pady=20, padx=25)


scrollable_frame.configure(command=multiple_yview)

root.mainloop()