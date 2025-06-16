from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook

class NoteBook(Notebook):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.__list_name = []
        self.__list_text = []
        self.__list_data = []
        self.__list_obj = []
        self.__list_obj_text = []
        self.__list_obj_frame = []


    def create_tab(self, name, text, path="", save=False):
        self.__list_name.append(name)
        self.__list_data.append({"path": path, "save": save})

        frame = Frame(self)
        frame.pack()
        self.__list_obj_frame.append(frame)

        scrtext = ScrolledText(frame)
        scrtext.insert("1.0", text)
        scrtext.pack()
        self.__list_obj_text.append(scrtext)

        line = Frame(frame)
        line.pack()
        self.__list_obj_frame.append(line)

        self.add(frame, text=name)

        self.set_tab(self.all_tabs() - 1)

        self.__list_text.append(self.get_text())
        self.after(500, self.__text_change)


    def current_tab(self):
        selected = self.select()
        return self.index(selected)


    def delete_tab(self, index):
        self.forget(index)

        if len(self.tabs()) == 0:
            quit()

        del self.__list_name[index]
        del self.__list_text[index]
        del self.__list_data[index]
        del self.__list_obj_text[index]
        del self.__list_obj_frame[index]


    def get_obj_text(self):
        return self.__list_obj_text[self.current_tab()]


    def get_text(self):
        return self.__list_obj_text[self.current_tab()].get("1.0", END)


    def get_data(self):
        return self.__list_data[self.current_tab()]


    def get_name(self):
        return self.__list_name[self.current_tab()]


    def rename_tab(self, index, text):
        self.tab(index, text=text)
        self.__list_name[index] = text


    def all_tabs(self):
        return len(self.tabs())


    def set_tab(self, index):
        self.select(index)


    def __text_change(self):
        if self.__list_text[self.current_tab()] != self.get_text():

            if not self.__list_name[self.current_tab()].endswith("*"):
                self.rename_tab(
                    self.current_tab(),
                    f"{self.__list_name[self.current_tab()]}*"
                )
                self.__list_text[self.current_tab()] = self.get_text()
                self.__list_data[self.current_tab()]["save"] = False

        self.after(500, self.__text_change)


    def text_save(self, path):
        self.__list_data[self.current_tab()]["save"] = True
        self.__list_data[self.current_tab()]["path"] = path
        self.__list_text[self.current_tab()] = self.get_text()

        self.rename_tab(
            self.current_tab(),
            path.split("/")[len(path.split("/")) - 1]
        )








#data = {"name": "hello.txt", "text": "Hello, World!"}
#notebook = Notebook(app)
#notebook.pack()
#
#frame = Frame(notebook)
#frame.pack()
#
#text = ScrolledText(frame)
#text.pack()
#
#line = Frame(frame)
#line.pack()
#
#notebook.add(frame, text="note.txt")
#
#frame = Frame(notebook)
#frame.pack()
#
#text = ScrolledText(frame)
#text.pack()
#
#line = Frame(frame)
#line.pack()
#
#notebook.add(frame, text="hello.txt")
