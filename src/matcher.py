from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(embedding1, embedding2):
    similarity = cosine_similarity([embedding1], [embedding2])
    return similarity[0][0]

# Example usage
# similarity_score = calculate_similarity(resume_embedding, jd_embedding)
