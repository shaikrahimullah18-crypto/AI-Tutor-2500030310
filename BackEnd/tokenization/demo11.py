from collections import Counter
import re

corpus = """
play play playing played player
i love learning python python python
generative ai helps students learn learn
is is a programming programming language
using artificial intelligence transforming education
"""

words = re.findall(r"\b\w+\b", corpus.lower())
word_freqs = Counter(words)

print("---------- WORD FREQUENCIES ----------")
for word, freq in word_freqs.items():
    print(f"{word} : {freq}")

print("\n---------- ADJACENT CHARACTER PAIRS ----------")
for word in word_freqs:
    chars = list(word)
    pairs = list(zip(chars, chars[1:]))
    print(f"\nWord: {word}")
    print(f"Character Pairs: {pairs}")