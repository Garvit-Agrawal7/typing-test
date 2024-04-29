from customtkinter import *
from PIL import Image


class App:
    def __init__(self, word_list):
        # Initializing Custom Tkinter
        self.app = CTk
        self.app.geometry('1280x720')
        self.app.title('Typing Speed Test')
        set_appearance_mode('light')
        self.schedule_function()

        # Word List
        n = 0
        for i in range(len(word_list)):
            n += len(word_list[i])
            if n * 7 >= 640:
                word_list.insert(i, "\n")
                n = 0
        self.words = " ".join(word_list)

        # Creating Image
        img = Image.open('keybr.png')
        self.image = CTkImage(img, size=img.size)
        self.my_label = CTkLabel(self.app, text="", image=self.image)
        self.my_label.place(x=640, y=500, anchor=CENTER)

        # Typing Test
        self.entry = CTkEntry(self.app, fg_color="#ebebeb", width=640, height=40, font=('Open Sans', 20))
        self.label = CTkLabel(self.app, text=self.words, width=640, font=('Open Sans', 20))
        self.label.place(x=640, y=200, anchor=CENTER)
        self.entry.place(x=640, y=300, anchor=CENTER)

        # Progress bar
        self.progressbar = CTkProgressBar(self.app, orientation="horizontal", width=600, progress_color="#F3D0D7", fg_color="#FAF9F6")
        self.progressbar.place(x=640, y=100, anchor=CENTER)

        self.app.mainloop()

    def update(self):
        progress = len(self.entry.get()) / len(self.words)
        self.progressbar.set(progress)
        print(progress)

    def schedule_function(self):
        self.update()
        self.app.after(100, self.schedule_function)
