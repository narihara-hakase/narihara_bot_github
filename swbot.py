import random
import re

class Swstat:
    def __init__(self):#インスタンス変数管理
        pass

    #クラス変数管理（こっちはプライベート変数推奨だよ）
    __STAT_LABEL = ['器用：','敏捷：','筋力：','生命：','知力：','精神：']

    __HIM_STAT = ["人間",2,0,2,0,2,0,2,0,2,0,2,0]
    __ELF_STAT = ["エルフ",2,0,2,0,1,0,2,0,2,0,2,0]
    __DWR_STAT = ["ドワーフ",2,6,1,0,2,0,2,0,1,0,2,6]
    __TAB_STAT = ["タビット",1,0,1,0,1,0,2,0,2,6,2,0]
    __RUN_STAT = ["ルーンフォーク",2,0,1,0,2,0,2,0,2,0,1,0]
    __NIG_STAT = ["ナイトメア",2,0,2,0,1,0,1,0,2,0,2,0]
    __RIK_STAT = ["リカント",1,0,1,3,2,0,2,0,1,6,1,0]
    __LIL_STAT = ["リルドラケン",1,0,2,0,2,0,2,6,1,0,2,0]
    __GRA_STAT = ["グラスランナー",2,0,2,0,1,0,2,6,1,0,2,6]
    __MEL_STAT = ["メリア",1,0,1,0,1,0,2,6,1,0,1,0]

    __RACE_STAT =[
      __HIM_STAT,
      __ELF_STAT,
      __DWR_STAT,
      __TAB_STAT,
      __RUN_STAT,
      __NIG_STAT,
      __RIK_STAT,
      __LIL_STAT,
      __GRA_STAT,
      __MEL_STAT,
    ]



    def roll_stat_str(self,com):
        race_cmd = re.findall('\d+',com)
        if int(race_cmd[0]) < len(self.__RACE_STAT):
            race_stat = self.__RACE_STAT[int(race_cmd[0])]
            send_ms = '種族：' + race_stat[0] + '\r\n'
            for j in range(3):
              for i in range(6):
                  min  = race_stat[1 + 2 * i] * 1 + race_stat[2 + 2 * i]
                  max = race_stat[1 + 2 * i] * 6 + race_stat[2 + 2 * i]
                  stat_tmp = random.randint(min,max)
                  send_ms  += self.__STAT_LABEL[i]
                  send_ms  += str(stat_tmp)
                  if i != (len(race_stat) - 1)/2 - 1:
                    send_ms +=', '
              else:
                send_ms +='\r\n'
        else:
              send_ms = '\$helpを参照し、正しい数値を入力してください'

        return send_ms
