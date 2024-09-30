import tkinter as tk
from tkinter import scrolledtext
import spacy

# Load spaCy English language model
nlp = spacy.load("en_core_web_sm")

class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        
        # Center the window on the screen
        window_width = 500
        window_height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        root.configure(bg="#2c3e50")
        
        # Set up GUI components
        self.setup_ui()

    def setup_ui(self):
        # Chat history area
        self.chat_history = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Helvetica", 12), bg="#ecf0f1", fg="#34495e")
        self.chat_history.config(state=tk.DISABLED)  # Chat history is read-only
        self.chat_history.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)
        
        # Input frame
        self.input_frame = tk.Frame(self.root, bg="#2c3e50")
        self.input_frame.pack(fill=tk.X, pady=10)
        
        # Entry box to type message
        self.user_input = tk.Entry(self.input_frame, font=("Helvetica", 12), bg="#ecf0f1", fg="#34495e", width=50)
        self.user_input.grid(row=0, column=0, padx=10)

        # Send button
        self.send_button = tk.Button(self.input_frame, text="Send", font=("Helvetica", 12), bg="#1abc9c", fg="white", command=self.send_message)
        self.send_button.grid(row=0, column=1, padx=5)

    def send_message(self):
        # Get user input
        message = self.user_input.get()
        if message.strip():
            # Display user message
            self.display_message(f"You: {message}", "user")
            
            # Generate and display bot response
            bot_response = self.generate_response(message)
            self.display_message(f"Bot: {bot_response}", "bot")
        
        # Clear the input field
        self.user_input.delete(0, tk.END)
    
    def display_message(self, message, sender):
        # Display the message in the chat history
        self.chat_history.config(state=tk.NORMAL)
        if sender == "user":
            self.chat_history.insert(tk.END, f"{message}\n", "user")
        else:
            self.chat_history.insert(tk.END, f"{message}\n", "bot")
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.yview(tk.END)

    def generate_response(self, user_input):
        """
        Generates a basic response using spaCy for language processing.
        """
        doc = nlp(user_input)

        # Rule-based simple chatbot logic
        if "hello" in user_input.lower() or "hi" in user_input.lower():
            return "Hello! How can I help you today?"
        elif "bye" in user_input.lower() or "goodbye" in user_input.lower():
            return "Goodbye! Have a nice day!"
        elif "how are you" in user_input.lower():
            return "I'm just a bot, but I'm doing great! How about you?"
        else:
            return "I'm not sure I understand. Can you rephrase?"

# Run the chatbot
if __name__ == "__main__":
    root = tk.Tk()
    chatbot = ChatBotApp(root)
    root.mainloop()
