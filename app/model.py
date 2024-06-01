import pandas as pd
import re
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from tensorflow.keras.models import load_model
import pickle

nltk.download('stopwords')
nltk.download('vader_lexicon')

def clean(text):
    if not isinstance(text, str):
        return ""
    stop_words = set(stopwords.words('english'))
    stemmer = SnowballStemmer("english")
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    text = ' '.join(stemmer.stem(word) for word in text.split() if word not in stop_words)
    return text

model = load_model('./static/my_model.keras')
with open('./static/tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

data = pd.read_csv("./static/12-05-2024.csv")
owner_dummies = pd.get_dummies(data['tweet_owner'], prefix='owner')
X_columns = pd.concat([pd.DataFrame(tfidf_vectorizer.transform(data['tweet_content'].apply(clean)).toarray(), columns=tfidf_vectorizer.get_feature_names_out()), owner_dummies], axis=1).columns

def predict_tweet_effect(tweet, tweet_owner):
    tweet_cleaned = clean(tweet)
    tweet_tfidf = tfidf_vectorizer.transform([tweet_cleaned]).toarray()
    tweet_tfidf_df = pd.DataFrame(tweet_tfidf, columns=tfidf_vectorizer.get_feature_names_out())
    owner_dummies_new = pd.get_dummies(pd.Series([tweet_owner]), prefix='owner')
    owner_dummies_df = pd.DataFrame(columns=owner_dummies.columns)  # Modeldeki tüm dummy sütunlarını oluşturma
    owner_dummies_df = pd.concat([owner_dummies_df, owner_dummies_new], ignore_index=True).fillna(0)
    tweet_final = pd.concat([tweet_tfidf_df, owner_dummies_df], axis=1)
    tweet_final = tweet_final.reindex(columns=X_columns, fill_value=0)
    

    prediction = model.predict(tweet_final)
    prediction_label = (prediction > 0.5).astype("int32")[0][0]
    
    return prediction_label == 1
