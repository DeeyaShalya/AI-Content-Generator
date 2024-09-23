from transformers import pipeline

# Function to generate content using transformers
def generate_content(prompt):
    generator = pipeline('text-generation', model='gpt2')
    generated_text = generator(prompt, max_length=100, num_return_sequences=1)
    return generated_text[0]['generated_text']