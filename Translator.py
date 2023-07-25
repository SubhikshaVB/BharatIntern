from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES

root= Tk()
root.title("Subhi's Translator Tool")
root.geometry('1600x900')
root.configure(bg="#FFC0CB")

Label(root, text="Language Translator", font='arial 20 bold', fg='black', bg='white').pack()

input_text = Text(root,font='arial 14', height=11,wrap=WORD, padx=5,pady=5, width=30,fg='black', bg='white',borderwidth=4,highlightthickness=2, highlightbackground="black")
input_text.place(x=600,y=100)

output_text = Text(root,font='arial 14', height=11,wrap=WORD, padx=5,pady=5, width=30,fg='black', bg='white',borderwidth=4,highlightthickness=2, highlightbackground="black")
output_text.place(x=600,y=500)

language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values=('English','Hindi','Dutch','Bengali','Urdu','Tamil','Telugu','French','Spanish','Japanese'))
src_lang.place(x=700,y=60)
src_lang.set('Select Input Language')
src_lang.configure(state='readonly')

dest_lang = ttk.Combobox(root, values=('English','Hindi','Dutch','Bengali','Urdu','Tamil','Telugu','French','Spanish','Japanese'))
dest_lang.place(x=700,y=450)
dest_lang.set('Select Output Language')
dest_lang.configure(state='readonly')

def Translate():
    translator= Translator()
    translated = translator.translate(text=input_text.get(1.0,END),src = src_lang.get(), dest=dest_lang.get())
    output_text.delete(1.0,END)
    output_text.insert(END,translated.text)
    
trans_btn = Button(root, text='Translate', font= 'arial 12 bold',pady=5,command= Translate ,fg='black', bg='white')
trans_btn.place(x=670,y=380)

def Clear():
    input_text.delete(0.0,END)
    output_text.delete(1.0,END)
    dest_lang.set('Choose language')


# Button for CLEAR
clear_btn = Button(root, text="Clear",font='arial 12 bold',pady=5, command= Clear)
clear_btn.place(x=800,y=380)

root.mainloop()
