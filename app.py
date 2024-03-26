import tkinter as tk
from tkinter import messagebox
import random
import string
import threading

def generate_password_async():
    length = int(length_entry.get())
    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4 characters.")
        return
    threading.Thread(target=generate_password, args=(length,)).start()

def generate_password(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    root.after(0, update_password_entry, password)

def update_password_entry(password):
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

def copy_to_clipboard():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_async)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=2, column=0, padx=10, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

root.mainloop()
