
word = input("Enter a word:")

print("Word:", word)
print("Length of the word:", len(word))
print("Characters in the given word:", list(word))

pairs = [(word[i], word[i+1]) for i in range(len(word)-1)]
print("Adjacent pairs:", pairs)
