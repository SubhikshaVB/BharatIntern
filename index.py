import tkinter as tk
from tkinter import ttk
import difflib

# Sample DICTIONARY (Bigger dictionary can be used by importing nltk or pdfplumber)
dictionary =  ["a","is","are","girl","boy","house","blue","red","orange","green","this","the","that","colour","apple","fruits","dress","wearing"]

# Function for AUTOCORRECT
def autocorrect_text():
    input_text = input_entry.get("1.0", tk.END).strip()
    words = input_text.split()
    corrected_words = []

    for word in words:
        closest_match = difflib.get_close_matches(word, dictionary, n=1, cutoff=0.75)
        corrected_words.append(closest_match[0] if closest_match else word)

    corrected_text = " ".join(corrected_words)
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", corrected_text)

# Function to CLEAR TEXT
def clear_text():
    input_entry.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    
# Creating TKINTER WINDOW
root = tk.Tk()
root.title("Subhi's Auto-Correct Tool")
root.geometry('1600x900')
root.configure(bg="#856ff8")

# Styling the BUTTON and LABEL
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 20), foreground="black", background="blue", padding=5)
style.configure("TLabel", font=("Helvetica", 20, "bold"), foreground="black")

# Input
input_label = ttk.Label(root, text="Enter your text:",anchor="w", justify="left")
input_label.pack(pady=5)
input_entry = tk.Text(root, height=10, width=80,font=30)
input_entry.pack(padx=10, pady=5)

# Button for AUTOCORRECT
correct_button = ttk.Button(root, text="Auto-Correct", command=autocorrect_text)
correct_button.pack(pady=5)

# Output
output_label = ttk.Label(root, text="Corrected text:", anchor="w",  justify="right")
output_label.pack(pady=5)
output_text = tk.Text(root, height=10, width=80,font=30)
output_text.pack(padx=10, pady=5)

# Button for CLEAR
clear_button = ttk.Button(root, text="Clear", command=clear_text, style="TButton")
clear_button.pack(pady=5)

root.mainloop()
