from os import environ
import aiohttp
from pyrogram import Client, filters

API_ID = environ.get('API_ID' '5615631')
API_HASH = environ.get('API_HASH' 'f65d600ff580456871cfddc086337b7a')
BOT_TOKEN = environ.get('BOT_TOKEN' '5348600801:AAFQmW63UQ63WR6RVaErtA646kH8Kelh91w')
API_KEY = environ.get('API_KEY' '97c5fa355da833d926df0fc4562e7fb62f7263a2'', '97c5fa355da833d926df0fc4562e7fb62f7263a2')

bot = Client('gplink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**𝗛𝗘𝗟𝗟𝗢🎈{message.chat.first_name}!**\n\n"
        "𝗜'𝗺 𝗚𝗣𝗹𝗶𝗻𝗸 𝗯𝗼𝘁. 𝗝𝘂𝘀𝘁 𝘀𝗲𝗻𝗱 𝗺𝗲 𝗹𝗶𝗻𝗸 𝗮𝗻𝗱 𝗴𝗲𝘁 𝗦𝗵𝗼𝗿𝘁𝗲𝗻𝗲𝗱 𝗨𝗥𝗟. \n\n 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗜𝘀 𝗠𝗮𝗱𝗲 𝗕𝘆 @CyberBoyAyush💖")


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(f'Here is your👉 [Short Link🎈]({short_link})', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://gplinks.in/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


bot.run()
