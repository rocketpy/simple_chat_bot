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
