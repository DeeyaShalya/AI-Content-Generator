import nltk
import spacy

# Download necessary data for NLTK and spaCy
nltk.download('punkt')
spacy.cli.download('en_core_web_sm')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Preprocess the input using NLTK and spaCy
def preprocess_input(text):
    # Tokenization using NLTK
    tokens = nltk.word_tokenize(text)

    # Perform spaCy processing
    doc = nlp(text)
    lemmatized_text = ' '.join([token.lemma_ for token in doc])

    return tokens, lemmatized_text