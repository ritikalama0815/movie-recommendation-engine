import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

#--------------------------#

##Step 1: Read CSV File
df = pd.read_csv("dataset.csv")
print(df.head())
print(df.columns)


##Step 2: Select "important" columns

important_features = ["keywords", "cast", "genres", "director"]

for feature in important_features:
	df[feature] = df[feature].fillna("") # fill NaN values with empty string cuz we got error below before
# Combines params into one string
def combine_features(row):
	try:
		return row["keywords"] + " " + row["cast"] + " " + row["genres"] + " " + row["director"]
	except:
		print("Error:", row)

df["combined_features"] = df.apply(combine_features, axis=1) # axis=1 means apply function to each row

print(df["combined_features"].head())

##Step 3: Create count matrix from this new combined column
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

similarity_scores = cosine_similarity(count_matrix)

movie_user_likes = input("Enter your favourite movie: ")