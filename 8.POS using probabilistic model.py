import nltk
from nltk.corpus import treebank
from collections import defaultdict
import random
tagged_sentences = treebank.tagged_sents(tagset='universal')
train_size = int(0.8 * len(tagged_sentences))
train_data = tagged_sentences[:train_size]
test_data = tagged_sentences[train_size:]
word_tag_freq = defaultdict(lambda: defaultdict(int))

for sentence in train_data:
    for word, tag in sentence:
        word_tag_freq[word.lower()][tag] += 1
most_probable_tag = {}

for word, tag_freqs in word_tag_freq.items():
    most_probable_tag[word] = max(tag_freqs, key=tag_freqs.get)
def stochastic_pos_tag(sentence):
    tags = []
    for word in sentence:
        word_lower = word.lower()
        if word_lower in most_probable_tag:
            tags.append(most_probable_tag[word_lower])
        else:
            tags.append(random.choice(list(word_tag_freq['the'].keys())))
    return list(zip(sentence, tags))
test_sentence = [word for word, tag in test_data[0]]
tagged_sentence = stochastic_pos_tag(test_sentence)
print("Original sentence:", test_sentence)
print("Tagged sentence:", tagged_sentence)
