import pandas as pd # type: ignore
import nltk # type: ignore
from sklearn.feature_extraction.text import CountVectorizer # type: ignore
from sklearn.naive_bayes import MultinomialNB # type: ignore
from nltk.corpus import stopwords # type: ignore

# Download stopwords if needed
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Step 1: Load and clean training data
df = pd.read_csv("email.csv")
df.columns = ['text', 'label']
df['label'] = df['label'].map({'phishing': 1, 'safe': 0})

def clean_text(text):
    words = text.lower().split()
    return " ".join([word for word in words if word not in stop_words])
df['text'] = df['text'].apply(clean_text)

# Step 2: Train the model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

model = MultinomialNB()
model.fit(X, y)

# Step 3: Function to predict new emails
def predict_email(email):
    cleaned = clean_text(email)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    return " Phishing Email!" if prediction == 1 else " Safe Email!"

# Step 4: Try your own input
while True:
    user_input = input("\n Enter your email text (or type 'exit' to quit):\n")
    if user_input.lower() == "exit":
        print(" Goodbye!")
        break
    print("Result:", predict_email(user_input))
