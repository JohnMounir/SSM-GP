from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import normalize
import pandas as pd
import numpy as np
from textblob import TextBlob
from joblib import dump , load
import nltk
class FeatureExtraction:
    def __init__(self,list):
        self.list = []
        self.list = list
        self.SentimentList = []
        self.SubjList = []
    def Sentiment(self):
        for x in range(len(self.list)):
            polartiy = TextBlob(self.list[x]).sentiment
            self.SentimentList.append(polartiy.polarity)
            self.SubjList.append(polartiy.subjectivity)
        return self.SentimentList

    def Training_TFIDF(self):
        Vectorizer = TfidfVectorizer(ngram_range=(1,2) , token_pattern='(?u)\\b\\w+\\b' , smooth_idf=True)
        X = Vectorizer.fit_transform(self.list)
        dump(Vectorizer , "TFIDF.Model")
        T = X.toarray()
        return T
    def Test_TFIDF(self):
        Vocabulary = load("TFIDF.Model")
        X = Vocabulary.transform(self.list)
        T = X.toarray()
        return T
