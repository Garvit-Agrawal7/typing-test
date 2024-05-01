import customtkinter as ctk
from PIL import Image

from typing_test import TypingTest


class App(ctk.CTk):
    def __init__(self, word_list):
        super().__init__()
        # Initializing Custom Tkinter
        self.geometry('1280x720')
        self.title('Typing Speed Test')
        ctk.set_appearance_mode('light')

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
        self.image = ctk.CTkImage(img, size=img.size)
        self.my_label = ctk.CTkLabel(self, text="", image=self.image)
        self.my_label.place(x=640, y=500, anchor=ctk.CENTER)

        # Typing Test
        self.entry = ctk.CTkEntry(self, fg_color="#ebebeb", width=640, height=40, font=('Open Sans', 20))
        self.label = ctk.CTkLabel(self, text=self.words, width=640, font=('Open Sans', 20))
        self.label.place(x=640, y=200, anchor=ctk.CENTER)
        self.entry.place(x=640, y=300, anchor=ctk.CENTER)

        # Progress bar
        self.progressbar = ctk.CTkProgressBar(self, orientation="horizontal", width=600, progress_color="#F3D0D7", fg_color="#FAF9F6")
        self.progressbar.place(x=640, y=100, anchor=ctk.CENTER)

        # Feedback, typing test result
        self.result = ctk.CTkLabel(self, text="", font=('Open Sans', 20))
        self.result.place(x=640, y=50, anchor=ctk.CENTER)

        # Typing Test Object
        self.test = TypingTest(entry=self.entry, expected_text=self.words.strip('\n'), result=self.result)

        self.time_label = ctk.CTkLabel(self, text="", font=('Open Sans', 100))
        self.time_label.place(x=640, y=360, anchor=ctk.CENTER)

        self.schedule_function()
        self.after(2, self.start_test)
        self.mainloop()

    def update(self):
        progress = len(self.entry.get().strip()) / len(self.words.strip())
        self.progressbar.set(progress)
        if progress == 1:
            self.test.end_typing_test()

    def schedule_function(self):
        self.update()
        self.after(100, self.schedule_function)

    def start_test(self):
        self.entry.focus()
        self.test.start_typing_test()
