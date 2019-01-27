import random

class Swstat:
    self.STAT_LABEL = ['器用：','敏捷：','筋力：','生命：','知力：','精神：']

    self.HIM_STAT = ["人間",2,0,2,0,2,0,2,0,2,0,2,0]
    self.ELF_STAT = ["エルフ",2,0,2,0,1,0,2,0,2,0,2,0]
    self.DWR_STAT = ["ドワーフ",2,6,1,0,2,0,2,0,1,0,2,6]
    self.TAB_STAT = ["タビット",1,0,1,0,1,0,2,0,2,6,2,0]
    self.RUN_STAT = ["ルーンフォーク",2,0,1,0,2,0,2,0,2,0,1,0]
    self.NIG_STAT = ["ナイトメア",2,0,2,0,1,0,1,0,2,0,2,0]
    self.RIK_STAT = ["リカント",1,0,1,3,2,0,2,0,1,6,1,0]
    self.LIL_STAT = ["リルドラケン",1,0,2,0,2,0,2,6,1,0,2,0]
    self.GRA_STAT = ["グラスランナー",2,0,2,0,1,0,2,6,1,0,2,6]
    self.MEL_STAT = ["メリア",1,0,1,0,1,0,2,6,1,0,1,0]

    self.RACE_STAT =[
      self.BHIM_STAT,
      self.ELF_STAT,
      self.DWR_STAT,
      self.TAB_STAT,
      self.RUN_STAT,
      self.NIG_STAT,
      self.RIK_STAT,
      self.LIL_STAT,
      self.GRA_STAT,
      self.MEL_STAT,
    ]

    def roll_stat_str(com)
        race_cmd = re.findall('\d+',com)
        if int(race_cmd[0]) < len(self.RACE_STAT):
            race_stat = self.RACE_STAT[int(race_cmd[0])]
            send_ms = '種族：' + race_stat[0] + '\r\n'
            for j in range(3):
              for i in range(6):
              min  = race_stat[1 + 2 * i] * 1 + race_stat[2 + 2 * i]
              max = race_stat[1 + 2 * i] * 6 + race_stat[2 + 2 * i]
              stat_tmp = random.randint(min,max)
              send_ms  += self.STAT_LABEL[i]
              send_ms  += str(stat_tmp)
              if i != (len(race_stat) - 1)/2 - 1:
                send_ms +=', '
              else:
                send_ms +='\r\n'
        else:
              send_ms = '\$helpを参照し、正しい数値を入力してください'

    return send_ms
