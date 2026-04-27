# Natural Language Processing (NLP) Repository

This repository contains all programs and projects developed for the **Natural Language Processing** subject at ESCOM, semester 7.

## Repository Structure

```
├── Class/
│   ├── Diagnostic_Exam/
│   │   └── word.ipynb
│   ├── Notes/
│   │   ├── U2/
│   │   └── U3/
│   ├── Tokenizador/
│   │   └── tokenizador.ipynb
│   ├── repeatedwords_deleter.ipynb
│   ├── stopwords_deleter.ipynb
│   └── two_lower.ipynb
│
├── Partial_1/
│   ├── Practices.ipynb
│   ├── tokenizer
│   ├── tokenizer.cpp
│   └── reportes/
│
├── Partial_2/
│   ├── Practices.ipynb
│   ├── mt_co.py
│   ├── requirements_datascientist.txt
│   ├── Data/
│   │   ├── Cocina/
│   │   ├── Deportes/
│   │   ├── Fisica/
│   │   ├── Maquillaje/
│   │   ├── Test/
│   │   └── Videojuegos/
│   ├── docs/
│   └── Exam/
│       ├── Exam.ipynb
│       ├── b_problem.ipynb
│       ├── c_problem.ipynb
│       ├── TopicClassifier.py
│       ├── Data/
│       └── NLP_Utilities/
│           ├── Bag_of_Words.py
│           ├── CoOccurrence_PCA.py
│           ├── Lemmatization.py
│           ├── TF_IDF.py
│           ├── Tokenizer.py
│           └── Dictionaries/
│
└── Partial_3/
    ├── Exam/
    │   ├── main.py
    │   ├── Data/
    │   ├── History/
    │   ├── LDA/
    │   ├── Summary/
    │   ├── Utils/
    │   └── Voice/
    └── Practices/
        ├── Practice_1.ipynb
        ├── Practice_3.ipynb
        ├── Data/
        ├── Practice_3/
        │   ├── main.py
        │   ├── Data/
        │   ├── History/
        │   ├── LDA/
        │   ├── Summary/
        │   ├── Utils/
        │   └── Voice/
```

## Contents

### Class/
Contains class exercises and theoretical materials:
- **Diagnostic_Exam/**: Diagnostic examination materials
  - `word.ipynb`: Word processing diagnostic exercise
- **Notes/**: Course notes organized by units
  - `U2/`: Unit 2 notes and exercises
  - `U3/`: Unit 3 notes and exercises
- **Tokenizador/**: Tokenizer implementation exercises
  - `tokenizador.ipynb`: Tokenizer implementation in Python
- **repeatedwords_deleter.ipynb**: Exercise for removing repeated words
- **stopwords_deleter.ipynb**: Exercise for removing stop words
- **two_lower.ipynb**: Exercise for text lowercase conversion

### Partial_1/
First partial examination materials and projects:
- **Practices.ipynb**: Practice exercises and implementations
- **tokenizer**: Executable tokenizer program
- **tokenizer.cpp**: C++ implementation of the tokenizer
- **reportes/**: Reports and documentation for the partial

### Partial_2/
Second partial examination - Text classification and NLP utilities:
- **Practices.ipynb**: Practice exercises for this partial
- **mt_co.py**: Machine translation and co-occurrence implementation
- **requirements_datascientist.txt**: Python dependencies
- **Data/**: Dataset folders by category (Cocina, Deportes, Fisica, Maquillaje, Test, Videojuegos)
- **Exam/**: Examination materials and topic classification
  - `Exam.ipynb`: Main exam notebook
  - `b_problem.ipynb`: Problem B exercises
  - `c_problem.ipynb`: Problem C exercises
  - `TopicClassifier.py`: Topic classification implementation
  - **NLP_Utilities/**: Reusable NLP functions
    - `Bag_of_Words.py`: Bag-of-Words vectorization
    - `CoOccurrence_PCA.py`: Co-occurrence matrix and PCA analysis
    - `Lemmatization.py`: Text lemmatization utilities
    - `TF_IDF.py`: TF-IDF vectorization
    - `Tokenizer.py`: Tokenization utilities
    - **Dictionaries/**: Utility dictionaries for NLP processing

### Partial_3/
Third partial examination - Advanced NLP topics:
- **Exam/**: Examination project with comprehensive implementation
  - `main.py`: Main entry point
  - **History/**: Story generation module
    - `story_generator.py`: Story generation implementation
  - **LDA/**: Latent Dirichlet Allocation topic modeling
    - `lda_model.py`: LDA model implementation
    - `preprocessing.py`: Data preprocessing for LDA
  - **Summary/**: Text summarization module
  - **Utils/**: Utility functions and helpers
  - **Voice/**: Speech processing module
    - `speech_to_text.py`: Speech-to-text conversion
    - `text_to_speech.py`: Text-to-speech synthesis
  - **Data/**: Datasets for exam
- **Practices/**: Practice exercises
  - `Practice_1.ipynb`: Practice 1 notebook
  - `Practice_3.ipynb`: Practice 3 notebook
  - **Data/**: Datasets by category
  - **Practice_3/**: Organized practice 3 implementation
    - `main.py`: Practice 3 main implementation
    - Similar modular structure as Exam/

## Technologies Used

- **Python**: Jupyter Notebooks, Scikit-learn, NLTK, Gensim
- **C++**: Tokenizer implementation
- **NLP Techniques**: 
  - Tokenization and text preprocessing
  - Bag-of-Words and TF-IDF vectorization
  - Co-occurrence analysis and dimensionality reduction (PCA)
  - Lemmatization
  - Topic modeling (LDA)
  - Speech processing (STT/TTS)
  - Text summarization
  - Story generation

## About

This repository serves as a comprehensive collection of all programming assignments, exercises, and projects completed during the NLP course at ESCOM. Each directory contains specific implementations and documentation related to different aspects of natural language processing, from basic text processing to advanced topics like topic modeling and speech synthesis.

## Author

Alexander Sanchez Garcia - ESCOM Student

---

*Repository for NLP Subject - Semester 7*