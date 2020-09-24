#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import *

from Application import Application

def main():
    root = Tk()
    root.title("The Horoscope")
    app = Application(root)
    app.pack()

    def submit(*args):
        app.on_submit()
        pass

    def closeWindow(*args):
        root.destroy()
        pass

    root.bind("<Escape>", closeWindow)
    root.bind("<Return>", submit)

    root.mainloop()
    pass

if __name__ == "__main__":
    main()
    pass