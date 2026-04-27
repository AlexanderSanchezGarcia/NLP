import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nlp = spacy.load("es_core_news_sm")
stop_words = set(stopwords.words("spanish"))

def clean_text(text):
    doc = nlp(text.lower())
    tokens = [
        token.lemma_
        for token in doc
        if token.is_alpha and token.text not in stop_words
    ]
    return tokens