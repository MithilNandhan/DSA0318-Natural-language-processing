import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["running", "jumps", "easily", "flying", "studies", "happier", "computers", "university"]
stemmed_words = [stemmer.stem(word) for word in words]
for original, stemmed in zip(words, stemmed_words):
    print(f"Original: {original}, Stemmed: {stemmed}")
