from tkinter import *


class WindowNow:
    def __init__(self, width=0, height=0, title='Now Window'):
        self.root = Tk()
        if width != 0 and height != 0:
            self.root.geometry(f'{width}x{height}')
        self.root.title(title)

        self.lbl = Label(self.root, text='0', font=('Arial Bond', 50))
        self.btn = Button(self.root, text='Жмакни!', font=('Arial Bond', 50), command=self.cnt)

        self.temp = 0

        self.draw_vgt()

    def run(self):
        self.root.mainloop()

    def draw_vgt(self):
        self.lbl.pack()
        self.btn.pack()

    def cnt(self):
        self.temp += 1
        self.lbl.configure(text=self.temp)