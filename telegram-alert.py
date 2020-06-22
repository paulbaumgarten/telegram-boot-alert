import time
from telegram.ext import Updater, CommandHandler

### SETTINGS ###

# Telegram token for your bot provided by the Bot Father
TELEGRAM_TOKEN = "---insert your api key here---"
# Telegram ID of your personal account (not the bot account)
OWNER_ID = 0

### FUNCTIONS ###

def get_ip_address():
    # Adapted from https://stackoverflow.com/a/30990617
    try:
        import socket    
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)) # Attempt to connect to Google DNS server
        return s.getsockname()[0]
    except:
        return False

def start(update, context):
    id = update.message.from_user.id
    print(f"Bot received /start command from {id}")
    ip = get_ip_address()
    if id == OWNER_ID:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"I am your Raspberry PI. My IP address is {ip}. Your ID is {id}.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your ID is {id}")

### MAIN ###

ip = get_ip_address()
while ip == False:
    print("Network not available... waiting 1 second...")
    time.sleep(1)
    ip = get_ip_address()

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)
updater.start_polling() # Start the bot (non-blocking)
if OWNER_ID > 0:
    print("Telegram bot is running... Sending a message to my owner.")
    updater.bot.send_message(chat_id=OWNER_ID, text=f"Raspberry Pi has started. My IP address is {ip}")
else:
    print("Telegram bot is running... Send a Telegram /start command to initiate.")
# Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT.
updater.idle()
