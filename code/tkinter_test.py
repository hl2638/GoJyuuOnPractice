from tkinter import *

window = Tk()
window.title("My Title")
# Background frame.
frm_BG = Frame(master=window, borderwidth=10, padx=50, pady=50, bg="#34A2FE")
frm_BG.pack(expand=True, fill=BOTH)
btn_b = Button(text="Button", master=frm_BG).grid(row=0, column=0)
window.mainloop()