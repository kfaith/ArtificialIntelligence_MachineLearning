import csv
import nltk
import emojis
import numpy
from collections import Counter
from nltk import ngrams
from nltk import everygrams
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
from nltk.corpus import stopwords 
from nltk.tokenize import TweetTokenizer
from sklearn.model_selection import cross_val_score


             
#this method is used to input a line of text from the csv file, and remove any stopwords from the english language, and then return the 
#sentence as an array of words without the stopwords in it.
def tokenizeAndFilter(text):
    fullTweet = text
    stopWords = set(stopwords.words('english'))
    tknzr = TweetTokenizer()
    wordTokens = tknzr.tokenize(fullTweet)

    for w in Tokens: 
        if w not in stopWords: 
            revisedSentence.append(w) 
    
    
    return revisedSentence 



nWordArray1 = []
nWordArray2 = []
nWordArray3 = []
nWordArray4 = []
nWordArray5 = []

#each of the nGramToArray methods are used to find what the top 50 grams of the csv file is, then put them into an array
#which is later used to check and see if the tweets contain any of those top 50 grams.
def nGramToArray1(nWordGramNum):

    for i in range(0,50):
        (word,numGrams) = nWordGramNum.most_common(50)[i]
        nWordArray1.append(*word)


def nGramToArray2(nWordGramNum):

    for i in range(0,50):
        ((word1,word2), numGrams) = nWordGrams2.most_common(50)[i]
        nWordArray2.append(word1 + " " + word2)


def nGramToArray3(nWordGramNum):

    for i in range(0,50):
        ((word1,word2,word3), numGrams) = nWordGrams3.most_common(50)[i]
        nWordArray3.append(word1 + " " + word2 + " " + word3)
    
def nGramToArray4(nWordGramNum):

    for i in range(0,50):
        ((word1,word2,word3,word4), numGrams) = nWordGrams4.most_common(50)[i]
        nWordArray4.append(word1 + " " + word2 + " " + word3 + " " + word4)

def nGramToArray5(nWordGramNum):

    for i in range(0,50):
        ((word1,word2,word3,word4,word5), numGrams) = nWordGrams5.most_common(50)[i]
        nWordArray5.append(word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5)


#This method takes the dictionary that is created later on in the project, and converts it to a csv file, so that the newly created csv file
#can be input into a machine learning algorithm and carry out a 10 fold validation on the matrix.
def printToOutputFile(dictionary):
    with open('tweetMatrix.csv', mode='w') as csvFile:
        fieldnames = ["tweets"] + ["hashtags"] + ["emojis"] + ["nWordGram1"] + ["nWordGram2"] + ["nWordGram3"] + ["nWordGram4"] + ["nWordGram5"] + ["popular"]
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)

        writer.writeheader()
        
        writer.writerow(dictionary)


        # The commented code below was a different attempt at writing a csv file using a stack overflow link, but I still cant get them to format how I want.
        # writer.writeheader()  
        # for key in dictionary.keys():
        #     csvFile.write("%s,%s\n"%(key,dictionary[key]))


