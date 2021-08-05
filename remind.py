import discord
from datetime import datetime
from discord import channel
from discord.ext import tasks

TOKEN = 'ODM3OTExNzYzODEwMzg1OTYx.YIzcJA.rB7qq9kgZKBY8FWUlKRCHcDo8m8'
CHANNEL_ID = 826243369973317632

client = discord.Client()


@client.event
async def on_ready():

    print('ログイン')

# coding:UTF-8


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')


@client.event
async def on_message(message):
    await TextChannel id = 826243369973317632 name = 'rythm' position = 0 nsfw = False news = False category_id = 425854769668816898 .channel.send("ha?")

# ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
