from tkinter import *
from notebook import NoteBook
import menu.file as File
import menu.help as Help

app = Tk()
app.title("Notepad")
app.geometry("600x400+400+300")
app.iconbitmap("icon.ico")
app.resizable(False, False)


notebook = NoteBook(app)
notebook.pack()

notebook.create_tab("note.txt", "This is Notepad!")

notebook.create_tab("hello.txt", "Hello, World!")


main_menu = Menu()

file_menu = File.File(app, notebook)
main_menu.add_cascade(label="File", menu=file_menu)

help_menu = Help.Help(app)
main_menu.add_cascade(label="Help", menu=help_menu)

app.config(menu=main_menu)


app.mainloop()
