import time


class TypingTest:
    def __init__(self, entry, expected_text, result):
        self.typing_entry = entry
        self.start_time = 0
        self.expected_text = expected_text
        self.feedback_label = result

    def start_typing_test(self):
        """Starts typing test"""
        self.start_time = time.time()

    def end_typing_test(self):
        """Ends typing test"""
        end_time = time.time()
        time_taken = end_time - self.start_time
        input_text = self.typing_entry.get()
        correct_chars = sum(1 for a, b in zip(input_text, self.expected_text) if a == b)
        accuracy = (correct_chars / len(self.expected_text)) * 100
        typing_speed = (len(input_text) / 5) / (time_taken / 60)  # Assuming average word length is 5 characters
        self.feedback_label.configure(text=f"Accuracy: {accuracy:.2f}%\nTyping Speed: {typing_speed:.2f} WPM")
