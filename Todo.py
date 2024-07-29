import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Enhanced To-Do List")
    window.geometry("400x300")

    def add_task():
        task = entry.get()
        if task:
            listbox.insert(tk.END, task)
            entry.delete(0, tk.END)

    entry = tk.Entry(window, width=30)
    entry.pack(pady=10)

    listbox = tk.Listbox(window, width=50, height=10)
    listbox.pack(pady=10)

    add_button = tk.Button(window, text="Add Task", command=add_task)
    add_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_window()