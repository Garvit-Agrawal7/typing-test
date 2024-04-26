from tkinter import *


class App:
    def __init__(self, word_list):
        self.font = ('Poppins', 20)
        self.screen = Tk()
        self.screen.title("Typing Speed Test")

        self.canvas = Canvas(width=1080, height=720)
        keyboard = PhotoImage(file='keybr.png')
        self.canvas.create_image(540, 540, image=keyboard)
        self.canvas.grid(row=0, column=1)

        words = Label(text=word_list, font=self.font)
        words.grid(row=0, column=1)

        self.screen.mainloop()

