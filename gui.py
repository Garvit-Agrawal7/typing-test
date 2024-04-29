from tkinter import *
import customtkinter as ctk
import time


class App:
    def __init__(self, word_list):
        self.start_time = None
        self.expected_text = ""
        for word in word_list:
            self.expected_text += word+" "

        # Initialising Tkinter
        self.font = ('Poppins', 14)
        self.screen = Tk()
        self.screen.title("Typing Speed Test")
        self.screen.config(padx=100, pady=25)

        # Adding keyboard layout
        self.canvas = Canvas(width=1024, height=768)
        keyboard = PhotoImage(file='keybr.png')
        self.canvas.create_image(540, 540, image=keyboard)
        self.canvas.grid(row=7, column=5, columnspan=5, rowspan=2)

        # Word list Label
        self.text_label = Label(self.screen, text=word_list)
        self.text_label.configure(font=self.font)
        self.text_label.grid(row=6, column=5)

        # Typing input
        self.typing_entry = Entry()
        self.typing_entry.grid(column=5, row=7)
        self.typing_entry.configure(highlightthickness=2, highlightcolor="#0C0C0C", bg="#F0EBE3", font=self.font,
                                    width=50)

        # Start and stop test
        start_button = Button(self.screen, text="Start Typing Test", command=self.start_typing_test)
        start_button.grid(column=4, row=8)
        end_button = Button(self.screen, text="End Typing Test", command=self.end_typing_test)
        end_button.grid(column=6, row=8)

        # Typing Test result
        self.feedback_label = Label(self.screen, text="")
        self.feedback_label.grid(column=5, row=8)

        self.screen.mainloop()

    def start_typing_test(self):
        """Starts typing test"""
        self.typing_entry.focus()
        self.start_time = time.time()
        self.text_label.config(text=self.expected_text)

    def end_typing_test(self):
        """Ends typing test"""
        end_time = time.time()
        time_taken = end_time - self.start_time
        input_text = self.typing_entry.get()
        correct_chars = sum(1 for a, b in zip(input_text, self.expected_text) if a == b)
        accuracy = (correct_chars / len(self.expected_text)) * 100
        typing_speed = (len(input_text) / 5) / (time_taken / 60)  # Assuming average word length is 5 characters
        self.feedback_label.config(text=f"Accuracy: {accuracy:.2f}%\nTyping Speed: {typing_speed:.2f} WPM")
