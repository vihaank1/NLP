
element = "I am happy it is a sunny day everything is fun I am happy"

from nltk.tokenize import word_tokenize

# Tokenize the input string into individual words
w = word_tokenize(element)

# Import collocation and n-gram tools from NLTK
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder, ngrams

# Create a bigram finder to identify all consecutive word pairs (bigrams)
bcf=BigramCollocationFinder.from_words(w)
tcf=TrigramCollocationFinder.from_words(w) # Create a trigram finder to identify all consecutive word triples (trigrams)


bigram_freqs = dict(bcf.ngram_fd.items())  # Extract bigram frequencies as a dictionary
trigram_freqs = dict(tcf.ngram_fd.items())  # Extract trigram frequencies as a dictionary
n = ngrams(w, 4)         # Generate 4-grams

print(bigram_freqs)
print(" ")
print(trigram_freqs)
print(" ")
print(n)

# Loop through and print each 4-gram tuple
for i in n:
    print(i)
