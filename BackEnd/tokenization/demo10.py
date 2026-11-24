from collections import Counter

word_freqs = {
    "play": 5,
    "playing": 3,
    "played": 2,
}

print("---------- WORD FREQUENCIES ----------")
for word, freq in word_freqs.items():
    print(f"{word} : {freq}")

print("\n---------- ADJACENT CHARACTER PAIRS ----------")
pair_freqs = Counter()
for word, freq in word_freqs.items():
    chars = list(word)
    pairs = list(zip(chars, chars[1:]))
    print(f"\nWord: {word}")
    print(f"Character Pairs: {pairs}")
    for p in pairs:
        pair_freqs[p] += freq

print("\n---------- INITIAL PAIR FREQUENCIES ----------")
for pair, freq in pair_freqs.items():
    print(f"{pair} : {freq}")

# Build base character vocabulary (sorted for deterministic IDs)
vocab = ["[UNK]"] + sorted({ch for w in word_freqs for ch in w})
token_to_id = {tok: idx for idx, tok in enumerate(vocab)}

# Iterative BPE merges
splits = {w: list(w) for w in word_freqs}
num_merges = 8

for _ in range(num_merges):
    counts = Counter()
    for word, freq in word_freqs.items():
        s = splits[word]
        for i in range(len(s) - 1):
            counts[(s[i], s[i + 1])] += freq
    if not counts:
        break
    best_pair, _ = counts.most_common(1)[0]
    merged_tok = best_pair[0] + best_pair[1]
    if merged_tok not in token_to_id:
        token_to_id[merged_tok] = len(token_to_id)

    for word in splits:
        s = splits[word]
        new_s = []
        i = 0
        while i < len(s):
            if i < len(s) - 1 and (s[i], s[i + 1]) == best_pair:
                new_s.append(merged_tok)
                i += 2
            else:
                new_s.append(s[i])
                i += 1
        splits[word] = new_s

print("\n---------- LEARNED VOCABULARY ----------")
for tok, idx in token_to_id.items():
    print(f"{tok} : {idx}")