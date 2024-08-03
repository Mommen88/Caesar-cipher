import tkinter as tk
from tkinter import messagebox

# Function to perform the Caesar cipher encryption/decryption
def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

# Function to handle the encryption/decryption action
def perform_action(action):
    text = text_entry.get("1.0", "end-1c")  # Get the text from the input field
    try:
        shift = int(shift_entry.get())  # Get the shift value from the input field
        if shift < 0 or shift > 25:  # Validate shift value
            messagebox.showerror("Error", "Shift value must be between 0 and 25.")
            return
        if action == "encrypt":
            result = caesar_cipher(text, shift)
        elif action == "decrypt":
            result = caesar_cipher(text, -shift)
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, result)  # Display the result
    except ValueError:
        messagebox.showerror("Error", "Invalid shift value. Please enter an integer between 0 and 25.")

# Function to clear all input and output fields
def clear_fields():
    text_entry.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)
    result_entry.delete("1.0", tk.END)

# Setting up the main application window
app = tk.Tk()
app.title("Caesar Cipher")

# Adding the title label
title_label = tk.Label(app, text="Caesar Cipher", font=("Arial", 16))
title_label.pack(pady=10)

# Adding the text input label and text box
text_label = tk.Label(app, text="Enter text:")
text_label.pack()
text_entry = tk.Text(app, height=5, width=40)
text_entry.pack(pady=5)

# Adding the shift input label and entry box
shift_label = tk.Label(app, text="Enter shift:")
shift_label.pack()
shift_entry = tk.Entry(app)
shift_entry.pack(pady=5)

# Adding the encrypt button
encrypt_button = tk.Button(app, text="Encrypt", command=lambda: perform_action("encrypt"))
encrypt_button.pack(pady=5)

# Adding the decrypt button
decrypt_button = tk.Button(app, text="Decrypt", command=lambda: perform_action("decrypt"))
decrypt_button.pack(pady=5)

# Adding the result label and text box
result_label = tk.Label(app, text="Result:")
result_label.pack()
result_entry = tk.Text(app, height=5, width=40)
result_entry.pack(pady=5)

# Adding the clear button
clear_button = tk.Button(app, text="Clear", command=clear_fields)
clear_button.pack(pady=10)

# Adding the quit button
quit_button = tk.Button(app, text="Quit", command=app.quit)
quit_button.pack(pady=10)

# Starting the main application loop
app.mainloop()
