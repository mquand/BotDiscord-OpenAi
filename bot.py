from keep_alive import keep_alive
import discord
import openai
import os
from dotenv import load_dotenv

# Mở HTTP server để Render giữ bot chạy
keep_alive()

# Load biến môi trường
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f" Bot đã đăng nhập: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ask"):
        prompt = message.content[len("!ask"):].strip()

        if not prompt:
            await message.channel.send(" Bạn chưa nhập câu hỏi sau `!ask`")
            return

        await message.channel.send("Đang trả lời...")

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # nhanh và rẻ
                messages=[
                    {"role": "system", "content": "Bạn là một trợ lý hữu ích."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7
            )
            reply = response['choices'][0]['message']['content']
            await message.channel.send(reply)

        except Exception as e:
            await message.channel.send(f" Lỗi: {e}")

client.run(DISCORD_TOKEN)
