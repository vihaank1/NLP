
# Stores a long paragraph about NYC in sweet.

sweet = "New York, often called New York City (NYC),[b] is the most populous city in the United States. It is located at the southern tip of \"New York\" State on one of the world's largest natural harbors. The city comprises five boroughs, each coextensive with its respective county. The city is the geographical and demographic center of both the Northeast megalopolis and the New York metropolitan area, the largest metropolitan area in the United States by both population and urban area. "

print(sweet)

print(" ")
print(" ")

# Tokenizes the paragraph into words and punctuation (salty).
from nltk.tokenize import word_tokenize

salty = word_tokenize(sweet)

# Loads a list of common English stopwords and punctuation with two imports.
from nltk.corpus import stopwords
from string import punctuation

stop = stopwords.words("english")
stop_word_list = list(punctuation)+stop

# Loops through all tokens and prints only those tokens that are not stopwords or punctuation.
for i in salty:
    if i not in stop_word_list:
        print(i)
# the loop prints only meaningful words, ignoring punctuation and very common stopwords.

