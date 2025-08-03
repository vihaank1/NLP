# We perform the 4 types of stemming on word changed    

from nltk.stem import LancasterStemmer, RegexpStemmer, PorterStemmer, SnowballStemmer

l = LancasterStemmer()
r = RegexpStemmer('ing')
p = PorterStemmer()
s = SnowballStemmer('english')

# Stemming outputs
print(l.stem("changed"))
print(r.stem("changed"))
print(p.stem("changed"))
print(s.stem("changed"))

print(" ")
# We perform Lemmatization on word mice

from nltk.stem import WordNetLemmatizer

wl = WordNetLemmatizer()
print(wl.lemmatize('mice'))




