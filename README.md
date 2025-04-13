# ResTrack - Phase I

ResTrack is an AI-powered tool designed to streamline the hiring process by intelligently comparing resumes against job descriptions. In Phase I, ResTrack focuses on analyzing resumes and determining which one aligns best with a given job description using NLP techniques.

## 🚀 Features (Phase I)

- 📄 **Resume & Job Description Parsing**  
  Extracts clean text from various formats (PDF, DOCX, etc.) for both resumes and job descriptions.

- 🧠 **Semantic Embedding Generation**  
  Converts parsed text into high-dimensional vector representations using state-of-the-art NLP models.

- 🔍 **Similarity Scoring**  
  Compares multiple resumes to a job description using cosine similarity between their embeddings.

- 🥇 **Top Candidate Selection**  
  Outputs a similarity search score of the resume based on how well they match the job description.

---

## Requirements

- pdfminer.six
- docx2txt
- sentence-transformers
- scikit-learn
- numpy
- python=3.10
- pip

---

## Folder Structure

```
restrack/
├── data/
│   ├── resumes/
│   └── job_descriptions/
├── src/
│   ├── main.py
|   ├── parser.py
│   ├── embedder.py
│   └── similarity.py
├── requirements.yml
└── README.md
```

---

## Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/kunal1704/restrack.git
cd restrack
```

2. **Create and Activate Conda Environment**

```bash
conda env create -f requirements.yml
conda activate restrack
```

3. **Run the Tool**

Make sure to place your resumes and job descriptions in the respective folders inside `/data`.

```bash
python main.py
```

4. **Output**

- A string displaying the similarity score of the resume and the Job description
- Depending on the threshold for similarity set by user, the following two strings shall come as output:
        -- This resume is a good match for the job description.
        -- This resume is not a good match for the job description.

  Output:
            Similarity score:
            This resume is a good match for the job description / This resume is not a good match for the job description.
---

## Next Steps

- 📊 Exploring other types of similarity measuring techniques 
- 🧠 Model fine-tuning on hiring data
- 🌐 Web interface for HR teams
- 🔒 Role-based access and authentication
- 📚 Candidate profile enrichment from LinkedIn/GitHub

---

## 🤝 Contributing
 
Feel free to fork this repo and submit a pull request for improvements or new features.

---

## 📃 License

This project is licensed under the MIT License.

---
