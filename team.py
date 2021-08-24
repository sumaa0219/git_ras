import discord
from discord import message
from discord import client
from discord import guild
from discord.ext import commands
import asyncio
import random
from discord.member import Member
import numpy as np


TOKEN = 'ODM3OTExNzYzODEwMzg1OTYx.YIzcJA.Hg0UKWza3pgJssZLPUJlDQiMzCs'
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)
client = discord.Client()
id = 877151270669000724


people_list = []
people_list_name = []
enque = []
list_a = []
list_b = []
attack = []
defence = []
MANAKOvcid = [840232397709770762, 785385689016696833,
              836170079501811752, 790878237881532416]
summavcid = [826243369973317632, 879669692745265172,
             425854769668816904, 841632288298106890]


@bot.event
async def on_ready():

    print('セットアップ完了')


@bot.command()
async def game(ctx):

    global chid
    global Gctx
    global embed_id

    Gctx = ctx

    if ctx.channel.id == MANAKOvcid[0]:
        chid = MANAKOvcid[0]

    if ctx.channel.id == summavcid[0]:
        chid = summavcid[0]

    people_list_name.clear()  # que削除
    people_list.clear()  # que削除
    embed = discord.Embed(title="ランダムでチーム分けを行います",
                          description="参加する人はリアクションしてください\n参加する全員がリアクションしたら”.team”を実行してください")
    embed_message = await ctx.send(embed=embed)
    embed_id = embed_message.id
    for reaction in ['👍', '👌', '🥰', '🚫']:
        await embed_message.add_reaction(reaction)


@bot.command()
async def que(ctx):
    await ctx.send(people_list_name)


@bot.command()
async def team(ctx):

    global attack
    global defence
    global lis_size
    global lis_size1
    list_a.clear()
    list_b.clear()
    attack.clear()
    defence.clear()

    member = np.array(people_list)  # LISTに関して取得
    list_size = member.size  # LISTの要素数の数取得
    channel = bot.get_channel(id)

    if list_size % 2 == 0:
        point_center: int = list_size // 2

    else:
        re_list_size = list_size + 1
        point_center: int = re_list_size // 2

    point_end = list_size
    random.shuffle(people_list)

    attack = people_list[0:point_center]
    defence = people_list[point_center:point_end]

    size = np.array(defence)
    lis_size = size.size
    if lis_size % 2 == 0:
        lis_size1 = lis_size

    else:
        lis_size1 = lis_size + 1

    for i in range(lis_size1):
        men1 = bot.get_user(attack[i])
        a = men1.name
        list_a.append(a)

    for x in range(lis_size):
        men2 = bot.get_user(defence[x])
        b = men2.name
        list_b.append(b)

    embed = discord.Embed(title="チームを発表します",
                          description="")
    embed.add_field(name="Aチーム", value=(list_a))
    embed.add_field(name="Bチーム", value=(list_b))
    embed_message = await ctx.send(embed=embed)


@bot.command()
async def start(ctx):

    global MANAKOvcid
    global summavcid
    global vc0

    attack_member = np.array(people_list)  # LISTに関して取得
    attack_size = attack_member.size

    if ctx.channel.id == MANAKOvcid[0]:  # ここに分岐を追加
        vc0 = bot.get_channel(MANAKOvcid[1])
        vc1 = bot.get_channel(MANAKOvcid[2])
        vc2 = bot.get_channel(MANAKOvcid[3])

    if ctx.channel.id == summavcid[0]:  # ここに分岐を追加
        vc0 = bot.get_channel(summavcid[1])
        vc1 = bot.get_channel(summavcid[2])
        vc2 = bot.get_channel(summavcid[3])

    for i in range(lis_size1):
        memid1 = ctx.guild.get_member(attack[i])
        await memid1.move_to(vc1)

    for x in range(lis_size):
        memid2 = ctx.guild.get_member(defence[x])
        await memid2.move_to(vc2)


