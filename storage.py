import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Store generated content in ChromaDB
def store_in_chromadb(prompt, generated_content):
    collection = client.create_collection("generated_articles")
    collection.add(
        ids=[prompt],  # Using prompt as ID
        embeddings=[[0]*768],  # Placeholder embedding
        metadatas=[{"content": generated_content}]
    )
    return f"Content stored for prompt: {prompt}"