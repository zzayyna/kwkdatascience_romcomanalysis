import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# files
old_reviews = pd.read_excel("oldreviews.xlsx", header=None, names=["review", "year"])
middle_reviews = pd.read_excel("middlereviews.xlsx", header=None, names=["review", "year"])
new_reviews = pd.read_excel("newreviews.xlsx", header=None, names=["review", "year"])

# cleanupp
stop_words = set(stopwords.words('english'))
stop_words.update(["movie","one","thing","lose a guy","film","make"])
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return " ".join(words)

old_reviews["clean"] = old_reviews["review"].apply(clean_text)
middle_reviews["clean"] = middle_reviews["review"].apply(clean_text)
new_reviews["clean"] = new_reviews["review"].apply(clean_text)

# sentiment analysis
sia = SentimentIntensityAnalyzer()

old_reviews["sentiment"] = old_reviews["clean"].apply(lambda x: sia.polarity_scores(x)["compound"])
middle_reviews["sentiment"] = middle_reviews["clean"].apply(lambda x: sia.polarity_scores(x)["compound"])
new_reviews["sentiment"] = new_reviews["clean"].apply(lambda x: sia.polarity_scores(x)["compound"])

print("Avg Old Sentiment:", old_reviews["sentiment"].mean())
print("Avg Middle Sentiment:", middle_reviews["sentiment"].mean())
print("Avg New Sentiment:", new_reviews["sentiment"].mean())

# visualize sentiment
old_by_year = old_reviews.groupby("year")["sentiment"].mean()
middle_by_year = middle_reviews.groupby("year")["sentiment"].mean()
new_by_year = new_reviews.groupby("year")["sentiment"].mean()

# Plot
plt.figure(figsize=(12,6))
plt.plot(old_by_year.index, old_by_year.values, marker='o', label='Old Reviews')
plt.plot(middle_by_year.index, middle_by_year.values, marker='o', label='Middle Reviews')
plt.plot(new_by_year.index, new_by_year.values, marker='o', label='New Reviews')
plt.xlabel("Year")
plt.ylabel("Average Sentiment")
plt.title("Sentiment Over Time: 'How to lose a Guy in 10 Days' Reviews")
plt.legend()
plt.grid(True)
plt.show()

# word cloud
def plot_wordcloud(text_series, title):
    text = " ".join(text_series.dropna().astype(str))
    
    wc = WordCloud(
        width=800,
        height=400,
        background_color="white",
        max_words=200
    ).generate(text)
    
    plt.figure(figsize=(10,5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off") 
    plt.title(title, fontsize=16)
    plt.show()

plot_wordcloud(old_reviews["clean"], "Old Reviews Word Cloud")
plot_wordcloud(middle_reviews["clean"],"Middle Reviews Word Cloud")
plot_wordcloud(new_reviews["clean"], "New Reviews Word Cloud")