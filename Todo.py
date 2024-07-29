import tkinter as tk
from tkinter import filedialog

def create_window():
    window = tk.Tk()
    window.title("Enhanced To-Do List")
    window.geometry("400x300")

    def add_task():
        task = entry.get()
        priority = priority_var.get()
        if task:
            listbox.insert(tk.END, f"{task} - Priority: {priority}")
            entry.delete(0, tk.END)

    def remove_task():
        selected_task_index = listbox.curselection()
        if selected_task_index:
            listbox.delete(selected_task_index)

    def mark_as_completed():
        selected_task_index = listbox.curselection()
        if selected_task_index:
            task = listbox.get(selected_task_index)
            listbox.delete(selected_task_index)
            listbox.insert(tk.END, f"{task} - Completed")

    def save_tasks():
        tasks = listbox.get(0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                for task in tasks:
                    file.write(task + "\n")

    def load_tasks():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    listbox.insert(tk.END, task.strip())

    entry = tk.Entry(window, width=30)
    entry.pack(pady=10)

    priority_var = tk.StringVar(value="Low")
    priority_frame = tk.Frame(window)
    priority_frame.pack(pady=5)

    tk.Label(priority_frame, text="Priority: ").pack(side=tk.LEFT)
    tk.Radiobutton(priority_frame, text="Low", variable=priority_var, value="Low").pack(side=tk.LEFT)
    tk.Radiobutton(priority_frame, text="Medium", variable=priority_var, value="Medium").pack(side=tk.LEFT)
    tk.Radiobutton(priority_frame, text="High", variable=priority_var, value="High").pack(side=tk.LEFT)

    listbox = tk.Listbox(window, width=50, height=10)
    listbox.pack(pady=10)

    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Add Task", command=add_task)
    add_button.grid(row=0, column=0, padx=5)

    remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
    remove_button.grid(row=0, column=1, padx=5)

    complete_button = tk.Button(button_frame, text="Complete Task", command=mark_as_completed)
    complete_button.grid(row=0, column=2, padx=5)

    save_button = tk.Button(button_frame, text="Save Tasks", command=save_tasks)
    save_button.grid(row=0, column=3, padx=5)

    load_button = tk.Button(button_frame, text="Load Tasks", command=load_tasks)
    load_button.grid(row=0, column=4, padx=5)

    window.mainloop()

if __name__ == "__main__":
    create_window()
