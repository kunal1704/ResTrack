from sentence_transformers import SentenceTransformer

# Initialize the model
model = SentenceTransformer('all-MiniLM-L6-v2')  # You can switch models if needed

def get_embedding(text):
    return model.encode(text)

# Example usage
# resume_embedding = get_embedding(resume_text)
# jd_embedding = get_embedding(jd_text)
