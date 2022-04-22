import os, sys
import pandas as pd
import gspread
import gspread_dataframe
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import telegram
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler

path6 = "..."  # Paste the path to your project folder 

# Set scope for authentication (Google Drive & Google Sheets) 
scope6 = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive'] 

# Authenticate using your credentials saved in JSON 
creds6 = ServiceAccountCredentials.from_json_keyfile_name(path6 + "/NAME_OF_YOUR_JSON_FILE.json", scope6)  # Paste the name of your JSON file dowloaded when enabling Google Drive API 

bot6_token = "BOT_TOKEN"   # Substitute "BOT_TOKEN" phrase with your Bot's Token. Get it when registering a new bot via BotFather on Telegram.

# Connect with Google Sheets
client6 = gspread.authorize(creds6)
my_sheet6 = client6.open("NAME_OF_YOUR_SPREADSHEET").sheet1   # Substitute "NAME_OF_YOUR_SPREADSHEET" phrase with the name of your Google Sheets file

# Get data from the sheet as DataFrame
data6 = gspread_dataframe.get_as_dataframe(my_sheet6, parse_dates=True, usecols=[0,1,2,3,4])

# My Google Sheet table has 4 columns: Date; Expenses; Category; Comments
# Format columns 
data6 = data6.astype({"Expenses" : "float64"})
data6.Date = pd.to_datetime(data6.Date)


# Handle incoming messages and offer 'types' of expenses to choose from
def enter_expenses(update, context):   
    input1 = update.message.text.split(",")   
    try:
        input1[1] = float(input1[1])
    except IndexError:
        return  
    # Buttons with predefined categories of expenses 
    buttons = [[]]
    buttons.append([])
    buttons.append([])
    buttons[0].append(telegram.InlineKeyboardButton(text='Grocery', callback_data=str(update.message.message_id) + '=' + str(update.message.date) + '=' + str(input1[1]) + '=' + 'Grocery' + '=' + str(input1[0])))
    buttons[0].append(telegram.InlineKeyboardButton(text='Transport', callback_data=str(update.message.message_id) + '=' + str(update.message.date) + '=' + str(input1[1]) + '=' + 'Transport' + '=' + str(input1[0])))
    # Feel free to add similar buttons with expense categories relevant to you. Ex.: Cafe, Household purchaces, Miscellaneous, etc.  

    keyboard = telegram.InlineKeyboardMarkup(buttons)   # Creating a keyboard
    bot6.send_message(update.message.chat_id, update.message.text, reply_markup=keyboard)

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

