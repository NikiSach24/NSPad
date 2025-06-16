from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class Help(Menu):
    def __init__(self, app, **kwargs):
        super().__init__(tearoff=0, **kwargs)

        self.app = app
        self.tab = 0

        self.add_command(label="About", command=self.about)
        self.add_command(label="How to use?")


    def about(self):
        win = Toplevel()
        win.title("About program")
        win.geometry(f"350x150+{self.app.winfo_x() + self.app.winfo_width()//2 - 175}+{self.app.winfo_y() + self.app.winfo_height()//2 - 75}")
        win.iconbitmap("icon.ico")
        win.resizable(False, False)

        name = Label(win, text="NotePad ++", font=("Arial", 20))
        name.pack()

        dev = Label(win, text="NikiSach24", font=("Arial", 15))
        dev.pack()

        self.tab = 0

        canvas = Canvas(win, height=65, width=65)
        canvas.place(x=20, y=10)
        img = PhotoImage(file='icon.png', height=65, width=65)
        canvas.create_image(0, 0, anchor=NW, image=img, tags="img")
        canvas.tag_bind("img", "<Button-1>", self.NotAnEasterEgg)

        win.mainloop()


    def NotAnEasterEgg(self, *args):
        if self.tab >= 5:
            messagebox.showinfo("Easter Egg", "This isn't an Easter Egg!!!")
        self.tab += 1
















# win = Toplevel()
# # ["TXT", "TXTX", "Other"]
# # "Select the type of the future file:"
# win.title("New File")
# win.geometry(f"350x250+{self.app.winfo_x() + self.app.winfo_width()//2 - 175}+{self.app.winfo_y() + self.app.winfo_height()//2 - 125}")
# win.iconbitmap("icon.ico")
# win.resizable(False, False)
#
# text = Label(win, text="Select the type of\nnew file:", font=("Arial", 16), height=3)
# text.pack()
#
# txt_button = Button(win, text="TXT", height=1, width=6, font=("Arial", 22), command=lambda: self.new_txt(win))
# txt_button.place(x=5, y=100)
#
# txtx_button = Button(win, text="TXTX", height=1, width=6, font=("Arial", 22), command=lambda: self.new_txtx(win))
# txtx_button.place(x=175 - txtx_button.winfo_width() // 2, y=100)
# txtx_button.update()
# txtx_button.place(x=175 - txtx_button.winfo_width() // 2, y=100)
#
# other_button = Button(win, text="OTHER", height=1, width=6, font=("Arial", 22), command=lambda: self.new_other(win, text))
# other_button.place(x=345 - txtx_button.winfo_width(), y=100)
# other_button.update()
# other_button.place(x=345 - txtx_button.winfo_width(), y=100)
#
# win.mainloop()











# def new_txt(self, win):
#     win.destroy()
#
#
# def new_txtx(self, win):
#     win.destroy()
#
#
# def new_other(self, win, text):
#     text.configure(text="Select or type the\nnew file type:")
#
#     entry = Entry(win, font=("Arial", 22), width=8, justify=CENTER)
#     entry.place(x=175 - entry.winfo_width() // 2, y=100)
#     entry.update()
#     entry.place(x=175 - entry.winfo_width() // 2, y=175)
#
#     win.mainloop()