# paragraph of text we want to analyze. It contains the word "horizon" whose meaning we want to figure out based on context
sunset = "Sunset (or sundown) is the disappearance of the Sun at the end of the Sun path, below the horizon of the Earth (or any other astronomical object in the Solar System) due to its rotation. As viewed from everywhere on Earth, it is a phenomenon that happens approximately once every 24 hours, except in areas close to the poles."

# We import the lesk function from nltk, which helps us find the correct meaning of a word in a sentence.
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize      # function that splits text into individual words, called "tokens"

# result from lesk algorithm is saved into the variable 'lk' as a Synset
lk = lesk(word_tokenize(sunset), "horizon")
print(lk)
print("")
print(lk.definition())   # prints the full dictionary definition of the chosen meaning of "horizon".
