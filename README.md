# PiM
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

# Planned Features
- Find large amount of training data.(IN PROGRESS)
- Switch from nltk to sklearn for sentiment analysis.(IN PROGRESS)
- Keep track of average user sentiment and other useful statistics.
- Keeping track of malicious messages and reporting them to moderators

# Updates
- Added basic bot commands for server management.
- Added sentiment analysis using VADER. The following shows the effectiveness of VADER on the given data:
![image](https://github.com/joshtopher/PiM/assets/102866050/9cf94153-f291-4383-811c-f794b90d2105)

In the case of this project, the score I am most concerned with is the recall of negatives, since it is important for the bot not to miss any negative messages. Therefore, at this point in time, I will be working on obtaining training data, and training a sentiment analysis tool with sklearn, which will allow me to more easily fine tune the ratings of the bot.



# Citations
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
