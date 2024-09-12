import re
import nltk
sentence = "The dog was running and chased 2 cats."
tokens = nltk.word_tokenize(sentence)
tagged_words = []
for word in tokens:
    if re.match(r'.*ing$', word):
        tagged_words.append((word, 'VBG'))  
    elif re.match(r'.*ed$', word):
        tagged_words.append((word, 'VBD'))
    elif re.match(r'.*es$', word):
        tagged_words.append((word, 'VBZ'))
    elif re.match(r'[0-9]+$', word):
        tagged_words.append((word, 'CD'))
    else:
        tagged_words.append((word, 'NN'))
print(tagged_words)
