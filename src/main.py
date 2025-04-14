from parser import parse_document
from embedder import get_embedding
from matcher import calculate_similarity
import pathlib 

def main():
    # Parse resume and JD
    PATH = pathlib.Path.cwd().parent
    
    resume_path = "Resume_Path"
    jd_path = "JD_Path"
    
    resume_text = parse_document(resume_path)
    jd_text = parse_document(jd_path)

    # Generate embeddings
    resume_embedding = get_embedding(resume_text)
    jd_embedding = get_embedding(jd_text)

    # Calculate similarity
    similarity_score = calculate_similarity(resume_embedding, jd_embedding)

    print(f"Similarity Score: {similarity_score:.4f}")
    
    if similarity_score > 0.8:
        print("This resume is an excellent match for the job description.")
    
    elif  0.5 < similarity_score < 0.8:
        print("This resume is a very good match for the job description.")
    
    elif  0.3 < similarity_score < 0.5:
        print("The candidate with this resume needs training to fit the job description.")

    else:
        print("This resume is not a good match for the job description.")


if __name__ == "__main__":
    main()