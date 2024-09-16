import tkinter as tk
from tkinter import scrolledtext
from app.assistant import Assistant
import threading

class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry("500x400")

        # Text display area
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 10))
        self.text_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Entry widget for user input
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10, padx=10, fill=tk.X)
        self.entry.bind("<Return>", self.process_input)

        # Start Assistant Button
        self.start_button = tk.Button(root, text="Start Assistant", command=self.start_assistant_thread)
        self.start_button.pack(pady=10)

        # Stop Assistant Button
        self.stop_button = tk.Button(root, text="Stop Assistant", command=self.stop_assistant_thread)
        self.stop_button.pack(pady=5)
        self.stop_button["state"] = tk.DISABLED

        self.assistant = Assistant()
        self.assistant_thread = None

    def start_assistant_thread(self):
        self.assistant_thread = threading.Thread(target=self.assistant.start)
        self.assistant_thread.start()
        self.start_button["state"] = tk.DISABLED
        self.stop_button["state"] = tk.NORMAL
        self.update_text_area("Voice Assistant Started...")

    def stop_assistant_thread(self):
        if self.assistant:
            self.assistant.active = False
            self.assistant_thread.join()
            self.update_text_area("Voice Assistant Stopped.")
            self.start_button["state"] = tk.NORMAL
            self.stop_button["state"] = tk.DISABLED

    def process_input(self, event):
        command = self.entry.get()
        self.entry.delete(0, tk.END)
        response = self.assistant.process_command(command)
        self.update_text_area(f"You: {command}")
        self.update_text_area(f"Assistant: {response}")

    def update_text_area(self, text):
        self.text_area.insert(tk.END, text + "\n")
        self.text_area.yview(tk.END)

def start_gui():
    root = tk.Tk()
    gui = VoiceAssistantGUI(root)
    root.mainloop()
