import random
from collections import defaultdict, Counter
from nltk.tokenize import word_tokenize
import nltk
text = "the quick brown fox jumps over the lazy dog and the quick brown fox runs away quickly"
words = word_tokenize(text.lower())
bigrams = list(zip(words[:-1], words[1:]))
bigram_freqs = defaultdict(Counter)
for w1, w2 in bigrams:
    bigram_freqs[w1][w2] += 1
bigram_probs = {}
for w1, counter in bigram_freqs.items():
    total_count = float(sum(counter.values()))
    bigram_probs[w1] = {w2: count / total_count for w2, count in counter.items()}
seed_word = "the"
length = 10
text = [seed_word]
for _ in range(length - 1):
    current_word = text[-1]
    if current_word not in bigram_probs:
        break
    next_words = list(bigram_probs[current_word].keys())
    next_word_probs = list(bigram_probs[current_word].values())
    next_word = random.choices(next_words, next_word_probs)[0]
    text.append(next_word)
generated_text = ' '.join(text)
print("Generated Text:", generated_text)
