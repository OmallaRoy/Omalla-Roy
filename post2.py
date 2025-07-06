# Social media used(telegram")
import asyncio
from telegram import Bot

BOT_TOKEN = '7992586629:AAErgAEnfVD-wnajIqInTcXcnK1-JBUfmNs'

CHAT_ID = '@RJtradecommunity'  

message = input("Enter your Telegram message: ")

async def post_telegram_message():
    bot = Bot(token=BOT_TOKEN)
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")

asyncio.run(post_telegram_message())
