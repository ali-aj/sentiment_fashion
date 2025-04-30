import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download(['stopwords', 'punkt', 'wordnet'])
from nltk.stem import WordNetLemmatizer

STOP = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    # Remove URLs
    text = re.sub(r"http\S+", "", text)
    # Remove mentions
    text = re.sub(r"@\S+", "", text)
    # Remove hashtags
    text = re.sub(r"#\S+", "", text)
    # Remove special chars
    text = re.sub(r"[^a-zA-Z ]", "", text)
    # Tokenize
    tokens = word_tokenize(text.lower())
    # Remove stopwords and lemmatize
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in STOP]
    return " ".join(tokens)

def main():
    # Load raw data
    df = pd.read_csv('data/raw/comments_twitter.csv')
    
    # Basic filtering
    df.drop_duplicates(subset=['content'], inplace=True)
    df = df[df['content'].str.len() > 10]
    
    # Clean text
    df['clean'] = df['content'].apply(clean_text)
    
    # Remove empty cleaned texts
    df = df[df['clean'].str.len() > 0]
    
    # Add length features
    df['word_count'] = df['clean'].apply(lambda x: len(x.split()))
    
    df.to_csv('data/clean/comments_clean.csv', index=False)
    print(f"Cleaned {len(df)} comments. Average word count: {df['word_count'].mean():.1f}")

if __name__ == "__main__":
    main()