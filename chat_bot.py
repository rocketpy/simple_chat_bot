# pip install chatterbot
# pip install chatterbot_corpus


from chatterbot import ChatBot


bot = ChatBot('BotName')

#  storage adapter
bot = ChatBot('BotName',
               storage_adapter='chatterbot.storage.SQLStorageAdapter',
               database_uri='sqlite:///database.sqlite3'
              )

#  logic adapter
bot = ChatBot('BotName',  
              logic_adapters=[
              'chatterbot.logic.BestMatch',
              'chatterbot.logic.TimeLogicAdapter'],
              )

#  training the chatbot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
'Hi',
'Hello',
'I need your assistance regarding my order',
'Please, Provide me with your order id',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An order takes 3-5 Business days to get delivered.',
'Okay Thanks',
'No Problem! Have a Good Day!'
])

#  testing
response = bot.get_response('I have a ...')

print("Bot response:", response)
