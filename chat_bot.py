# pip install chatterbot
# pip install chatterbot_corpus


from chatterbot import ChatBot


bot = ChatBot('BotName')

bot = ChatBot(
    'BotName',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)
