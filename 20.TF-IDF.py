import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def preprocess(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return ' '.join(tokens)
def rank_documents(documents, query):
    processed_docs = [preprocess(doc) for doc in documents]
    processed_query = preprocess(query)
    corpus = processed_docs + [processed_query]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    query_vector = tfidf_matrix[-1]  
    document_vectors = tfidf_matrix[:-1]  
    similarities = cosine_similarity(query_vector, document_vectors).flatten()
    ranked_doc_indices = np.argsort(similarities)[::-1]
    return ranked_doc_indices, similarities
if __name__ == "__main__":
    documents = [
        "The cat sat on the mat.",
        "Dogs are barking in the neighborhood.",
        "There is a beautiful garden with flowers.",
        "A bank can help you with your savings and investments.",
        "Cats are different from dogs in many ways."
    ]
    query = "cats and dogs"
    ranked_indices, similarities = rank_documents(documents, query)
    print("Documents ranked by relevance to the query:")
    for i, idx in enumerate(ranked_indices):
        print(f"Rank {i+1}: Document {idx+1} with similarity {similarities[idx]:.4f}")
        print(f"Content: {documents[idx]}\n")
