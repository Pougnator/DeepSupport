import json
from pprint import pprint

#name = input("Enter a name: ")
#print(name)
read_file_path = r"C:\Python\rasa_nlu\data\examples\rasa\myTestData.json"
write_file_path = r"C:\Python\rasa_nlu\data\examples\rasa\myTestData2.json"
myfile = open(read_file_path,'r', encoding='utf-8-sig', errors='ignore')
strmyfile = myfile.read()
myfile.close()

mydata = json.loads(strmyfile, encoding='utf-8-sig')
mylist =mydata['rasa_nlu_data']['common_examples']
alist = {'text': 'yo', 'intent': 'greet', 'entities': []}
mylist.append(alist)
mydata['rasa_nlu_data']['common_examples'] = mylist
myfile = open(write_file_path,'w', encoding='utf-8-sig', errors='ignore')
json.dump(mydata, myfile, ensure_ascii=True)
myfile.close()
