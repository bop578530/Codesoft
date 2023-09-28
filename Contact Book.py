import tkinter as tk
from tkinter import messagebox

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    if name and phone:
        contact_list.insert(tk.END, f"{name}: {phone}")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter both name and phone number.")

# Function to delete a selected contact
def delete_contact():
    try:
        selected_contact = contact_list.get(contact_list.curselection())
        contact_list.delete(contact_list.curselection())
    except tk.TclError:
        messagebox.showwarning("Error", "No contact selected.")

# Create the main window
window = tk.Tk()
window.title("Contact Book")

# Labels and Entry fields
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

phone_label = tk.Label(window, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

# Add and Delete buttons
add_button = tk.Button(window, text="Add Contact", command=add_contact)
add_button.pack()

delete_button = tk.Button(window, text="Delete Contact", command=delete_contact)
delete_button.pack()

# Contact list
contact_list = tk.Listbox(window)
contact_list.pack()

# Start the GUI event loop
window.mainloop()
