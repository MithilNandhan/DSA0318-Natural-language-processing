import re
import nltk
sentence = "The dog was running and chased 2 cats."
tokens = nltk.word_tokenize(sentence)
initial_tagged_words = []
for word in tokens:
    if re.match(r'.*ing$', word):
        initial_tagged_words.append((word, 'VBG'))  
    elif re.match(r'.*ed$', word):
        initial_tagged_words.append((word, 'VBD')) 
    elif re.match(r'.*es$', word):
        initial_tagged_words.append((word, 'VBZ'))  
    elif re.match(r'[0-9]+$', word):
        initial_tagged_words.append((word, 'CD')) 
    else:
        initial_tagged_words.append((word, 'NN'))   
print("Initial tagging:", initial_tagged_words)
def apply_transformations(tagged_words):
    transformed_words = []
    for i in range(len(tagged_words)):
        word, tag = tagged_words[i]
        if tag == 'NN' and word.lower() == 'the':
            transformed_words.append((word, 'DT')) 
        else:
            transformed_words.append((word, tag))
    return transformed_words
final_tagged_words = apply_transformations(initial_tagged_words)
print("Final tagging:", final_tagged_words)
