import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import FloatEntry
from math import pi

def main():
    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.master.title("Area of a Circle")
    frm_main.pack(padx=(30), pady=(40), fill=tk.BOTH, expand=1)
    createWindow(frm_main)
    root.mainloop()

def createWindow(frame):
    lbl_radius = Label(frame, text="Radius: ")
    ent_radius = FloatEntry(frame, width=10, lower_bound=0, upper_bound=100)
    lbl_units = Label(frame, text="cm")
    lbl_area = Label(frame, text="Area: ")
    lbl_result = Label(frame, text="")
    lbl_area_units = Label(frame, text="cm^2")
    
    btnClear = Button(frame, text="Clear", command=lambda: clear(ent_radius, lbl_result))

    lbl_radius.grid(row=0, column=0, padx=5, pady=(5,30))
    ent_radius.grid(row=0, column=1, padx=5, pady=(5,30))
    lbl_units.grid(row=0, column=2, padx=5, pady=(5,30))
    lbl_area.grid(row=1, column=0, padx=5, pady=5)
    lbl_result.grid(row=1, column=1, padx=5, pady=5)
    lbl_area_units.grid(row=1, column=2, padx=5, pady=5)
    btnClear.grid(row=2, column=1, padx=5, pady=5)

    def calculateArea(event):
        try:
            radius = float(ent_radius.get())
            max_radius = 100
            if radius < 0 or radius > max_radius:
                raise ValueError
            lbl_result.config(text=f"{pi * radius ** 2:.2f}")
        except ValueError:
            lbl_result.config(text="Please enter a value between 0 and 100")

    def clear(entry, label):
        btnClear.focus()
        ent_radius.clear()
        lbl_result.config(text="")

    ent_radius.bind("<KeyRelease>", calculateArea)

    btnClear.config(command=lambda: clear(ent_radius, lbl_result))

    ent_radius.focus()

if __name__ == "__main__":
    main()
            