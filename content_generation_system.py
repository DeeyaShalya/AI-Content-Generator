import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import nltk
import spacy
import chromadb
from transformers import pipeline

# Download necessary data for NLTK and spaCy
nltk.download('punkt')
spacy.cli.download('en_core_web_sm')

# Initialize spaCy model and ChromaDB client
nlp = spacy.load("en_core_web_sm")
client = chromadb.Client()

# Preprocess the input using NLTK and spaCy
def preprocess_input(text):
    tokens = nltk.word_tokenize(text)
    doc = nlp(text)
    lemmatized_text = ' '.join([token.lemma_ for token in doc])
    return tokens, lemmatized_text

# Function to generate content using transformers
def generate_content(prompt):
    generator = pipeline('text-generation', model='gpt2')
    generated_text = generator(prompt, max_length=100, num_return_sequences=1)
    return generated_text[0]['generated_text']

# Store generated content in ChromaDB
def store_in_chromadb(prompt, generated_content):
    collection = client.create_collection("generated_articles")
    collection.add(
        ids=[prompt],  # Using prompt as ID
        embeddings=[[0]*768],  # Placeholder embedding
        metadatas=[{"content": generated_content}]
    )
    return f"Content stored for prompt: {prompt}"

#GUI
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Function to preprocess input (you can replace this with your actual function)
def preprocess_input(user_input):
    tokens = user_input.split()  # Example tokenization
    lemmatized_text = user_input.lower()  # Example lemmatization
    return tokens, lemmatized_text

# Function to simulate content generation based on the user input and length option
def generate_content(user_input, length_option):
    # Simulating content generation based on length
    base_content = f"Generated content for: {user_input}. "  # Use input as context for content
    if length_option == "Short (100-150 words)":
        generated_content = base_content + " ".join([base_content] * 10)  # Repeat to simulate 100-150 words
    elif length_option == "Medium (200-250 words)":
        generated_content = base_content + " ".join([base_content] * 20)  # Repeat to simulate 200-250 words
    else:  # Long (300-350 words)
        generated_content = base_content + " ".join([base_content] * 30)  # Repeat to simulate 300-350 words
    return generated_content

# Function to store generated content (replace with actual storage logic)
def store_in_chromadb(user_input, generated_content):
    # Simulate storing data in ChromaDB (you can replace this with actual functionality)
    print("Storing in ChromaDB:", user_input, generated_content)

# Function to handle content generation and display in GUI
def generate_and_display():
    user_input = entry.get()  # Get user input
    length_option = length_var.get()  # Get length option from dropdown
    if user_input.strip() == "":  # Check if input is empty
        messagebox.showerror("Input Error", "Please enter a topic to generate content.")
        return
    
    tokens, lemmatized_text = preprocess_input(user_input)  # Preprocess input
    generated_content = generate_content(user_input, length_option)  # Generate content based on input and length
    store_in_chromadb(user_input, generated_content)  # Store content in ChromaDB

    # Clear previous output and display new generated content
    output_area.delete(1.0, tk.END)
    output_area.insert(tk.END, f"Tokens: {tokens}\n\nLemmatized Text: {lemmatized_text}\n\nGenerated Content:\n{generated_content}")

# Function to clear the output field
def clear_output():
    output_area.delete(1.0, tk.END)

# Setup the enhanced GUI window
root = tk.Tk()
root.title("Attractive Content Generation System")
root.geometry("700x600")
root.config(bg='#282C34')  # Dark theme background

# Create a stylish title label
title_label = tk.Label(root, text="AI Content Generator", font=("Helvetica", 20, "bold"), bg="#61AFEF", fg="#282C34")
title_label.pack(pady=20)

# Create label and input field with enhanced styling
label = tk.Label(root, text="Enter your topic or prompt:", font=("Arial", 14), bg="#282C34", fg="#ABB2BF")
label.pack()

entry = tk.Entry(root, width=50, font=("Arial", 12), bg="#98C379", fg="#282C34")
entry.pack(pady=10)

# Dropdown for content length options
length_var = tk.StringVar(root)
length_var.set("Medium (200-250 words)")  # Default value
length_dropdown = tk.OptionMenu(root, length_var, "Short (100-150 words)", "Medium (200-250 words)", "Long (300-350 words)")
length_dropdown.config(font=("Arial", 12), bg="#98C379", fg="#282C34")
length_dropdown.pack(pady=10)

# Create a button to generate content
generate_button = tk.Button(root, text="Generate Content", font=("Arial", 12, "bold"), bg="#E06C75", fg="white", command=generate_and_display)
generate_button.pack(pady=10)

# Output area with a scrollbar and modern font
output_area = scrolledtext.ScrolledText(root, width=70, height=15, font=("Arial", 12), bg="#98C379", fg="#282C34", wrap=tk.WORD)
output_area.pack(pady=10)

# Create a button to clear the output
clear_button = tk.Button(root, text="Clear Output", font=("Arial", 12, "bold"), bg="#E06C75", fg="white", command=clear_output)
clear_button.pack(pady=10)

# Footer label
footer_label = tk.Label(root, text="Powered by AI & NLP - Built with spaCy, NLTK, Transformers, and ChromaDB", font=("Arial", 10), bg="#282C34", fg="#ABB2BF")
footer_label.pack(pady=20)

# Run the GUI
root.mainloop()