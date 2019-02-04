import discord

import re
import random
import swbot as SW
import accesslog

ch_agenda= '413611312464134144'
ch_general= '263246089115664384'
ch_test= '523395238484508672'
ch_bot= '468147038412865536'

if __name__ == '__main__':

    sw = SW.Swstat()
    Alog = accesslog.accesslog()

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
    async def on_voice_state_update(before, after):#memberを返す
        Alog.add_member_list(after)
        if( Alog.is_update_time() ):
            send_ms = Alog.print_logs_str()
            await client.send_message(discord.Object(id=ch_bot), send_ms)

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
        if re.match('\$help', com):
            help_ms =['``` ',
            '$[整数]d[整数] ダイスコードに従いダイスをふる',
            '$s[整数]d[整数] ダイスを降った後整列させ、期待値を表示する。',
            '$logs VCアクセスログおよびサーバータイムを表示する。',
            "$sw_ab アビス強化表を振ります",
            '$sw_ca[無しor整数] 整数の数だけ経歴表を振ります',
            '$sw_re 冒険に出た理由表を振ります',
             "$sw_[整数] 種族の初期値を3回生成する",
             "  人間：0,エルフ：1,ドワーフ：2,タビット：3",
             "  ルーンフォーク：4,ナイトメア：5,リカント：6,",
             "  リルドラケン：7,グラスランナー：8,メリア：9,",
             "　ティエンス：10,レプラカーン：11",
             '``` ']

            await client.send_message(message.channel, '\n'.join(help_ms))

        elif re.match('\$\d+d\d+', com):
            dice = []
            dice_cmd_list = re.findall('\d+',com)
            dice_cmd_list = [int(dice_cmd_list[0]),int(dice_cmd_list[1])] #int化してます

            for s in range(0,dice_cmd_list[0]):
                dice.append(random.randint(1,dice_cmd_list[1]))

            dice_num = map(str, dice)
            dice_num = ','.join(dice_num)
            dice_total = str(sum(dice))

            send_ms = 'ころころ...' + '[' + dice_num + '] 合計:'+ dice_total
            await client.send_message(message.channel, send_ms)

        elif re.match('\$[sS]\d+d\d+', com):
            dice = []
            dice_cmd_list = re.findall('\d+',com)
            dice_cmd_list = [int(dice_cmd_list[0]),int(dice_cmd_list[1])] #int化してます

            for s in range(0,dice_cmd_list[0]):
                dice.append(random.randint(1,dice_cmd_list[1]))
            dice.sort()

            dice_mean = str(((dice_cmd_list[1]+1))/2 *dice_cmd_list[0])

            dice_num = map(str, dice)
            dice_num = ','.join(dice_num)
            dice_total = str(sum(dice))

            send_ms = 'ころころ...' + '[' + dice_num + '] 合計:'+ dice_total + ' 期待値:' + dice_mean
            await client.send_message(message.channel, send_ms)

        elif re.match('\$sw_\d+', com):
            send_ms = sw.roll_stat_str(com)
            await client.send_message(message.channel, send_ms)

        elif re.match('\$sw_ab', com):
            send_ms = sw.roll_abyss_str()
            await client.send_message(message.channel, send_ms)

        elif re.match('\$sw_ca\d*', com):
            send_ms = sw.roll_Career_str(com)
            await client.send_message(message.channel, send_ms)

        elif re.match('\$sw_re', com):
            send_ms = sw.roll_reason_str()
            await client.send_message(message.channel, send_ms)

        elif re.match('\$logs', com):
            send_ms = Alog.debug_print_str()
            await client.send_message(message.channel, send_ms)

    #client.run("NDc4NTc2NTMyNzA5ODM0NzUz.DvY5iw.JpGGr9EunFqKx78TGymc7oHJOIA") #for test bot
    client.run("NDY2NjcxMTczMjIwOTU4MjE4.DxZ7Pg.r22zfpPlCjAzM5GaBarvrZjgz2w")
