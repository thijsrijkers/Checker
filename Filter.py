import json

wordCount = []

with open('Storage\data.json') as json_file:
    data = json.loads(json_file.read())
    list = data['WordsEntered']

    for data in list:
        wordCount.append(data['Word'])

def most_frequent(wordCount): 
    return max(set(wordCount), key = wordCount.count) 

def write_json(data, filename='Storage\BestTopic.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 

with open('Storage\BestTopic.json') as json_file: 
    data = json.load(json_file) 
      
    temp = data['BestTopic'] 
  
    y = {
            "Topic": most_frequent(wordCount)
        } 
  
    temp.append(y) 
      
write_json(data)  