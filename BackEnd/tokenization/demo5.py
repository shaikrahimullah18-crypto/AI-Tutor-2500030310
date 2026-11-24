
corpus = {
    "play": 5,
    "playing": 3,
    "played": 2
}

print("Corpus:", corpus)
print("Length of corpus:", len(corpus))

for word in corpus:
    print(word)

for count in corpus.values():
    print(count)

for word, count in corpus.items():
    print(word, count)
