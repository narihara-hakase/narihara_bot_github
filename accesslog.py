import discord
import re
import datetime

class accesslog:
        def __init__(self):#インスタンス変数管理
            today = datetime.date.today().day
            unique_member_list = []


        def add_member_list(self,member_tmp):
            if(member_tmp.voice.is_afk = false  and  self.unique_member_list.count(member_tmp.name) == 0):
                self.unique_member_list.append(member_tmp.name)

        def is_update_time(self):
            return true

        def print_logs_str(self):
            headder = "本日のアクセス人数は[" + str( len(self.unique_member_list) ) + "]人でした。\r\n"
            member_table = "\r\n".join(self.unique_member_list)
            send_ms = header + member_table
            return send_ms
