
text = "python is a programming language"

tokens = text.split()

print("Tokens:", tokens)
print("Length of tokens:", len(tokens))

print("First token:", tokens[0])
print("Last token:", tokens[-1])
print("Last token:", tokens[-1])

print("First two tokens:", tokens[:2])
print("Tokens in reverse order:", tokens[::-1])
print("Last two tokens:", tokens[-2:])

print(",".join(tokens))
