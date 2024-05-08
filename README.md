# PiM
(Python Intention Management)
This is a re-visit of one of my previous projects 'pybot'. Initially, the project was a Discord bot that helped manage discord servers, however this bot will attempt to use sentiment analysis to tag malicious messages and report them to the server owner.
'pybot' URL: https://github.com/joshtopher/pybot


To add PiM to your discord server, use this URL. PiM needs administrator privileges for full functionality.

URL: https://discord.com/oauth2/authorize?client_id=1215686228331073587&permissions=8&scope=bot


# Goals
1) To assess the difference in python programming, practices, readability, and knowledge with my current self and myself and myself before taking any higher level computer science classes('pybot').
2) To create a practical tool that I am able to use for myself and share with others.
3) To become more familiar with sentiment analysis tools used in a course I am currently taking: 'Text Mining for AI' at Vrije Universiteit Amsterdam.

# Current Features
- General server management functionality
- Sentiment analysis of messages using VADER
- Find large amount of training data
- Switch from nltk to sklearn for sentiment analysis.

# Planned Features
- Keep track of average user sentiment and other useful statistics.
- Keep track of malicious messages and report them to moderators

# Updates
- Added basic bot commands for server management.
- Added sentiment analysis using VADER. The following shows the effectiveness of VADER on the given data:
![image](https://github.com/joshtopher/PiM/assets/102866050/9cf94153-f291-4383-811c-f794b90d2105)

The accuracy and some other scores of this model are not where I would like them to be, so I will attempt to train a model using local data through the sklearn library.
- Added sentiment analysis using sklearn trained from data stored locally. The accuracy of this model is 67%, already an improvement from the previous model, however needs some fine-tuning.
- Added some feature engineering bringing up the accuracy to 68.4%, which I am satisfied with for now but will revisit.

# Citations
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
