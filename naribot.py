import discord

import re
import random
ch_agenda= '413611312464134144'
ch_general= '263246089115664384'
ch_test= '523395238484508672'

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
        pin_ms = await client.pins_from(client.get_channel(ch_agenda))
        send_ms ='現在の募集中セッションは'+str(len(pin_ms)-1)+'件だよ。参加してね。'
        await client.send_message(discord.Object(id=ch_general), send_ms)

@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.channel.id == ch_agenda:
        mes = reaction.message.content
        str_list = re.findall('[０-９\d]+月[０-９\d]+日|[０-９\d]+[\/][０-９\d]+',mes)

        if str_list == []:
            send_ms = '開催日時不明'
        else:
            send_ms = str_list[0]

        await client.send_message(user , send_ms+"のセッションに参加申し込みしました")

@client.event
async def on_reaction_remove(reaction, user):
    if reaction.message.channel.id == ch_agenda:
        mes = reaction.message.content
        str_list = re.findall('[０-９\d]+月[０-９\d]+日|[０-９\d]+[\/][０-９\d]+',mes)

        if str_list == []:
            send_ms = '開催日時不明'
        else:
            send_ms = str_list[0]

        await client.send_message(user , send_ms+"のセッションの参加を取り消しました")

@client.event
async def on_message(message):
    com = message.content

    ''' 一時的にオミット中。
        if message.channel.id == ch_agenda:
            if re.search('everyone', com):
                await client.pin_message(message)
                pin_ms = await client.pins_from(client.get_channel(ch_agenda))
                send_ms ='現在の募集中セッションは'+str(len(pin_ms)-1)+'件だよ。参加してね。'
                await client.send_message(discord.Object(id = ch_general), send_ms)
    '''

    if re.match('\$\d+d\d+', com):
        dice = []
        str_list = re.findall('\d+',com)
        for s in range(0,int(str_list[0])):
            dice.append(random.randint(1,int(str_list[1])))
        dice.sort()

        dice_mean = ((str_list[1]+1))/2 *str_list[0]

        dice_num = map(str, dice)
        dice_num = ','.join(dice_num)
        dice_total = str(sum(dice))

        send_ms = 'ころころ...' + '[' + dice_num + '] 合計:'+ dice_total + ' 期待値:' + dice_mean
        await client.send_message(message.channel, send_ms)

#client.run("NDc4NTc2NTMyNzA5ODM0NzUz.DvY5iw.JpGGr9EunFqKx78TGymc7oHJOIA") #for test bot
client.run("NDY2NjcxMTczMjIwOTU4MjE4.DvjS9g.8d5XGm7wF36AJ6MyYtWuJu3G7SA")
