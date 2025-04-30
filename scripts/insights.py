import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

def top_keywords(series, n=20):
    all_words = ' '.join(series).split()
    return Counter(all_words).most_common(n)

def analyze_trends(df):
    # Monthly sentiment trends
    monthly = df.set_index('date').resample('M')['vader_score'].mean()
    return monthly

def brand_comparison(df):
    return df.groupby('brand')['vader_score'].agg([
        'mean', 'count', 'std'
    ]).round(3)

def campaign_impact(df, campaign_date):
    before = df[df['date'] < campaign_date]['vader_score'].mean()
    after = df[df['date'] >= campaign_date]['vader_score'].mean()
    return (after - before) / before * 100

def main():
    # Load data
    df = pd.read_csv('data/clean/comments_sentiment.csv', parse_dates=['date'])
    
    # Analyze by sentiment
    pos = df[df['sentiment']=='positive']['clean']
    neg = df[df['sentiment']=='negative']['clean']
    
    # Get insights
    print("\nTop Positive Keywords:")
    print(top_keywords(pos, n=10))
    
    print("\nTop Negative Keywords:")
    print(top_keywords(neg, n=10))
    
    print("\nBrand Performance:")
    print(brand_comparison(df))
    
    # Analyze campaign impact
    campaign_date = '2025-03-01'
    impact = campaign_impact(df, campaign_date)
    print(f"\nCampaign Impact: {impact:.1f}% change in sentiment")
    
    # Save visualizations
    plt.figure(figsize=(10,6))
    analyze_trends(df).plot()
    plt.title('Sentiment Trends Over Time')
    plt.savefig('data/reports/sentiment_trends.png')
    
    # Save detailed insights
    insights = {
        'overall_sentiment': df['sentiment'].value_counts().to_dict(),
        'brand_performance': brand_comparison(df).to_dict(),
        'campaign_impact': impact,
        'top_positive': dict(top_keywords(pos, 10)),
        'top_negative': dict(top_keywords(neg, 10))
    }
    
    pd.DataFrame(insights).to_csv('data/reports/detailed_insights.csv')

if __name__ == "__main__":
    main()