from parser import parse_document
from embedder import get_embedding
from matcher import calculate_similarity
import pathlib 

def main():
    # Parse resume and JD
    PATH = pathlib.Path.cwd().parent
    
    resume_path = PATH / "data"/ "resumes"/"resume.pdf"
    jd_path = PATH / "data"/ "job_descriptions"/"Tara_Capital_Partners_India.pdf"
    
    print("Parsing documents...")
    resume_text = parse_document(resume_path)
    jd_text = parse_document(jd_path)

    # Generate embeddings
    print("Generating embeddings...")
    resume_embedding = get_embedding(resume_text)
    jd_embedding = get_embedding(jd_text)

    # Calculate similarity
    print("Calculating similarity...")
    similarity_score = calculate_similarity(resume_embedding, jd_embedding)

    print(f"Similarity Score: {similarity_score:.4f}")
    if similarity_score > 0.7:
        print("This resume is a good match for the job description.")
    else:
        print("This resume is not a good match for the job description.")

# Example usage
# run_comparison("data/resumes/sample_resume.pdf", "data/job_descriptions/sample_jd.txt")

if __name__ == "__main__":
    main()
