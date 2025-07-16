
import pandas as pd   # type: ignore # to read CSV file
import nltk           # type: ignore # for natural language tools
nltk.download('stopwords')  # download English stopwords (like "is", "the", "and")

from nltk.corpus import stopwords # type: ignore
stop_words = set(stopwords.words('english'))

# Step 1: Load your email data from CSV
df = pd.read_csv("email.csv")  # This file must be in the same folder as this .py file
df.columns = ['text', 'label']  # Rename the columns to 'text' and 'label'

# Step 2: Convert labels (phishing = 1, safe = 0)
df['label'] = df['label'].map({'phishing': 1, 'safe': 0})

# Step 3: Function to clean text
def clean_text(text):
    words = text.lower().split()  # Make lowercase, then split into words
    return " ".join([word for word in words if word not in stop_words])  # remove stopwords

# Step 4: Apply cleaning function to every email
df['text'] = df['text'].apply(clean_text)

# Step 5: Show the cleaned data
print(df.head())
