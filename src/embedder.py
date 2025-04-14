from sentence_transformers import SentenceTransformer
from nltk.tokenize import sent_tokenize
import numpy as np

# Initialize the model
model = SentenceTransformer('all-MiniLM-L6-v2')
MAX_TOKENS = 256  # model max length

def chunk_text(text, max_tokens=MAX_TOKENS):
    """Splits text into chunks based on sentence boundaries to fit token limit."""
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        # Estimate token count as number of words 
        if len((current_chunk + sentence).split()) <= max_tokens:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def get_embedding(text):
    """
    Returns a single embedding for the input text.
    If text is too long, it is chunked and the chunk embeddings are averaged.
    """
    chunks = chunk_text(text)
    embeddings = model.encode(chunks)

    # Average embeddings across all chunks
    document_embedding = np.mean(embeddings, axis=0)
    return document_embedding
