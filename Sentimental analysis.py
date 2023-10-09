from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    
    # Classify the polarity of the text
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Example usage
marketing_text = "Our new product is innovative and amazing!"
sentiment = analyze_sentiment(marketing_text)
print(f"Sentiment: {sentiment}")
