import tkinter as tk
from tkinter import scrolledtext
from preprocessing import preprocess_input
from generation import generate_content
from storage import store_in_chromadb

# Function to handle content generation and display in GUI
def generate_and_display():
    user_input = entry.get()
    tokens, lemmatized_text = preprocess_input(user_input)
    generated_content = generate_content(user_input)
    store_in_chromadb(user_input, generated_content)

    output_area.delete(1.0, tk.END)
    output_area.insert(tk.END, f"Tokens: {tokens}\n\nLemmatized Text: {lemmatized_text}\n\nGenerated Content:\n{generated_content}")

# Setup the enhanced GUI window
root = tk.Tk()
root.title("Attractive Content Generation System")
root.geometry("700x500")
root.config(bg='#282C34')  # Dark theme background

# Create a stylish title label
title_label = tk.Label(root, text="AI Content Generator", font=("Helvetica", 20, "bold"), bg="#61AFEF", fg="#282C34")
title_label.pack(pady=20)

# Create label and input field with enhanced styling
label = tk.Label(root, text="Enter your topic or prompt:", font=("Arial", 14), bg="#282C34", fg="#ABB2BF")
label.pack()

entry = tk.Entry(root, width=50, font=("Arial", 12), bg="#98C379", fg="#282C34")
entry.pack(pady=10)

# Create a button with a modern look to generate content
generate_button = tk.Button(root, text="Generate Content", font=("Arial", 12, "bold"), bg="#E06C75", fg="white", command=generate_and_display)
generate_button.pack(pady=10)

# Output area with a scrollbar and modern font
output_area = scrolledtext.ScrolledText(root, width=70, height=15, font=("Arial", 12), bg="#98C379", fg="#282C34", wrap=tk.WORD)
output_area.pack(pady=10)

# Footer label
footer_label = tk.Label(root, text="Powered by AI & NLP - Built with spaCy, NLTK, Transformers, and ChromaDB", font=("Arial", 10), bg="#282C34", fg="#ABB2BF")
footer_label.pack(pady=20)
root.mainloop()