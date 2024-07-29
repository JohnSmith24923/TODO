import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Enhanced To-Do List")
    window.geometry("400x300")
    window.mainloop()

if __name__ == "__main__":
    create_window()