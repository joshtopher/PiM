import csv
import nltk
from nltk.sentiment.util import mark_negation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def csv_data_to_dict(filename: str) -> dict:
    # accumulator value
    ret: dict = {}


    # open csv file containing data
    with open(filename) as f:
        reader = csv.reader(f)
        # iterate through rows of csv to add specific values to ret
        counter: int = 1
        for row in reader:
            data: dict = {"sentiment_label": (row[3]), "text": row[1]}
            ret[counter] = data
            counter += 1
    return ret


def vader_output_to_label(output: dict) -> str:
    compound = output['compound']
    if compound < 0:
        return 'negative'
    elif compound == 0:
        return 'neutral'
    else:
        return 'positive'


def pre_process( text: str) -> str:
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Apply POS tagging
    tokens = pos_tag(tokens)

    # Merge POS tags with tokens
    tokens = [' '.join(t) for t in tokens]

    # Apply negation
    tokens = mark_negation(tokens)

    return ' '.join(tokens)