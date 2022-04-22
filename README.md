# bot6-Telegram-Cash-Expenses-Tracker
A bot for saving my cash expenses to a budget table. <br>

<h2>How to use the bot:</h2>
<ul>
  <li>Enter manually (in the bot interface) your expense description and price, separated with a comma. Ex.: 'Bananas, 2'.</li>
  <li>Select a predefined category of your expense: press one of the appeared buttons. Ex.: 'Grocery' button.</li>
  <li>The bot saves your input as a new row in the budget table (Google Sheets).</li>
</ul>

<h2>Create a new Telegram bot:</h2>
<ul>
  <li>Intall <a href="https://telegram.org/">Telegram</a> (if you don't have it yet) & open it.</li>
  <li>Register your new Bot with Telegram's official tool - <a href="https://telegram.me/BotFather">BotFather.</a></li>
  <li>Follow <a href="https://telegram.me/BotFather">BotFather's</a> instructions, get a Token (keep it safe) to access Telegram API.</li>  
</ul>

<h2>Access Google Sheets API:</h2>
<ul>
  <li>Create a new spreadsheet via <a href="https://www.google.com/sheets/about/">Google Sheets</a> (a Google account is necessary).</li>
  <li>Open <a href="http://console.cloud.google.com/">Google Cloud Console</a> and create a new project.</li>
  <li>Enable <a href="https://console.cloud.google.com/apis/library/drive.googleapis.com">Google Drive API</a>.  Set ‘web server access’, to read ‘application data’. Download your credentials (keep safe!) in JSON format to your project folder.</li>
  <li>Enable <a href="http://console.cloud.google.com/apis/library/sheets.googleapis.com">Google Sheets API</a>.</li> 
  <li>Install libraries:</li>
  <code>pip3 install gspread</code><br>
  <code>pip3 install gspread-dataframe</code><br>
  <code>pip3 install oauth2client</code><br>
  <li>Open your JSON file, copy “client_email” email address from it.</li>
  <li>In your Google Sheets spreadsheet press “Share" (big green button in the right top) & paste that email address to add it as “editor”.</li>
</ul>

<h2>Makeadjustments:</h2>
<ul>
  <li>Make substitutions in the code of <a href="https://github.com/DS-jr/bot6-Telegram-Cash-Expenses-Tracker/blob/main/main6.py">main6.py</a> file: "/PATH"; "/NAME_OF_YOUR_JSON_FILE.json"; "BOT_TOKEN"; "NAME_OF_YOUR_SPREADSHEET".</li>
  <li>In Google Sheets table: give manually names to columns according to your needs (I used 4 columns: Date; Expenses; Category; Comments).</li>
  <li>Confirm the columns in Google Sheets table match with the code in <a href="https://github.com/DS-jr/bot6-Telegram-Cash-Expenses-Tracker/blob/main/main6.py">main6.py</a> file (quantity, order, names, content type).</li>
  <li>Run <a href="https://github.com/DS-jr/bot6-Telegram-Cash-Expenses-Tracker/blob/main/main6.py">main6.py</a> program & start using the bot.</li>
</ul>