@bot.command()
async def end(ctx):
    all_member = np.array(people_list)  # LISTに関して取得
    all_size = all_member.size

    for x in range(all_size):
        menall = ctx.guild.get_member(people_list[x])
        await menall.move_to(vc0)


@ bot.event
async def on_reaction_add(reaction, user):

    global people_list
    global people_list_name
    global list_size
    global channel

    channel = bot.get_channel(id)  # 管理チャット取得
    ctx = bot.get_channel(chid)
    people_voice = user.voice
    people_id = user.id  # リアクションユーザーID取得
    people_neme = user.name  # リアクションユーザー名取得
    member = np.array(people_list)  # LISTに関して取得
    list_size = member.size  # LISTの要素数の数取得

    if reaction.message.id == embed_id:

        if reaction.emoji == '👍':

            if people_id in people_list:
                await channel.send(people_neme)
                await channel.send("現在の人数" + str(list_size) + "人")

            else:
                if people_id == 837911763810385961:
                    await channel.send("これはBOTです")

                else:
                    people_list.append(people_id)
                    people_list_name.append(people_neme)
                    await channel.send("現在の人数" + str(list_size) + "人")

        if reaction.emoji == "👌":
            if people_id == 837911763810385961:
                await channel.send("これはBOTです")

            else:
                global attack
                global defence
                global lis_size
                global lis_size1
                list_a.clear()
                list_b.clear()
                attack.clear()
                defence.clear()

                member = np.array(people_list)  # LISTに関して取得
                list_size = member.size  # LISTの要素数の数取得
                channel = bot.get_channel(id)

                if list_size % 2 == 0:
                    point_center: int = list_size // 2

                else:
                    re_list_size = list_size + 1
                    point_center: int = re_list_size // 2

                point_end = list_size
                random.shuffle(people_list)

                attack = people_list[0:point_center]
                defence = people_list[point_center:point_end]

                size = np.array(defence)
                lis_size = size.size
                if lis_size % 2 == 0:
                    lis_size1 = lis_size

                else:
                    lis_size1 = lis_size + 1

                for i in range(lis_size1):
                    men1 = bot.get_user(attack[i])
                    a = men1.name
                    list_a.append(a)

                for x in range(lis_size):
                    men2 = bot.get_user(defence[x])
                    b = men2.name
                    list_b.append(b)

                embed = discord.Embed(title="チームを発表します",
                                      description="")
                embed.add_field(name="Aチーム", value=(list_a))
                embed.add_field(name="Bチーム", value=(list_b))
                embed_message = await ctx.send(embed=embed)

        if reaction.emoji == "🥰":
            if people_id == 837911763810385961:
                await channel.send("これはBOTです")

            else:
                global MANAKOvcid
                global summavcid
                global vc0

                attack_member = np.array(people_list)  # LISTに関して取得
                attack_size = attack_member.size

                if Gctx.channel.id == MANAKOvcid[0]:  # ここに分岐を追加
                    vc0 = bot.get_channel(MANAKOvcid[1])
                    vc1 = bot.get_channel(MANAKOvcid[2])
                    vc2 = bot.get_channel(MANAKOvcid[3])

                if Gctx.channel.id == summavcid[0]:  # ここに分岐を追加
                    vc0 = bot.get_channel(summavcid[1])
                    vc1 = bot.get_channel(summavcid[2])
                    vc2 = bot.get_channel(summavcid[3])

                for i in range(lis_size1):
                    memid1 = Gctx.guild.get_member(attack[i])
                    await memid1.move_to(vc1)

                for x in range(lis_size):
                    memid2 = Gctx.guild.get_member(defence[x])
                    await memid2.move_to(vc2)

        if reaction.emoji == '🚫':
            if people_id == 837911763810385961:
                await channel.send("これはBOTです")

            else:
                all_member = np.array(people_list)  # LISTに関して取得
                all_size = all_member.size

                for x in range(all_size):
                    menall = Gctx.guild.get_member(people_list[x])
                    await menall.move_to(vc0)

    else:
        print("errer")

bot.run(TOKEN)
