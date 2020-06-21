from telegram.ext import Updater, CommandHandler

### SETTINGS ###

# Telegram token for your bot provided by the Bot Father
TELEGRAM_TOKEN = "---insert your api key here---"
# Telegram ID of your personal account (not the bot account)
OWNER_ID = 0

### FUNCTIONS ###

def get_ip_address():
    import socket    
    hostname = socket.gethostname()    
    ip_address = socket.gethostbyname(hostname)
    return str(ip_address)

def start(update, context):
    id = update.message.from_user.id
    print(f"Bot received /start command from {id}")
    ip = get_ip_address()
    if id == OWNER_ID:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"I am your Raspberry PI. My IP address is {ip}. Your ID is {id}.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your ID is {id}")

### MAIN ###

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
start_handler = CommandHandler('start', start)
hello_handler = CommandHandler('hello', start)
updater.dispatcher.add_handler(start_handler)
updater.start_polling() # Start the bot (non-blocking)
if OWNER_ID > 0:
    print("Telegram bot is running... Sending a message to my owner.")
    ip = get_ip_address()
    updater.bot.send_message(chat_id=OWNER_ID, text=f"Raspberry Pi has started. My IP address is {ip}")
else:
    print("Telegram bot is running... Send a Telegram /start command to initiate.")
# Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT.
updater.idle()
