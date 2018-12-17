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

    if message.channel.id == ch_agenda:
        if re.search('everyone', com):
            client.pin_message(message)
            pin_ms = await client.pins_from(client.get_channel(ch_agenda))
            send_ms ='現在の募集中セッションは'+str(len(pin_ms)-1)+'件だよ。参加してね。'
            await client.send_message(discord.Object(id = ch_general, send_ms)



    if re.match('\$\d+d\d+', com):
        dice = []
        str_list = re.findall('\d+',com)
        for s in range(0,int(str_list[0])):
            dice.append(random.randint(1,int(str_list[1])))

        dice_num = map(str, dice)
        dice_num = ','.join(dice_num)
        dice_total = str(sum(dice))

        send_ms = 'ころころ...' + '[' + dice_num + '] 合計:'+ dice_total
        await client.send_message(message.channel, send_ms)

    if re.match('\$[Gg][Mm][Ww]', com):
        gmt = ['最高のプレゼントをあなたへ…',
        '冷めた手料理',
        '真っ赤な…',
        '人里離れた山荘、開かない玄関、何も起きないはずがなく…',
        '青春は○○の味である',
        '気づいて、お願い、気づかないで']

        odai = gmt[random.randint(0,5)]

        send_ms = 'D6ころころ...' + 'あなたのGMお題は' + '[' + odai + ']' + 'に決定しました！'
        await client.send_message(message.channel, send_ms)

    if re.match('\$[Pp][Ll][Ww]', com):
        plt = ['ああなんて可愛そうなお方、私が救ってみせましょう！',
        'あなたに私の全てを捧げますっ！',
        '熱血派の高身長美形',
        '終焉の闇へと誘う、この背に在る白銀の翼...',
        'THE 主人公',
        'オ～！ワタシニホンゴ、ワカリマセ～ン',
        '自分大好き人間',
        '酒に任せて適当なこと言う奴',
        'オーバーリアクション',
        '不幸体質',
        '〇〇以外何も見えない',
        'ゴリラ',
        'SAN値が無くなる1歩前',
        'うわぁ腹の底まで真っ黒だ',
        'あなたを守ります、ありとあらゆる困難から',
        '女子力（物理）',
        '人間以外にモテる',
        '三度の飯より〇〇が好き！',
        '○○を守るのは俺の仕事',
        '二度とあんな目に合いたくない',]

        odai = plt[random.randint(0,19)]

        send_ms = 'D20ころころ...' + 'あなたのPLお題は' + '[' + odai + ']' + 'に決定しました！'
        await client.send_message(message.channel, send_ms)

#client.run("NDc4NTc2NTMyNzA5ODM0NzUz.DvY5iw.JpGGr9EunFqKx78TGymc7oHJOIA") #for test bot
client.run("NDY2NjcxMTczMjIwOTU4MjE4.Dt2KYA.EaQOTqbdWLQ01CMIhkVtQkfCSRg")
