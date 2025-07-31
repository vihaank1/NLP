# NLP example from NLP wikipedia

import nltk
nltk.download('all')


# here we tokenize
text = "Natural language processing (NLP) is the processing of natural language information by a computer. The study of NLP, a subfield of computer science, is generally associated with artificial intelligence. NLP is related to information retrieval, knowledge representation, computational linguistics, and more broadly with linguistics."

from nltk.tokenize import word_tokenize

w = word_tokenize(text)
print(w)

print("----------------------------------")

# Analyze parts of speech
from nltk import pos_tag

p = pos_tag(w)
print(p)
