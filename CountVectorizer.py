goodness = ["it was the year 2017", "are you doing good"]

import pandas as pd

# Create a DataFrame with one column named "name" with text entries
df=pd.DataFrame({"name": goodness})
print(df)
print(" ")

# Import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
# Learns the vocabulary from the text data (fit) Transforms the text into a sparse matrix of word counts (transform)
best = cv.fit_transform(df["name"])

# Print the resulting sparse matrix
print(best)
print(" ")

# Print vocabulary dictionary
print(cv.vocabulary_)
