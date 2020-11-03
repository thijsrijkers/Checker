import json
import subprocess
import os

wordCount = []
wordCountTopics = []

saveWord = []
saveWordCounter = 0

with open('Storage\data.json') as json_file:
    data = json.loads(json_file.read())
    list = data['WordsEntered']

    for data in list:
        wordCount.append(data['Word'])

with open('Storage\BestTopic.json') as json_file:
    data = json.loads(json_file.read())
    list = data['BestTopic']

    for data in list:
        wordCountTopics.append(data['Topic'])

def write_json(data, filename='Storage\BestTopic.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 

def most_frequent(wordCount): 
    return max(set(wordCount), key = wordCount.count) 

def most_frequentTopic(wordCountTopics): 
    return max(set(wordCountTopics), key = wordCountTopics.count) 
    
def secondFrequent(wordCount): 
    from collections import Counter 
  
    c = Counter(wordCount)  
       
    return(c.most_common()[1][0]) 

def printNoEdit(): 
    print('No addition to list is necessary')

def printEdit(): 
    print("List Of Topics Has Been Adjusted")

with open('Storage\BestTopic.json') as json_file: 
    data = json.load(json_file) 
      
    temp = data['BestTopic'] 
    countListWordCount = wordCount.count

    if most_frequent(wordCount) != most_frequentTopic(wordCountTopics):
        if saveWord.count == wordCount.count or most_frequent(wordCount) not in wordCountTopics:
            topicToEnter = most_frequent(wordCount)
                
            y = {      
                    "Topic": topicToEnter
                } 
                
            temp.append(y) 

            write_json(data)  
            saveWord.append(topicToEnter)
            saveWordCounter = saveWordCounter + 1
            printEdit()
        else:
            printNoEdit()
    elif secondFrequent(wordCount) != most_frequentTopic(wordCountTopics):
        if saveWord.count == wordCount.count or secondFrequent(wordCount) not in wordCountTopics:
            topicToEnter = secondFrequent(wordCount)
                
            y = {      
                    "Topic": topicToEnter
                } 
                
            temp.append(y) 

            write_json(data)  
            saveWord.append(topicToEnter)
            saveWordCounter = saveWordCounter + 1
            printEdit()
        else:
            printNoEdit()
    
    if saveWordCounter >= 5:
        print("There are new additions in the list, is recommended to make a copy or to process them")
        saveWordCounter = 0
        saveWord *= 0