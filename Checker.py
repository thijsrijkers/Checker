import json

input = input("Track: ")
print(f"Word tracked: {input}")

# function to add to JSON 
def write_json(data, filename='Storage\data.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      
      
with open('Storage\data.json') as json_file: 
    data = json.load(json_file) 
      
    temp = data['WordsEntered'] 
  
    y = {
            "Word": input
        } 
  
    temp.append(y) 
      
write_json(data)  