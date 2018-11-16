from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

 # from rasa_nlu.converters import load_data
from rasa_nlu.training_data import load_data

from rasa_nlu.config import RasaNLUModelConfig
 #from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu import config

def train (data, config_file, model_dir):
    training_data = load_data(data)
    configuration = config.load(config_file)
    trainer = Trainer(configuration)
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'chat')

def run():
    interpreter = Interpreter.load('./models/nlu/default/chat')
    print(interpreter.parse('I have a connection error'))
    #print(interpreter.parse(u'What is the reivew for the movie Die Hard?'))

if __name__ == '__main__':
    #train('./data/examples/rasa/testData.json', './sample_configs/config_spacy.yml', './models/nlu')
    run()