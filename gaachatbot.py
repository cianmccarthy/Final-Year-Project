# -*- coding: utf-8 -*-
"""GAAChatbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ePd9P_bwJGnd3MtphgunyiEDhna5j-zO
"""

pip install chatterbot

from chatterbot import ChatBot

bot = ChatBot('Marty')

bot = ChatBot(
    'Marty',
    storage_adapter='chatterbot.storage.SQLStorageAdapter', #connects to sql databases
    database_uri='sqlite:///database.sqlite3' #sets up a database for where the phrases in the conversation will be stored
)

bot = ChatBot(
    'Marty',
    storage_adapter='chatterbot.storage.SQLStorageAdapter', read_only = True,
    logic_adapters=[
        'chatterbot.logic.BestMatch' #selects a response based on the best known match to one of the statements
    ],
    database_uri='sqlite:///database.sqlite3'
)

#importing the CSV pack
import csv

#looping through the csv file to read each phrase and appending it to the array 'small_talk'
small_talk = []
reader = csv.reader(open("responses.csv"))
for i in reader:
  print(i[0])
  small_talk.append(i[0])

print(small_talk)

from chatterbot.trainers import ListTrainer
#setting up a variable for the list trainer method which is implemented to my chatbot
list_trainer = ListTrainer(bot)

#training the chatbot to the phrases in the 'small_talk' array
list_trainer.train(small_talk)

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break