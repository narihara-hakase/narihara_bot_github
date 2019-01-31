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

    #[Column][row]
    __abyss_data = [
    [ '1-1' , '「自傷の」' , '…装備時' , 'この武具を装備中に装備者がクリティカルを発生させた時、装備者のHPが5点減少する。' ],
    [ '1-2' , '「嘆きの」' , '…装備時' , '近くに敵が居たり、長い緊張状態が続くと涙が止まらなくなる。戦闘中なら「射程：術者（自身）」「射程：接触」以外の効果で対象を選べなくなる。' ],
    [ '1-3' , '「優しき」' , '…装備時' , '敵に同情してしまう。敵対するキャラクターを対象とする場合、対象のHPが1点以上減少しているなら命中力判定、魔法行使判定に-2のペナルティ修正を受ける。' ],
    [ '1-4' , '「差別の」' , '…装備時' , '特定の分類に対して与える物理ダメージ・魔法ダメージが2点減少する。分類は「分類決定表」で無作為に決定する。' ],
    [ '1-5' , '「脆弱な」' , '…装備時' , '魔法ダメージを受けるたび、そのダメージが+1点される。' ],
    [ '1-6' , '「無謀な」' , '…装備時' , '防護点が2点減少する（最低0）。' ],
    [ '2-1' , '「重い」' , '…装備時' , '強化した武具の必要筋力が+2点される。威力、防護点などは変化なし。' ],
    [ '2-2' , '「難しい」' , '…装備時' , 'いかなる威力表使用時でも、③④欄の数値が威力に関係なく「0」になる（自動失敗ではない）。' ],
    [ '2-3' , '「軟弱な」' , '…装備時' , '精神抵抗力判定に-1のペナルティ修正を受ける。' ],
    [ '2-4' , '「病弱な」' , '…装備時' , '生命抵抗力判定に-1のペナルティ修正を受ける。' ],
    [ '2-5' , '「過激な」' , '…装備時' , '特定の属性から受ける物理ダメージ、魔法ダメージが2点上昇する。属性は「属性決定表」で無作為に決定する。' ],
    [ '2-6' , '「陽気な」' , '…装備時' , '精神抵抗力判定に失敗するたび、笑いが止まらなくなる。次の手番終了時まで行動判定（『Ⅰ』123頁）に-1のペナルティ修正を受ける。この効果は累積する。' ],
    [ '3-1' , '「たどたどしい」' , '…装備時' , '話をするときに言葉に詰まったり、言い間違えたりしやすくなる。魔法行為判定に-1のペナルティ修正を受ける。' ],
    [ '3-2' , '「代弁する」' , '…装備時' , '自身の会話は、そのまま武具が魔法文明語の聞き取りづらい声で話す。装備中は魔法文明語以外の言語で会話は行えず、妖精魔法、魔動機術を行使できなくなる。' ],
    [ '3-3' , '「施しは受けない」' , '…装備時' , '戦闘中、「抵抗：任意」の効果を受け入れた場合、次の手番開始時まで生命抵抗力、精神抵抗力に-2のペナルティ修正を受ける。' ],
    [ '3-4' , '「死に近い」' , '…携行時' , '常に生死判定に「冒険者レベル」と同じ値のペナルティ修正を受ける。' ],
    [ '3-5' , '「おしゃれな」' , '…携行時' , 'その武具を常に華美に飾りたくなる。収入を得るたび、その1割以上をこの武具の装飾に費やさなければならない（効果などに変化はない）。' ],
    [ '3-6' , '「マナを吸う」' , '…携行時' , '魔法や練技など、自身の意思でMPを消費する効果を使用する場合、すべてのMP消費が1点上昇する。' ],
    [ '4-1' , '「鈍重な」' , '…携行時' , '移動力が半分（端数切り上げ）になる。' ],
    [ '4-2' , '「定まらない」' , '…携行時' , '戦闘中の手番開始時に1dし、出目が「1」なら《タ―ゲッティング》とそれを前提にした戦闘特技を修得していないものとして扱う。' ],
    [ '4-3' , '「錯乱の」' , '…携行時' , '戦闘中の手番開始時に1dし、出目が「1」なら近接攻撃を含む「射程：接触」を対象に効果を使用する際、対象は同じ位置（エリア、座標）のすべてキャラクター（敵味方含む）から無作為に選ばれる。' ],
    [ '4-4' , '「足絡みの」' , '…携行時' , '戦闘中の手番開始時に1dし、出目が「1」ならその場で即座に転倒する。手番中には起き上がれない。' ],
    [ '4-5' , '「滑り落ちる」' , '…携行時' , '戦闘中の手番開始時に1dし、出目が「1」なら手に装備または保持している物をすべてその場に落とす（その手番の主動作で拾うことは可能）。' ],
    [ '4-6' , '「悪臭放つ」' , '…携行時' , '強い悪臭を放つ。所持しているだけで他キャラクターに不快感を与え、隠密判定に-2のペナルティ修正を受ける。さらに冒険者ランク（『Ⅰ』137頁）が1段階低いものとして扱われる。' ],
    [ '5-1' , '「醜悪な」' , '…携行時' , '武具の見た目が悪く、魅力がない。売却する際、基本売却価格の4分の1の価格で売却する。さらに冒険者ランク（『Ⅰ』137頁）が1段階低いものとして扱われる。' ],
    [ '5-2' , '「唸る」' , '…携行時' , 'その武具から常に羽虫が飛び交うような音が響く。隠密判定、危険感知判定に-4のペナルティ修正を受ける。' ],
    [ '5-3' , '「ふやけた」' , '…携行時' , '水を吸ったようにふやけた質感をしている。追加ダメージ-1（武器）、防護点-1（鎧、盾）。病気属性の効果に対する生命抵抗力、精神抵抗力判定に-4のペナルティ修正を受ける。' ],
    [ '5-4' , '「古傷の」' , '…携行時' , 'HPを回復する効果（休息による回復を含む）を受けた場合、その回復量が1点減少する。 ' ],
    [ '5-5' , '「まばゆい」' , '…携帯時' , '光などを弾いて強く輝く。自身は常に視界が悪いことによる-1のペナルティ修正を受ける。' ],
    [ '5-6' , '「栄光なき」' , '…携行時' , '行為判定で自動成功とは扱わず、2dを振り直し、その後の出目に従う。この効果は1日に1回のみ発揮される。' ],
    [ '6-1' , '「正直者の」' , '…携行時' , '嘘、方便がすぐにばれるようになる。真偽判定の対象となる場合、-4のペナルティ修正を受ける。 ' ],
    [ '6-2' , '「乗り物酔いの」' , '…携行時' , '揺れに弱くなる。自身の足以外の手段で10分以上移動した後、1時間、行動判定に-1のペナルティ修正を受ける。' ],
    [ '6-3' , '「碧を厭う」' , '…携行時' , '自然の中では落ち着かなくなる。自然環境（『Ⅰ』108頁）では行動判定に-1のペナルティ修正を受ける。' ],
    [ '6-4' , '「我慢できない」' , '…携行時' , 'セッション中に1日の始まりを迎えるたび、趣味や嗜好品などに「冒険者レベル×10」ガメルを出費しなければならない。趣味や嗜好品が消費できない環境であれば、翌日の朝まで最大HP、最大MPが「冒険者レベル」点減少する。' ],
    [ '6-5' , '「つきまとう」' , '…携行時' , 'この武具が気がつけば身の回りにある。この武具以外での命中力判定、魔法行使判定（武器）、回避力判定（鎧、盾）に-4のペナルティ修正を受ける。' ],
    [ '6-6' , '「のろまな」' , '…携行時' , '戦闘開始処理の「戦闘準備」をいっさい行えなくなる。']
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
            header = '種族：' + self.__RACE_STAT[race_num][0][0] + '\r\n'

            stat_str=''
            for i in range(3):
                for cnt,label in enumerate( self.__STAT_LABEL ):
                    stat_str += label + str(stat_data[i][cnt]) + ','
                stat_str += '\r\n'

            send_ms = header + stat_str

        else:
              send_ms = '\$helpを参照し、正しい数値を入力してください'

        return send_ms

    def roll_abyss_str(self):
        column = random.randint(0,35)

        header = 'アビス強化ダイス:[' + self.__abyss_data[column][0] + ']\r\n'
        a_name = 'アビスカース名称>' + self.__abyss_data[column][1] +'\r\n'
        timing = 'タイミング>' + self.__abyss_data[column][2] + '\r\n'
        effect = '効果>' + self.__abyss_data[column][3] + '\r\n'
        send_ms = header + a_name + timing + effect
        return send_ms
