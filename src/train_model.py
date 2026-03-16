import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("tickets_dataset.csv")

df["text"] = df["title"] + " " + df["body"]

X = df["text"]
y = df["category"]

vectorizer = TfidfVectorizer()

X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2
)

model = LogisticRegression(max_iter=200)

model.fit(X_train, y_train)

print("Model trained")
