import json
import logging
from pprint import pprint

#name = input("Enter a name: ")
#print(name)
# This file is used to update the training data that is used by our model. 
# After the training data is updated we still have to launch the "Train" function in nlu_model_AR.py to train the model
###################################################################################################

# PrepareData creates a list in the format that can be later understood by the rasa functions
# It uses some text and an intent as parameters
def PrepareData(body, intent):
    alist = {'text': body, 'intent': intent, 'entities': []}
    return alist

# Append data opens the hardcoded test data json file, and appends the "dataList" argument into it.
# The dataList must be a correctly formated dictionnary format
# Example of format: dataList= {'text': 'cuircuir', 'intent': 'greet', 'entities': []}
def AppendTrainingData(dataList):

    read_file_path = r"C:\Python\rasa_nlu\data\examples\rasa\myTestData2.json"
    write_file_path = r"C:\Python\rasa_nlu\data\examples\rasa\myTestData2.json"
    myfile = open(read_file_path,'r', encoding='utf-8-sig', errors='ignore')
    strmyfile = myfile.read()
    myfile.close()

    mydata = json.loads(strmyfile, encoding='utf-8-sig')
    mylist =mydata['rasa_nlu_data']['common_examples']
    mylist.append(dataList)

    mydata['rasa_nlu_data']['common_examples'] = mylist
    myfile = open(write_file_path,'w', encoding='utf-8-sig', errors='ignore')
    json.dump(mydata, myfile, ensure_ascii=True)
    myfile.close()
    logging.info("Training datafile appended")

if __name__ == '__main__':
    mybody = "CuirMou"
    myintent = "Hamdou"
    data = PrepareData(mybody, myintent)
    AppendTrainingData(data)


