from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.metrics import classification_report
from helper import *


class SentimentBot:

    def __init__(self):
        self.vader_model = SentimentIntensityAnalyzer()
        self.data = csv_data_to_dict("archive/Messages.csv") # loading training data



    def polarity(self, message: str) -> dict:
        return self.vader_model.polarity_scores(message)


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


