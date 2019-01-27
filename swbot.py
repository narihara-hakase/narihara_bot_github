import random
import re

class Swstat:
    def __init__(self):#インスタンス変数管理
        pass

    #クラス変数管理（こっちはプライベート変数推奨だよ）
    __STAT_LABEL = ['器用：','敏捷：','筋力：','生命：','知力：','精神：']

#データ構造メモ　[[Name], [Number of Dice to rolled], [Number of Correction value]]
    __HIM_STAT = [["人間"],[2,2,2,2,2,2,],[0,0,0,0,0,0]]
    __ELF_STAT = [["エルフ"],[2,2,1,2,2,2],[0,0,0,0,0,0]]
    __DWR_STAT = [["ドワーフ"],[2,1,2,2,1,2],[6,0,0,0,0,6]]
    __TAB_STAT = [["タビット"],[1,1,1,2,2,2],[0,0,0,0,6,0]]
    __RUN_STAT = [["ルーンフォーク"],[2,1,2,2,2,1],[0,0,0,0,0,0]]
    __NIG_STAT = [["ナイトメア"],[2,2,1,1,2,2],[0,0,0,0,0,0]]
    __RIK_STAT = [["リカント"],[1,1,2,2,1,1],[0,3,0,0,6,0]]
    __LIL_STAT = [["リルドラケン"],[1,2,2,2,1,2],[0,0,0,6,0,0]]
    __GRA_STAT = [["グラスランナー"],[2,2,1,2,1,2],[0,0,0,6,0,6]]
    __MEL_STAT = [["メリア"],[1,1,1,2,1,1],[0,0,0,6,0,0]]

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
        race_cmd = re.findall('[0-9]|[1-9][0-9]',com)
        race_num = int(race_cmd[0])
        #配列[race_num][0]処理
        if  race_num < len(self.__RACE_STAT):


            stat_data =[] #データ構造構築
            #3回ふります
            for i in range(3):
                #配列[race_num][1]処理
                stat_tmpary = []
                for dice in self.__RACE_STAT[race_num][1]: #ダイス指定個数を振ります
                    stat_tmp = 0
                    for roll in range(dice):
                        stat_tmp += random.randint(1,6)
                    stat_tmpary.append(stat_tmp) #ここでステータス1次元配列構築

            #配列[race_num][2]処理
                for cnt,C_value in enumerate(self.__RACE_STAT[race_num][2]):#配列と同時にカウンタを取得してます
                    stat_tmpary[cnt] += C_value
                stat_data.append(stat_tmpary) #ここで2次元配列にして結果保存

            #データ文字列生成
            header = '種族：' + self.__RACE_STAT[race_num][0] + '\r\n'

            stat_str=[]
            for i in range(3):
                for cnt,label in enumerate( self.__STAT_LABEL ):
                    stat_str += label + str(stat_data[i][cnt]) + ','
                stat_str += '\r\n'

            send_ms = header + stat_str

        else:
              send_ms = '\$helpを参照し、正しい数値を入力してください'

        return send_ms
