from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class File(Menu):
    def __init__(self, app, notebook, **kwargs):
        super().__init__(tearoff=0, **kwargs)

        self.app = app
        self.notebook = notebook

        self.add_command(label="New", command=self.new, accelerator="Ctrl+N")
        self.add_command(label="Save", command=self.save, accelerator="Ctrl+S")
        self.add_command(label="Save as", command=self.saveas, accelerator="Ctrl+Shift+S")
        self.add_command(label="Open", command=self.open, accelerator="Ctrl+O")
        self.add_command(label="Close", command=self.close, accelerator="Ctrl+Shift+C")
        self.add_separator()
        self.add_command(label="Exit", command=self.exit, accelerator="Alt+F4")

        app.bind("<Control-n>", self.new)
        app.bind("<Control-s>", self.save)
        app.bind("<Control-N>", self.new)
        app.bind("<Control-S>", self.save)
        app.bind("<Control-Shift-S>", lambda save: self.saveas("Save as"))
        app.bind("<Control-o>", self.open)
        app.bind("<Control-O>", self.open)
        app.bind("<Control-Shift-C>", self.close)
        app.protocol("WM_DELETE_WINDOW", self.exit)


    def new(self, *args):
        self.notebook.create_tab("new file", "")


    def save(self, *args):
        if self.notebook.get_data()["path"] == None or self.notebook.get_data()["path"] == "":
            return self.saveas(save="Save")
        else:
            file = self.notebook.get_data()["path"]
            self.notebook.text_save(file)

            path = file

            with open(file, "w") as file:
                file.write(self.notebook.get_text())
            return path


    def saveas(self, save="Save as", *args):
        filename = self.notebook.get_name()
        if filename.endswith("*"):
            filename = filename[:len(filename)-1]

        file = filedialog.asksaveasfilename(
            title=f"{save} file:",
            defaultextension=".txt",
            initialfile=filename,
            confirmoverwrite=True,
            filetypes=[("Text Files", "*.txt"), ("Custom Text Files", "*.txtx"), ("All Files", "*")]
        )

        if file != "":
            self.notebook.text_save(file)

            path = file

            with open(file, "w") as file:
                file.write(self.notebook.get_text())

            return path
        return ""


    def open(self, *args):
        file = filedialog.askopenfilename(
            title="Open file:",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("Custom Text Files", "*.txtx"), ("All Files", "*")]
        )

        if file != "":
            self.notebook.create_tab(
                file.split("/")[len(file.split("/")) - 1],
                open(file, "r").read(),
                file,
                True
            )


    def close(self, *args):
        close = True

        if self.notebook.get_data()["save"] == False:
            file_save = messagebox.askyesnocancel("File", "Save file?")

            if file_save == None:
                close = False

            elif file_save == True:
                if self.save() == "":
                    close = False

            elif file_save == False:
                pass

        if close:
            self.notebook.delete_tab(self.notebook.current_tab())


    def exit(self, *args):
        quitbool = True
        tabs = 0

        for tab in range(0, self.notebook.all_tabs()):
            self.notebook.set_tab(tab)
            if self.notebook.get_data()["save"] == False:
                tabs += 1

        if tabs > 0:
            files_save = messagebox.askyesnocancel("Files", "Save files?")

            if files_save == None:
                quitbool = False

            elif files_save == True:
                for tab in range(self.notebook.all_tabs()):
                    self.notebook.set_tab(tab)
                    if self.save() == "":
                        quitbool = False
                        break

            elif files_save == False:
                pass


        if quitbool:
            quit()














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