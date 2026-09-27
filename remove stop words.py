stopwords = ['the', 'is', 'in', 'and', 'to', 'a', 'of', 'for', 'on', 'with']

text = "This is a sample text to remove stopwords from."
words = text.split()
filtered = [word for word in words if word.lower() not in stopwords]
print(" ".join(filtered))
