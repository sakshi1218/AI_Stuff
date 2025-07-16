# train_model.py

import pandas as pd # type: ignore
import nltk # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.feature_extraction.text import CountVectorizer # type: ignore
from sklearn.naive_bayes import MultinomialNB # type: ignore
from sklearn.metrics import accuracy_score # type: ignore
from nltk.corpus import stopwords # type: ignore

# Download stopwords (if not already downloaded)
nltk.download('stopwords')

# Load dataset
df = pd.read_csv("email.csv")
df.columns = ['text', 'label']
df['label'] = df['label'].map({'phishing': 1, 'safe': 0})

# Remove stopwords
stop_words = set(stopwords.words('english'))
def clean_text(text):
    words = text.lower().split()
    return " ".join([word for word in words if word not in stop_words])
df['text'] = df['text'].apply(clean_text)

# STEP 4: Vectorize the cleaned text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])  # Convert text to numbers

# STEP 5: Prepare labels
y = df['label']

# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict using test data
y_pred = model.predict(X_test)

# Show accuracy
print(" Model Accuracy:", accuracy_score(y_test, y_pred))
