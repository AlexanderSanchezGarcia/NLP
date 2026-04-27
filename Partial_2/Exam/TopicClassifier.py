# ===========================================================
#      A) PREPROCESSING AND LEMMATIZATION
# ===========================================================

from NLP_Utilities.CoOccurrence_PCA import CoOccurrencePCA
import PyPDF2
import math


def preprocess_text(text):
    """
    Receives a long text (≥ 500 words) and returns its lemmas
    using only the Tokenizer inherited in CoOccurrencePCA.
    """
    nlp = CoOccurrencePCA()
    tokens = nlp.tokenize(text)
    return tokens


# ===========================================================
#      B) BASIC PDF READER
# ===========================================================

def read_pdf(path):
    text = ""
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


# ===========================================================
#      C) BUILD WORD-FREQUENCY DICTIONARY (Bag of Words)
# ===========================================================

def build_frequency_vector(tokens):
    freq = {}
    for tok in tokens:
        freq[tok] = freq.get(tok, 0) + 1
    return freq


# ===========================================================
#      D) COSINE SIMILARITY (manual implementation)
# ===========================================================

def cosine_similarity(vec1, vec2):
    """
    vec1 and vec2 are dictionaries {word: frequency}
    """

    # Intersection of words
    common_words = set(vec1.keys()) & set(vec2.keys())

    # Numerator: sum of products
    dot_product = sum(vec1[w] * vec2[w] for w in common_words)

    # Norms
    norm1 = math.sqrt(sum(f * f for f in vec1.values()))
    norm2 = math.sqrt(sum(f * f for f in vec2.values()))

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot_product / (norm1 * norm2)


# ===========================================================
#      E) COMPARE THREE TEXTS AND CHOOSE THE MOST SIMILAR
# ===========================================================

def compare_texts_cosine(target_vector, vector_list):
    """
    target_vector: frequency vector of the text to classify
    vector_list: list of (name, vector)
    Returns: name of most similar text + dictionary of scores
    """

    scores = {}
    for name, vec in vector_list:
        scores[name] = cosine_similarity(target_vector, vec)

    # Best match
    best_match = max(scores, key=scores.get)

    return best_match, scores


# ===========================================================
#                      MAIN PROGRAM
# ===========================================================

if __name__ == "__main__":

    # Paths to your three PDFs
    pdf1 = r"Data/Texto1"
    pdf2 = r"Data/Texto2"
    pdf3 = r"Data/Texto3"
    

    # -------- READ & PREPROCESS --------
    texts = {
        "Texto1": preprocess_text(read_pdf(pdf1)),
        "Texto2": preprocess_text(read_pdf(pdf2)),
        "Texto3": preprocess_text(read_pdf(pdf3)),
    }

    # -------- BUILD FREQUENCY VECTORS --------
    vectors = {name: build_frequency_vector(tokens)
               for name, tokens in texts.items()}

    # -------- TEXT TO CLASSIFY --------
    consulta = input("Write down the text you wanna compare:\n")
    consulta_tokens = preprocess_text(consulta)
    consulta_vector = build_frequency_vector(consulta_tokens)

    # -------- COSINE COMPARISON --------
    vector_list = [(name, vectors[name]) for name in vectors]

    best, scores = compare_texts_cosine(consulta_vector, vector_list)

    print("\n=== RESULTS OF COSINE SIMILARITY ===")
    for name, score in scores.items():
        print(f"{name}: {score:.4f}")

    print("\n→ The most likely document is:", best)
