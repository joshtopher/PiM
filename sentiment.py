import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from sklearn.metrics import classification_report
from helper import *
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline




# Sentiment Analysis Model using VADER
class SentimentBot():

    def __init__(self):
        self.data = csv_data_to_dict("archive/Messages.csv") # loading training data
        self.vader_model = SentimentIntensityAnalyzer()

    def polarity(self, message: str) -> dict:
        return self.vader_model.polarity_scores(pre_process(message))

    def test_accuracy(self):
        gold_labels = []
        vader_labels = []
        # iterate through data
        for message_id, info in self.data.items():
            # retrieve the text and golden label
            message = info['text']
            label = info['sentiment_label']

            # get VADER polarity scores and use helper function to convert them to labels
            output = self.polarity(message)
            vader_label = vader_output_to_label(output)

            # add golden labels and VADER labels to respective lists
            vader_labels.append(vader_label)
            gold_labels.append(label)

        print(classification_report(gold_labels, vader_labels, digits=4))

# Sentiment Analysis Model using LinearSVC
class SentimentBot2():

    def __init__(self):
        self.x_test = []
        self.y_test = []
        self.model = None
        self.data = csv_data_to_dict("archive/Messages.csv") # loading training data
        self.train()
    
    def predict(self, message: str) -> str:
        return self.model.predict([pre_process(message)])[0]
    
    def train(self):
        texts = []
        labels = []
        for message_id, info in self.data.items():
            texts.append(info['text'])
            labels.append(info['sentiment_label'])

        X_train, self.X_test, y_train, self.y_test = train_test_split(texts, labels, test_size=0.17, random_state=42)
        # Define the pipeline
        self.model = Pipeline([
        ('tfidf', TfidfVectorizer(preprocessor=pre_process, stop_words=stopwords.words('english'), 
                                  max_features=7000, ngram_range=(1,2), min_df=15, max_df=0.7)),
        ('clf', LinearSVC()),
        ])

        # Train the model
        self.model.fit(X_train, y_train)
    
    def test_accuracy(self):
            # Predictions
            predictions = self.model.predict(self.X_test)

            # Evaluate the model
            accuracy = accuracy_score(self.y_test, predictions)
            print(f'Model accuracy: {accuracy}')

