# Comprehensive Project Report: Sentiment Analysis of Customer Comments on Pakistani Fashion Brands

## Introduction
This report presents a detailed sentiment analysis of customer comments on prominent Pakistani fashion brands, including Khaadi, Gul Ahmed, Sapphire, J., and Bonanza Satrangi. The project leverages social media data from platforms like Facebook and Twitter to evaluate customer sentiments, identify trends, and provide actionable insights for stakeholders. Utilizing free and open-source tools, the analysis ensures accessibility and reproducibility, adhering to specified requirements. The primary objectives include data collection, preprocessing, sentiment analysis, visualization, and deriving conclusions with recommendations for future enhancements.

## Project Setup
The project is implemented in a Jupyter Notebook environment using Python 3. The following libraries were employed:

- **pandas**: For data manipulation and analysis.
- **nltk**: For natural language processing, including VADER sentiment analysis.
- **matplotlib** and **seaborn**: For creating visualizations.
- **wordcloud**: For generating word clouds.
- **emoji**: For handling emoji removal in text preprocessing.

The setup involves installing these libraries via the command:
```
pip install pandas nltk matplotlib seaborn wordcloud emoji
```
Additionally, NLTK datasets (`vader_lexicon` and `stopwords`) were downloaded to support sentiment analysis and text cleaning.

## Methodology

### Data Collection and Loading
- **Dataset**: Customer comments were sourced from social media and stored in `pakistani_fashion_comments.csv`.
- **Structure**: The dataset includes columns:
  - `brand`: Name of the fashion brand (e.g., J., Gul Ahmed).
  - `text`: Customer comment text.
  - `created_at`: Comment date (converted to datetime format).
  - `platform`: Source platform (e.g., Facebook, Twitter).
  - `language`: Predominantly English, with some Roman-Urdu phrases.
- **Loading**: Data was loaded into a pandas DataFrame, with column names standardized (`comment` to `text`, `date` to `created_at`).

**Sample Data**:
| Brand            | Text                                                      | Created At  | Platform | Language |
|------------------|-----------------------------------------------------------|-------------|----------|----------|
| J.               | The Ramadan collection is breathtaking! Traditional yet modern. | 2024-02-05  | Facebook | English  |
| Bonanza Satrangi | Lahore store ka experience aam tha, na khas acha na bura | 2024-02-21  | Twitter  | English  |
| J.               | Website crashed during sale and lost my cart items        | 2024-02-15  | Twitter  | English  |

### Data Preprocessing
A comprehensive cleaning process was applied to prepare the data for analysis:
- **Cleaning Steps**:
  - Removed URLs, mentions, and hashtags using regular expressions (`re.sub`).
  - Eliminated emojis with the `emoji.replace_emoji` function.
  - Stripped non-alphabetic characters and converted text to lowercase.
  - Filtered out stopwords (English from NLTK and custom Roman-Urdu list: `hai`, `ka`, `ke`, etc.) and words shorter than two characters.
- **Implementation**: A `clean_text` function processed the text, storing results in a new `clean_text` column.

### Sentiment Analysis
- **Tool**: VADER (Valence Aware Dictionary and sEntiment Reasoner) from NLTK, optimized for social media text.
- **Scoring**: The compound polarity score classified sentiments:
  - Positive: > 0.05
  - Negative: < -0.05
  - Neutral: -0.05 to 0.05
- **Application**: Sentiments were assigned to each `clean_text` entry, stored in a `sentiment` column.

### Visualization
The analysis generated multiple visualizations:
- **Sentiment Distribution Bar Chart** (`sentiment_distribution.png`):
  - Displays counts of positive, negative, and neutral sentiments.
  - Example: Approximately 250 positive, 200 neutral, 50 negative comments.
  - ![Alt text](https://github.com/ali-aj/sentiment_fashion/blob/104bf159162bf1ce3a20db85e2f981a0448627be/sentiment_distribution.png)
- **Sentiment Trends Line Graph** (`sentiment_trends.png`):
  - Tracks sentiment proportions over time (January to May 2024).
  - Observations: Positive sentiment rose to 0.55 by May, negative remained stable at ~0.1.
  - ![Alt text](https://github.com/ali-aj/sentiment_fashion/blob/104bf159162bf1ce3a20db85e2f981a0448627be/sentiment_trends.png)
- **Word Clouds**:
  - **Positive Word Cloud** (`positive_wordcloud.png`): Highlights terms like "breathtaking," "quality," "modern."
  - ![Alt text](https://github.com/ali-aj/sentiment_fashion/blob/104bf159162bf1ce3a20db85e2f981a0448627be/positive_wordcloud.png)
  - **Negative Word Cloud** (`negative_wordcloud.png`): Features terms like "delayed," "website crashed," "poor quality."
  - ![Alt text](https://github.com/ali-aj/sentiment_fashion/blob/104bf159162bf1ce3a20db85e2f981a0448627be/negative_wordcloud.png)

## Results and Findings
- **Sentiment Distribution**: Predominantly positive sentiment (~50%), followed by neutral (~40%), and a minority negative (~10%), indicating favorable customer perception.
- **Temporal Trends**: Positive sentiment increased over time, peaking in May 2024, while neutral sentiment peaked in March, possibly tied to sales events.
- **Key Insights**:
  - **Positive Drivers**: Appreciation for innovative designs, hijab-friendly options, and quality fabrics.
  - **Negative Drivers**: Operational issues like website crashes and delivery delays.
- **Themes**:
  - Positive: Design excellence and cultural relevance.
  - Negative: Technical and service-related complaints.

## Deliverables
The project produced:
- `pakistani_fashion_comments.csv`: Raw and processed dataset.
- `sentiment_distribution.png`: Bar chart of sentiment counts.
- `sentiment_trends.png`: Line graph of sentiment trends.
- `positive_wordcloud.png`: Word cloud for positive comments.
- `negative_wordcloud.png`: Word cloud for negative comments.

## Conclusion
This project successfully analyzed customer sentiments for Pakistani fashion brands, meeting its objectives of data preprocessing, sentiment classification, and visualization. 

## Recommendations
- **Operational Improvements**: Enhance website reliability and streamline delivery processes to reduce negative sentiment.
- **Marketing Strategy**: Leverage positive feedback on designs and sustainability in campaigns.
- **Future Extensions**:
  - Expand dataset size or include more brands.
  - Focus on specific events (e.g., Eid sales) for deeper temporal insights.
  - Integrate advanced techniques like machine learning for nuanced analysis.

This report serves as a foundation for strategic decision-making in the Pakistani fashion industry, with opportunities for further refinement based on stakeholder needs.
