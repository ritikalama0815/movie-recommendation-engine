# Movie Recommendation System

A content-based movie recommendation engine built with Python and scikit-learn.

This project:

* Loads movie data from a CSV file
* Extracts important text features
* Converts text into numerical vectors using `CountVectorizer`
* Calculates similarity scores with cosine similarity
* Recommends similar movies based on user input

Tech Stack:

* Python, Pandas, NumPy, scikit-learn

Example Features:

* Movie title, Keywords, Cast, Genres, Director

How to Run:

1. Install dependencies:

```bash
pip install pandas numpy scikit-learn
```

2. Add your dataset file:

```bash
dataset.csv
```

3. Run the script:

```bash
python main.py
```

Dataset Format Example:

```csv
index,title,keywords,cast,genres,director
0,Avatar,future world,Sam Worthington,Action,James Cameron
```

