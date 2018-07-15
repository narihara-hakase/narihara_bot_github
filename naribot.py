import discord

import re
import random
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message_edit(before, after):
    if before.pinned != after.pinned:
        pin_ms = await client.pins_from(client.get_channel('413611312464134144'))

        send_ms ='現在の募集中セッションは'+str(len(pin_ms)-1)+'件だよ。参加してね。'

        await client.send_message(discord.Object(id='263246089115664384'), send_ms)

@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.channel.id == '413611312464134144':
        mes = reaction.message.content
        str_list = re.findall('[０-９\d]+月[０-９\d]+日|[０-９\d]+[\/][０-９\d]+',mes)

        if str_list == []:
            send_ms = '開催日時不明'
        else:
            send_ms = str_list[0]

        await client.send_message(user , send_ms+"のセッションに参加申し込みしました")

@client.event
async def on_reaction_remove(reaction, user):
    if reaction.message.channel.id == '413611312464134144':
        mes = reaction.message.content
        str_list = re.findall('[０-９\d]+月[０-９\d]+日|[０-９\d]+[\/][０-９\d]+',mes)

        if str_list == []:
            send_ms = '開催日時不明'
        else:
            send_ms = str_list[0]

        await client.send_message(user , send_ms+"のセッションの参加を取り消しました")

@client.event
async def on_message(message):
    dice_com = message.content
    dice = []

    if re.match('\$\d+d\d+', dice_com):
        str_list = re.findall('\d+',dice_com)
        for s in range(0,int(str_list[0])):
            dice.append(random.randint(1,int(str_list[1])))

        dice_num = map(str, dice)
        dice_num = ','.join(dice_num)
        dice_total = str(sum(dice))

        send_ms = 'ころころ...' + '[' + dice_num + '] 合計:'+ dice_total
        await client.send_message(message.channel, send_ms)

client.run("NDY2NjcxMTczMjIwOTU4MjE4.Difdrw.-q95jLpQ6ClM4ZjBzX-1KDUsKVM")
