import tkinter as tk
from tkinter import*
import affine as affine
import railfence as railfence
import autokey as autokey
def update_key_label(*args):
    cipher = cipher_var.get()
    if cipher == 'affine':
        key_type_label.config(text="Type Integer: a/b")
    elif cipher == 'auto key':
        key_type_label.config(text="Type Integer:key")
    elif cipher == 'railence':
        key_type_label.config(text="Type Integer rails")

def process_text():
    text = text_entry.get("1.0", "end-1c")
    mode = mode_var.get()
    cipher = cipher_var.get()
    if(key_entry1.get()!=''):
        if cipher == 'affine':
            a = int(key_entry1.get())
            b = int(key_entry2.get())
            if mode == 'encrypt':
                result = affine.affine_encryption(text, a,b)
            elif mode == 'decrypt':
            #l1,l2=affine.most_two_letters_used(text)
            #a,b=affine.getKey(l1,l2)
                result = affine.affine_decryption(text, a,b)
        elif cipher == 'auto key':
            key = key_entry1.get()
            if mode == 'encrypt':
                result = autokey.autokey_encryption(text, key)
            elif mode == 'decrypt':
                result =autokey.autokey_decryption(text, key)
        elif cipher == 'railfence':
            key = int(key_entry1.get())
            if mode == 'encrypt':
                result = railfence.railfence_encryption(text, key)
            elif mode== 'decrypt':
                result = railfence.railfence_decryption(text, key)

        result_text.delete("1.0", "end")
        result_text.insert("1.0", result)
root = tk.Tk()
root.title("Cryptography")
# Text entry
text_label = tk.Label(root, text="Enter text:")
text_label.pack()
text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()
# Choose cipher
cipher_label = tk.Label(root, text="Choose cipher:")
cipher_label.pack()
cipher_var = tk.StringVar()
cipher_var.set('affine')  # Default cipher
cipher_option = tk.OptionMenu(root, cipher_var, 'affine', 'auto key', 'railfence', command=update_key_label)
cipher_option.pack()
# Choose mode (Encrypt/Decrypt)
mode_label = tk.Label(root, text="Choose mode:")
mode_label.pack()
mode_var = tk.StringVar()
mode_var.set('encrypt')  # Default mode
mode_option = tk.OptionMenu(root, mode_var, 'encrypt', 'decrypt')
mode_option.pack()
# Enter key
key_label = tk.Label(root, text="Enter key:")
key_label.pack()
key_entry1 = tk.Entry(root)
key_entry2= tk.Entry(root)
key_entry1.pack()
key_entry2.pack()
# Key type label
key_type_label = tk.Label(root, text="Key Type: Integer")
key_type_label.pack()
# Process button
process_button = tk.Button(root, text="Run", command=process_text)
process_button.pack()
# Result text
result_text = tk.Text(root, height=5, width=50)
result_text.pack()
root.mainloop()