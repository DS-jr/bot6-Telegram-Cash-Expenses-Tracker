# bot6-Telegram-Cash-Expenses-Tracker
I'm currently building a bot for tracking my cash expenses. <br>
Will publish the code here in the second half of April 2022. 

<h2>How to use the bot:</h2>
<ul>
  <li>Enter manually in the bot interface your expense description and price, separated with a comma. Ex.: 'Bananas, 2'.</li>
  <li>Select a predefined category of your expense: press one of the appeared buttons. Ex.: 'Grocery' button.</li>
  <li>The bot saves your input as a new row in the budget table (Google Sheet).</li>
</ul>

<h2>Create a new Telegram bot:</h2>
<ul>
  <li>Intall <a href="https://telegram.org/">Telegram</a> (if you don't have it yet) & open it.</li>
  <li>Register your new Bot with Telegram's official tool - <a href="https://telegram.me/BotFather">BotFather.</a></li>
  <li>Follow <a href="https://telegram.me/BotFather">BotFather's</a> instructions, get a Token (keep it safe) to access Telegram API.</li>  
</ul>

<h2>Access Google Sheets API:</h2>
<ul>
  <li>Create a new spreadsheet via <a href="https://www.google.com/sheets/about/">Google Sheets</a> (a Google account is necessary). Fill in some data in the cells.</li>
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

<li>In Google Sheets table: give manually names to columns according to your needs. Ex.: Date; Expenses; Category; Comments </li>
<li>Make necessary substitutions in the code of <a href="https://github.com/DS-jr/bot6-Telegram-Cash-Expenses-Tracker/blob/main/main6.py">main6.py</a> file Ex.: "/PATH"; "/NAME_OF_YOUR_JSON_FILE.json"; "BOT_TOKEN"; "NAME_OF_YOUR_SPREADSHEET"</li>
<li>Run <a href="https://github.com/DS-jr/bot6-Telegram-Cash-Expenses-Tracker/blob/main/main6.py">main6.py</a> program & start using the bot</li>

