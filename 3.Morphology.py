import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tag import pos_tag
text = "The striped bats are hanging on their feet for best"
words = word_tokenize(text)
print("Tokenized Words:", words)
pos_tags = pos_tag(words)
print("\nPart-of-Speech Tags:", pos_tags)
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print("\nStemmed Words:", stemmed_words)
lemmatizer = WordNetLemmatizer()
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags]
print("\nLemmatized Words:", lemmatized_words)
