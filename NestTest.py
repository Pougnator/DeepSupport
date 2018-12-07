from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from GetEmail import readmail
from answer_analyser import isFromApp
from BasicUI import UserSelectIntent
from ProcessTrainingData import AppendTrainingData
from ProcessTrainingData import PrepareData
# from rasa_nlu.converters import load_data
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
 #from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu import config
import json
import logging
from pprint import pprint
model_dir = r"C:\Python\rasa_nlu\projects\default\default"

def train (data, config_file, model_dir):
    training_data = load_data(data)
    configuration = config.load(config_file)
    trainer = Trainer(configuration)
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'perifit')

def run():
    status, mystring = isFromApp(readmail())
    if status==True:
        logging.info("Email from app")
    print("Loading interpreter...")
    interpreter = Interpreter.load(r"C:\Python\rasa_nlu\projects\default\default\perifit")
    #print(interpreter.parse(mystring))
    return interpreter.parse(mystring), mystring

def getranking(mydict):
    intent_ranking = mydict["intent_ranking"]  
    print("Intent ranking obtained: ")
    for item in intent_ranking:
        print(str(intent_ranking.index(item)) + " " + item["name"] + " confidence: " + str(item["confidence"]))
    return list(intent_ranking)
    
    
if __name__ == '__main__':
    train(r"C:\Python\rasa_nlu\data\examples\rasa\myTestData2.json", r"C:\Python\rasa_nlu\sample_configs\config_spacy.yml", model_dir)
    logging.basicConfig(level=logging.DEBUG)
    mydict, strdata = run()
    ranking = getranking(mydict)
    choice = int(UserSelectIntent())
    logging.debug(ranking)
    logging.debug(type(ranking))
    if choice == -1:
        print("You wish to enter a new category")
        strchoice = input("Tape the new category that fits to this email")
    else:
        strchoice = str(ranking.pop(choice)["name"])
    print ("You have confirmed the intent: " + strchoice)
    mylist = PrepareData(strdata, strchoice)
    AppendTrainingData(mylist)



# where model_directory points to the model folder
#model_directory = r"C:\Python\rasa_nlu\projects\default\model_20180729-224509"
#interpreter = Interpreter.load(model_directory)
#interpreter.parse(u"reademail ertert")
