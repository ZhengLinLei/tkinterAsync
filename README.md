# TkinterAsync

[![Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Run your own code with [Tkinter Tcl/Tk](https://docs.python.org/3/library/tkinter.html) Python module loop at the same time

PIP package install:
```
pip install tkinterAsync
```

Pypi [https://pypi.org/project/tkinterAsync/](https://pypi.org/project/tkinterAsync/)



## Example code

The code is inside `test/example.py` file:
```Python

import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))  # LOCATE INTO ROOT PATH


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


```


### How to use?

Create your Tkinter default function or class:
```Python

import tkinter as tk


def App():

    # root = tk.Tk() <------ YOU CAN REMOVE THIS LINE

    root.title('Example')   # -----------------> ONLY NEED THE PROCCESS AND LOGIC OF THE APPLICATION
    root.maxsize(1000, 400)

    # root.mainloop() <------ YOU CAN REMOVE THIS LINE
    
```

But in this case you don't need to import Tkinter, beacause the module pass the Tkinter module into the function
```Python

def App(root, tk, ttk): # <------ LOOK HERE! CHANGE THE NAME IF YOU WANT <app>, <tkinter>, <ttk>

    root.title('Example')
    root.maxsize(1000, 400)

```

And then call the class passing the function like params
```Python
from src.tkinterAsync import Tkinter
# or
# from tkinterAsync import Tkinter

MyApp = Tkinter(App) # <------ PASSING THE FUNCTION

```


## Found some issues?

Let us know when you found an issue

[Github - Issues](https://github.com/ZhengLinLei/tkinterAsync/issues)




### Love this repo? Give us a star ⭐

<a href="./">
  <img src="https://img.shields.io/badge/TkinterAsync-Rate-blue">
</a>