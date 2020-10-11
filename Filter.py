import json

with open('Storage\data.json') as json_file:
    # convert JSON text to python dictionary
    data = json.loads(json_file.read())
    list = data['WordsEntered']
    # print data
    for data in list:
        print(data['Word'])

#[TODO] Remove this input when develop is finished
input("Press enter to exit ;)")