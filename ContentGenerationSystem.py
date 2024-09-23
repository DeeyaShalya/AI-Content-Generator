#Step 1: Set Up the Environment
#Install the required packages

#Step 2: Leverage LLM for Text Generation
#API Key Setup
import openai
# Set up your API Key
#Update the Text Generation Function Using Hugging Face
from transformers import pipeline

# Load the pre-trained model from Hugging Face (e.g., GPT-2 or GPT-Neo)
generator = pipeline('text-generation', model='gpt2')

# Function to generate text using the Hugging Face model
def generate_text(prompt):
    result = generator(prompt, max_length=500, num_return_sequences=1)
    return result[0]['generated_text']

# Example usage
prompt = "Write an article about the importance of AI in healthcare."
generated_text = generate_text(prompt)
print(generated_text)

from transformers import AutoModelForCausalLM, AutoTokenizer

#Using GPT-2 (Smaller Model)
# Load a smaller version of GPT-2
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Encode the input prompt
prompt = "The future of AI in healthcare is promising because"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text from the prompt
outputs = model.generate(**inputs, max_length=500, do_sample=True)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)

#Enable Model Offloading (Use CPU for Inference)
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model to the CPU to save GPU memory
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2").to("cpu")

# Encode the input prompt
prompt = "AI in education will revolutionize learning because"
inputs = tokenizer(prompt, return_tensors="pt").to("cpu")

# Generate text from the prompt
outputs = model.generate(**inputs, max_length=500, do_sample=True)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)

# Encode the input prompt
prompt = "The future of AI in healthcare is promising because"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text from the prompt
outputs = model.generate(**inputs, max_length=500, do_sample=True)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)

#Step 3: Preprocess the Generated Content using NLTK and spaCy
#Text Preprocessing:
import nltk
import spacy

# Downloading NLTK dependencies
nltk.download('punkt')

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Function to preprocess text
def preprocess_text(text):
    # Tokenization using NLTK
    tokens = nltk.word_tokenize(text)

    # Named Entity Recognition using spaCy
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return tokens, entities

tokens, entities = preprocess_text(generated_text)
print(f"Tokens: {tokens[:10]}")
print(f"Named Entities: {entities}")

#Step 4: Store Generated Content in ChromaDB
# Step 4: Store Generated Content in ChromaDB
import chromadb
import nltk
import spacy
from transformers import pipeline

# Download necessary data for NLTK and spaCy
nltk.download('punkt')
spacy.cli.download('en_core_web_sm')

# Initialize spaCy model and ChromaDB client
nlp = spacy.load("en_core_web_sm")
client = chromadb.Client()

# Create or retrieve the collection
collection_name = "generated_content"
if collection_name not in [col.name for col in client.list_collections()]:
    collection = client.create_collection(name=collection_name)
else:
    collection = client.get_collection(name=collection_name)

# Function to preprocess text
def preprocess_text(text):
    # Tokenization using NLTK
    tokens = nltk.word_tokenize(text)
    
    # Named Entity Recognition using spaCy
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return tokens, entities

# Preprocess the generated text
tokens, entities = preprocess_text(generated_text)

# Convert tokens and entities to strings for ChromaDB compatibility
tokens_str = ' '.join(tokens)
entities_str = ', '.join([f"{entity[0]} ({entity[1]})" for entity in entities])

# Define the generated content to be inserted (content as string)
document_content = generated_text + "\n\nTokens: " + tokens_str + "\nEntities: " + entities_str
#
# Insert the content into the collection (ChromaDB expects strings, not dictionaries)
collection.add(ids=["1"], documents=[document_content])

print("Content successfully stored in ChromaDB.")

#Step 5: Build a GUI for Customized User Input
#Advanced Features and Improvements
#Add User Customization for Tone and Length:
# Add dropdowns for customization
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QPushButton, QComboBox, QMessageBox
from transformers import pipeline

# Initialize the content generation model using Hugging Face transformers
generator = pipeline('text-generation', model='gpt2')

# Function to generate content using a pre-trained model
def generate_content(user_input, length_option):
    max_length = 150  # Default to 150 words

    if length_option == "Short (100-150 words)":
        max_length = 150
    elif length_option == "Medium (200-250 words)":
        max_length = 250
    elif length_option == "Long (300-350 words)":
        max_length = 350

    # Generate content using the GPT-2 model
    generated = generator(user_input, max_length=max_length, num_return_sequences=1)
    
    return generated[0]['generated_text']

class ContentGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('AI Content Generator')
        self.setGeometry(100, 100, 800, 600)

        # Layout setup
        layout = QVBoxLayout()

        # Title label
        title_label = QLabel("AI Content Generator", self)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title_label)

        # Input label and field
        self.input_label = QLabel("Enter your topic or prompt:", self)
        layout.addWidget(self.input_label)

        self.input_field = QLineEdit(self)
        self.input_field.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.input_field)

        # Dropdown for content length selection
        self.length_label = QLabel("Select content length:", self)
        layout.addWidget(self.length_label)

        self.length_combo = QComboBox(self)
        self.length_combo.addItems(["Short (100-150 words)", "Medium (200-250 words)", "Long (300-350 words)"])
        self.length_combo.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.length_combo)

        # Button to generate content
        self.generate_button = QPushButton("Generate Content", self)
        self.generate_button.clicked.connect(self.generate_and_display)
        self.generate_button.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(self.generate_button)

        # Output text area
        self.output_area = QTextEdit(self)
        self.output_area.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.output_area)

        # Clear button
        self.clear_button = QPushButton("Clear Output", self)
        self.clear_button.clicked.connect(self.clear_output)
        self.clear_button.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(self.clear_button)

        # Footer label
        footer_label = QLabel("Powered by AI & NLP - Built with PyQt5 and GPT-2", self)
        footer_label.setStyleSheet("font-size: 12px; color: gray;")
        layout.addWidget(footer_label)

        # Set layout
        self.setLayout(layout)

    # Function to handle content generation
    def generate_and_display(self):
        user_input = self.input_field.text()
        length_option = self.length_combo.currentText()

        if not user_input.strip():
            QMessageBox.warning(self, "Input Error", "Please enter a topic to generate content.")
            return

        # Generate the content using GPT-2
        generated_content = generate_content(user_input, length_option)

        self.output_area.setPlainText(f"Generated Content:\n{generated_content}")

    # Function to clear the output field
    def clear_output(self):
        self.output_area.clear()

# Main execution block
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContentGeneratorApp()
    window.show()
    sys.exit(app.exec_())