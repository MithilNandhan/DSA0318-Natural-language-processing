import nltk
from nltk import word_tokenize, pos_tag
text = "The quick brown fox jumps over the lazy dog."
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
print(pos_tags)
