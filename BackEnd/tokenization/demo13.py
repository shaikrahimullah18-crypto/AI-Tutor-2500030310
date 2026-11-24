from collections import Counter

# Reconstructed from the visible token pairs and decoded output in demo13.py
tokens = [
    "_", "I", "_", "_", "a", "m", "_", "_play", "i", "ng", "_",
    "_", "f", "o", "o", "t", "b", "a", "l", "l"
]

token_freq = Counter(tokens)
pair_freq = Counter(zip(tokens, tokens[1:]))

print("========== TOKEN FREQUENCIES ==========")
for tok, cnt in token_freq.items():
    print(f"{tok} : {cnt}")

print("\n========== ADJACENT TOKEN PAIR FREQUENCIES ==========")
for pair, cnt in pair_freq.items():
    print(f"{pair} : {cnt}")

# Map '_' back to spaces (matching how '_' acts as whitespace marker in the output)
decoded_text = "".join(" " if t == "_" else t for t in tokens)

print("\n========== DECODED TEXT ==========")
print(f"Decoded Text: {decoded_text}")