import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nlp = spacy.load('en_core_web_sm')
def evaluate_coherence(text):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    if len(sentences) < 2:
        return "Text is too short to evaluate coherence."
    vectorizer = TfidfVectorizer()
    sentence_vectors = vectorizer.fit_transform(sentences).toarray()
    similarities = []
    for i in range(len(sentence_vectors) - 1):
        similarity = cosine_similarity([sentence_vectors[i]], [sentence_vectors[i + 1]])[0][0]
        similarities.append(similarity)
    avg_similarity = np.mean(similarities)
    coherence_score = avg_similarity
    if coherence_score > 0.5:
        coherence = "high"
    elif coherence_score > 0.2:
        coherence = "moderate"
    else:
        coherence = "low"
    return f"Coherence Score: {coherence_score:.4f} ({coherence} coherence)"
if __name__ == "__main__":
    text = ("John went to the store. He bought some milk. "
            "The weather was nice. A dog was barking outside. "
            "The milk was cold when he came back home.")
    coherence_result = evaluate_coherence(text)
    print(coherence_result)
