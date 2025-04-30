import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()
        
    def get_vader_sentiment(self, text):
        return self.vader.polarity_scores(text)['compound']
    
    def get_textblob_sentiment(self, text):
        return TextBlob(text).sentiment.polarity
    
    def get_aspect_sentiments(self, text, aspects):
        sentiments = {}
        for aspect in aspects:
            if aspect in text.lower():
                sent = self.get_vader_sentiment(text)
                sentiments[aspect] = sent
        return sentiments

def main():
    # Load clean data
    df = pd.read_csv('data/clean/comments_clean.csv', parse_dates=['date'])
    
    # Initialize analyzer
    analyzer = SentimentAnalyzer()
    
    # Calculate overall sentiment
    df['vader_score'] = df['clean'].apply(analyzer.get_vader_sentiment)
    df['tb_polarity'] = df['clean'].apply(analyzer.get_textblob_sentiment)
    
    # Categorize sentiment
    bins = [-1, -0.05, 0.05, 1]
    labels = ['negative', 'neutral', 'positive']
    df['sentiment'] = pd.cut(df['vader_score'], bins=bins, labels=labels)
    
    # Aspect-based sentiment analysis
    aspects = ['quality', 'price', 'service', 'delivery', 'design', 'fabric']
    for aspect in aspects:
        df[f'aspect_{aspect}'] = df['clean'].apply(
            lambda x: analyzer.get_aspect_sentiments(x, [aspect]).get(aspect, np.nan)
        )
    
    # Save results
    df.to_csv('data/clean/comments_sentiment.csv', index=False)
    
    # Print summary
    print("\nOverall Sentiment Distribution:")
    print(df['sentiment'].value_counts(normalize=True).round(3))
    
    print("\nAspect-based Sentiment Averages:")
    aspect_cols = [col for col in df.columns if col.startswith('aspect_')]
    print(df[aspect_cols].mean().round(3))

if __name__ == "__main__":
    main()