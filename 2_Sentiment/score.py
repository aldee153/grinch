import nltk
from nltk import sentiment
nltk.download('vader_lexicon')

# load the inbuilt vader Sentiment Analyzer
senti_analyze = sentiment.vader.SentimentIntensityAnalyzer()

# Create a dict with polarity scores, we will use compound score only.
senti_analyze.polarity_scores(df.script[0])

# Apply on all lyrics and store the ['negative', 'neutral', 'positive'] segments as well.
df['sentiment_score'] = pd.DataFrame(df.script.apply(senti_analyze.polarity_scores).tolist())['compound']
df['sentiment'] = pd.cut(df['sentiment_score'], [-np.inf, -0.35, 0.35, np.inf], labels=['negative', 'neutral', 'positive'])

df.head()