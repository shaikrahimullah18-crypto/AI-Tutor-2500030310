from collections import Counter
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("xlm-roberta-base")
sentence = input("Enter a sentence: ")

tokens = tokenizer.tokenize(sentence)
token_ids = tokenizer.convert_tokens_to_ids(tokens)
decoded_text = tokenizer.decode(token_ids, skip_special_tokens=True)

token_freq = Counter(tokens)
pair_freq = Counter(zip(tokens, tokens[1:]))

print("\n========== TOKENIZATION RESULT ==========")
print(f"Original Text: {sentence}")
print(f"SentencePiece Tokens: {tokens}")
print(f"Token IDs: {token_ids}")
print(f"Total Tokens: {len(tokens)}")

print("\n========== TOKEN FREQUENCIES ==========")
for tok, cnt in token_freq.items():
    print(f"{tok} : {cnt}")

print("\n========== ADJACENT TOKEN PAIR FREQUENCIES ==========")
for pair, cnt in pair_freq.items():
    print(f"{pair} : {cnt}")

print("\n========== DECODED TEXT ==========")
print(f"Decoded Text: {decoded_text}")