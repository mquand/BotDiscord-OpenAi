import discord
import openai
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Quan trọng: Cho phép đọc nội dung tin nhắn

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f" Bot đã đăng nhập với tên: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ask"):
        prompt = message.content[len("!ask"):].strip()
        if not prompt:
            await message.channel.send(" Hãy nhập câu hỏi sau `!ask`")
            return

        await message.channel.send(" Đang suy nghĩ...")

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  
                messages=[
                    {"role": "system", "content": "Bạn là một trợ lý hữu ích."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=1000,
                temperature=0.7,
            )

            reply = response['choices'][0]['message']['content']
            await message.channel.send(reply)

        except Exception as e:
            await message.channel.send(f" Lỗi: {str(e)}")

client.run(DISCORD_TOKEN)
