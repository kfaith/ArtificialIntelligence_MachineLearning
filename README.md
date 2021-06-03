# ArtificialIntelligence_MachineLearning

This program takes a large tweet-set from a file, and assigns category labels to the tweet-set, it will read each tweet individually and categorize the data held in each tweet. If it contains a feature, it will input a 1 into a dictionary, if it does not contain the feature, it will input a 0. 

For example, if looking to see if a tweet had an emoji, we search through every character in the tweet, and if an emoji is found, it appends a 1 to the dictionary. If an emoji isnt found in the tweet, the dictionary will instead be appended with a 0.

Once the dictionary is completed, the program stores the dictionaries data in a JSON file, which is later used to carry out a 10-fold cross validation of different machine learning algorithms. Due to the existence of libraries which already carry out this functionality, the program simply makes calls to the library instead.
