import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        pass


# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create input and button widgets
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=1, column=0, padx=10, pady=10)

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
