import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


from src.tkinterAsync import Tkinter

# TKINTER GUI
def gui(root, tk, ttk):
    root.title('Title example')
    root.geometry('300x300')

    root.resizable(0, 0)

    button = tk.Button(root, text = 'Alert', padx = 25, cursor = 'hand2', command = lambda : print('Hello World!'))
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# CREATE VARIABLE

root = Tkinter(gui)


# AFTER RUNNING TKINTER, THE PYTHON MUST RUN THE CODE BELOW AT THE SAME TIME

print('Running this after Tkinter')

for i in range(1000):
    print(i)
