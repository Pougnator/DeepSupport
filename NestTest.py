from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from GetEmail import readmail
from BasicUI import UserSelectIntent
# from rasa_nlu.converters import load_data
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
 #from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu import config
import json
from pprint import pprint


def train (data, config_file, model_dir):
    training_data = load_data(data)
    configuration = config.load(config_file)
    trainer = Trainer(configuration)
    trainer.train(training_data)
    model_directory = trainer.persist(trainer.persist(r"C:\Python\rasa_nlu\projects\default\default"))

def run():
    mystring = readmail()
    print("Loading interpreter...")
    interpreter = Interpreter.load(r"C:\Python\rasa_nlu\projects\default\default\model_20180819-203551")
    #print(interpreter.parse(mystring))
    return interpreter.parse(mystring)

def getranking(mydict):
    intent_ranking = mydict["intent_ranking"]  
    print("Intent ranking obtained: ")
    #i=0
    for item in intent_ranking:
        print(str(intent_ranking.index(item)) + " " + item["name"])
        #i = i+1
    return list(intent_ranking)

    
if __name__ == '__main__':
   # train(r"C:\Python\rasa_nlu\data\examples\rasa\myTestData2.json", r"C:\Python\rasa_nlu\sample_configs\config_spacy.yml", './models/nlu')
    mydict = run()
    ranking = getranking(mydict)
    choice = int(UserSelectIntent())
    print(ranking)
    print(type(ranking))
    print ("You have confirmed the intent: " + str(ranking.pop(choice)["name"]))




# where model_directory points to the model folder
#model_directory = r"C:\Python\rasa_nlu\projects\default\model_20180729-224509"
#interpreter = Interpreter.load(model_directory)
#interpreter.parse(u"reademail ertert")