# This is the main part of the assignment, this creates a dictionary with the headers as the keys, and has the data stored in those keys as
# either a 0 or a 1, depending on if the tweet contains the given feature.
with open('tweet-set2.txt', encoding="utf-8") as tweetFile:
    csvReader = csv.reader(tweetFile, delimiter=',')
    numLines = 0
    tweetNum = []
    tweetsDictionary = {}
    popularList = []
    hashtagList = []
    emojiList = []
    nWordList1 = []
    nWordList2 = []
    nWordList3 = []
    nWordList4 = []
    nWordList5 = []

    text = open('tweet-set2.txt', encoding="utf-8").read()
    

    # counts the number of ngrams in the text and stores them.
    nWordGrams1 = Counter(ngrams(text.split(), 1))
    nWordGrams2 = Counter(ngrams(text.split(), 2))
    nWordGrams3 = Counter(ngrams(text.split(), 3))
    nWordGrams4 = Counter(ngrams(text.split(), 4))
    nWordGrams5 = Counter(ngrams(text.split(), 5))

    # stores the top 50 of the ngrams into an array
    nGramToArray1(nWordGrams1)
    nGramToArray2(nWordGrams2)
    nGramToArray3(nWordGrams3)
    nGramToArray4(nWordGrams4)
    nGramToArray5(nWordGrams5)


    for row in csvReader:  #reads every row in the csv

        if numLines == 0:
            numLines += 1   
        else:
            tweetNum.append(numLines)   #what tweet number it is

            if row[0].__contains__('#'):  #if the tweet contains a hashtag
                hashtagList.append('1')
            else:
                hashtagList.append('0')

            if (emojis.count(row[0]) >= 1): #if the tweet contains an emoji
                emojiList.append('1')
            else:
                emojiList.append('0')


            #this is for the word grams, if the tweet has a word/words, put a 1 and break, otherwise keep going through 
            #until it reaches the end of the word array and the ticker is 50 then put a 0.(Doesnt contain the gram)
            for i in range(0,50):
                if row[0].__contains__(nWordArray1[i]):
                    nWordList1.append('1')
                    break
                elif i == 49 and not row[0].__contains__(nWordArray1[49]):
                    nWordList1.append('0')


            for i in range(0,50):
                if row[0].__contains__(nWordArray2[i]):
                    nWordList2.append('1')
                    break
                elif i == 49 and not row[0].__contains__(nWordArray2[49]):
                    nWordList2.append('0')
            

            for i in range(0,50):
                if row[0].__contains__(nWordArray3[i]):
                    nWordList3.append('1')
                    break
                elif i == 49 and not row[0].__contains__(nWordArray3[49]):
                    nWordList3.append('0')


            for i in range(0,50):
                if row[0].__contains__(nWordArray4[i]):
                    nWordList4.append('1')
                    break
                elif i == 49 and not row[0].__contains__(nWordArray4[49]):
                    nWordList4.append('0')


            for i in range(0,50):
                if row[0].__contains__(nWordArray5[i]):
                    nWordList5.append('1')
                    break
                elif i == 49 and not row[0].__contains__(nWordArray5[49]):
                    nWordList5.append('0')            

            popularList.append(row[1]) #just takes the popularity number and stores it in the new dictionary
            numLines += 1   

        #This is the dictionary which is later passed into a csv file for the machine learning algorthm.
        tweetsDictionary = {
            "tweets": tweetNum,
            "hashtags": hashtagList,
            "emojis": emojiList,
            "nWordGram1": nWordList1,
            "nWordGram2": nWordList2,
            "nWordGram3": nWordList3,
            "nWordGram4": nWordList4,
            "nWordGram5": nWordList5,
            "popular": popularList
        }
    printToOutputFile(tweetsDictionary)
    print(f'Processed {numLines} lines.')



#This method follows along with what was explained in class, checks the 10 fold cross validation of the machine learning algorithm
#then outputs the average score for the algorithm.
def tenFoldCrossValidation(csvFile):
    

    columns = ['tweets','hashtags','emojis','nWordGram1','nWordGram2','nWordGram3','nWordGram4','nWordGram5','popular']

    pima = pd.read_csv(csvFile)
    pima.head()

    X = pima[pima.columns[0:8]] #predictor features
    y = pima.popular #class label

    #Decision Tree Classifier average score for 10 fold cross validation
    clf = DecisionTreeClassifier()
    scoresDTC = cross_val_score(clf, X, y, cv=10)
    print("The average score for the Decision Tree Classifier is : " + scoresDTC)

    clf = svm.LinearSVC
    scoresSVC = cross_val_score(clf, X, y, cv=10)
    print("The average score for the Linear Support Vector Machine is : " + scoresSVC)

    clf = SGDClassifier()
    scoresSGD = cross_val_score(clf, X, y, cv=10)
    print("The average score for Stochastic Gradient Descent is : " + scoresSGD)
    



#calls the function on the matrix created in part2 of the assignment.
tenFoldCrossValidation("tweetMatrix.csv")