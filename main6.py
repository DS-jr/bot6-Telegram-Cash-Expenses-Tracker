import os, sys
import pandas as pd
import gspread
import gspread_dataframe
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import telegram
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler

path6 = "..."  # Paste the path to your project folder 

# Set scope for authentication (Google Drive & Google Sheets):
scope6 = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive'] 

# Authenticate using your credentials saved in JSON:
creds6 = ServiceAccountCredentials.from_json_keyfile_name(path6 + "/NAME_OF_YOUR_JSON_FILE.json", scope6)  # Paste the name of your JSON file dowloaded when enabling Google Drive API 

bot6_token = "BOT_TOKEN"   # Substitute "BOT_TOKEN" phrase with your Bot's Token. Get it when registering a new bot via BotFather on Telegram.


# ... 



# Create bot object:
bot6 = telegram.Bot(token=bot6_token)

# Add handlers:
updater = Updater(bot6_token, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.all, enter_expenses))
updater.dispatcher.add_handler(CallbackQueryHandler(callback_query_handler))

# Start polling:
updater.start_polling()
updater.idle()

