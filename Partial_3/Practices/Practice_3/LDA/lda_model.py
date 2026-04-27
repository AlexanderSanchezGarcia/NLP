import random
from gensim import corpora, models
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from LDA.preprocessing import clean_text
from Voice.text_to_speech import speak

def load_docs():
    docs = []
    for i in range(10):
        text = open(f"Data/doc{i}.txt", encoding="utf-8").read()
        docs.append(text)
    return docs

def execute_lda():
    speak("¿Cuántos tópicos deseas modelar?")
    try:
        num_topics = int(input("Número de tópicos: "))
    except:
        num_topics = 3

    docs = load_docs()
    processed_texts = [clean_text(doc) for doc in docs]

    dictionary = corpora.Dictionary(processed_texts)
    corpus = [dictionary.doc2bow(text) for text in processed_texts]
    lda = models.LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        passes=10,
        random_state=42
    )

    for i, topic in lda.show_topics(num_topics=num_topics, num_words=10, formatted=False):
        palabras = dict(topic)
        nube = WordCloud(background_color="white").generate_from_frequencies(palabras)

        plt.figure()
        plt.imshow(nube, interpolation="bilinear")
        plt.axis("off")
        plt.title(f"Tópico {i}")
        plt.show()

        speak(f"Este es el tópico número {i}")