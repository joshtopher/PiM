import nltk
from sentiment import SentimentBot


def main():
    # nltk.download('vader_lexicon', quiet=False)
    bot = SentimentBot()
    bot.test_accuracy()

main()