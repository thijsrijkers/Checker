import json

with open('Storage\data.json') as json_file:
    data = json.load(json_file)    
    print(data["WordsEntered"])

#[TODO] Remove this input when develop is finished
input("Press enter to exit ;)")