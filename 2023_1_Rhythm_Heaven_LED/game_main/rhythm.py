import time
from concurrent.futures import ThreadPoolExecutor
from playsound import playsound
import random

# 定数
SLOW_BPM = 117.0 + 0.3 - 0.2 # here
QUICK_BPM = 143.0 * 2 - 70 - 1 - 0.5 # here
SLOW_INTRO = 8.4 - 0.03 - 0.01 # here
QUICK_INTRO = 7.2 # here

# モード選択入力
def choose_mode():
    mode = 0
    while mode == 0:
        mode = int(input("choose mode : "))
    return mode

# 入力時間がどの判定に属するか決定する
def checkInput(inputTime, tempo, mode, inputColor, randomColorList):
    # 正しい入力時間
    correct_list = music_trans(tempo, mode, "end")
    # print(inputTime) # debug 入力時間, コメントアウトするとEnter２回必要な時がある、here
    # print(correct_list) # debug       here
    
    judge = "None" # 判定

    for cl, rcl in zip(correct_list, randomColorList):
        if cl - 0.1 <= inputTime and inputTime <= cl + 0.1 and inputColor == rcl:
            judge = "perfect"
            break
        elif cl - 0.2 <= inputTime and inputTime <= cl + 0.2 and inputColor == rcl:
            judge = "good"
            break

    if judge == "None":
        judge = "bad"
    print(judge)
    return judge

# 常に動かす入力受付関数
def input_switch_brue(mode, randomColorList):
    if mode == 1 or mode == 2:
        bpm = SLOW_BPM
    else:
        bpm = QUICK_BPM

    bps = bpm / 60
    tempo = 1 / bps  #  1拍子の間隔

    if mode == 1 or mode == 2:
        introTime = SLOW_INTRO
    else:
        introTime = QUICK_INTRO

    startTime = time.time()
    judge_dict = {"perfect" : 0, "good" : 0, "bad" : 0} # 判定のリスト
    print("Brue  : Press Enter") # Enterボタンでタイミングを取る
    print("White : Press Enter + Space")
    # 音楽の小節数
    if mode == 1 or mode == 2:
        music_len = 150
    else:
        music_len = 218

    # 音楽の終了まで回し続ける
    # inputを待たないといけないので最後のinputで関数が終わるように調整する
    while time.time() - startTime < music_len * tempo + introTime:
        # この中で入力の判定を実行できるのでは？
        # 正しい入力のリストを作ってinputTimeとのズレをだせる
        inputStr = input()
        inputTime = time.time() - startTime
        #　ただのEnterはBrue
        if inputStr == "":
            color = "Brue"
            print("3 input Brue", end=" ") # 入力した３のリズム
        #  SpaceからのEnterはWhite
        else:
            color = "White"
            print("3 input White", end=" ")
        judge_dict[checkInput(inputTime, tempo, mode, color, randomColorList)] += 1

    totalRhythm = 0 # 全部で何回あるか
    for i in judge_dict.values():
        totalRhythm += i
    # 全体数に満たないときは、叩いてない分をbadにする
    if mode == 1 or mode == 2:
        if totalRhythm < 29:
            judge_dict["bad"] += 29 - totalRhythm
            totalRhythm = 29
    else:
        if totalRhythm < 40:
            judge_dict["bad"] += 40 - totalRhythm
            totalRhythm = 40

    # 終了時のスコア集計
    maxScore = totalRhythm * 2 # 全部Perfectのときのスコア
    score = judge_dict["perfect"] * 2 + judge_dict["good"] # ゲットした最終スコア
    level = int(10 * score / maxScore) # 最後に７セグへ表示するノリ感レベル
    
    # 結果の表示
    print()
    print("perfect : " + str(judge_dict["perfect"]))
    print("good    : " + str(judge_dict["good"]))
    print("bad     : " + str(judge_dict["bad"]))
    print(f"your score : {score} / {maxScore}")

    return level

# 三連符のリズム、引数は間隔、色
def rhythm3(t_bitween, color):
    print(1, color)
    time.sleep(t_bitween)
    print(2,color)
    time.sleep(t_bitween)
    # print(3, color, "wrong") # ３連符の最後の３とその秒数 # debug 後で消す

# 早い三連符
def quick(color, tempo):
    rhythm3(tempo / 2, color)

# 普通の三連符
def normal(color, tempo):
    rhythm3(tempo, color)

# 遅い三連符
def slow(color, tempo):
    rhythm3(tempo * 2, color)

# ちょっと遅い三連符
def half_slow(color, tempo):
    rhythm3(tempo * 1.5, color)

# かなり早い三連符
def very_quick(color, tempo):
    rhythm3(tempo / 4, color)

# 楽譜をリストに変換, startとendの秒数を返す
def music_trans(tempo, mode, option):
    s = 0 # slow
    n = 1 # normal
    q = 2 # quick
    h = 3 # half_slow
    v = 4 # very_quick
    # (開始時間, 三連符の速さ)の楽譜、変換前
    if mode == 1 or mode == 2:
        music_list_startBefore_speed = [(0, s), (9, n), (17, n), (20.5, q), (25, n), (30, q), (33, n), (38.5, q), (41, n), (46, q), (49, n), (52.5, q), (57, s), 
                    (65, s), (72.5, n), (76.5, n), (81.5, n), (85.5, n), (88.5, q), (93, s), (101, n), (106.5, q), (109, s), (117, n), (122, q), (127, s), 
                    (135, s), (143, s), (152.5, q)] 
    else:
        music_list_startBefore_speed = [(0, s), (9, n), (13, n), (17, n), (21, n), (25, n), (29, n), (36, n), (41, n), (45, n), (49, n), (53, n), (57, n), (61, n), 
                    (68, n), (76, n), (84, n), (92, n), (100, n), (109, h), (117, h), (129, h), (137, h), (145, n), (149, n), (153, n), (157, n), (161, n), (165, n),
                    (172, n), (177, n), (181, n), (185, n), (189, n), (193, n), (197, n), (203.5, v), (209, n), (213, n), (220, n)] 

    if mode == 1 or mode == 2:
        introTime = SLOW_INTRO
    else:
        introTime = QUICK_INTRO
    
    music_list_start_speed = []
    for startRhythm, speed in music_list_startBefore_speed:
        startRhythm = startRhythm * tempo + introTime 
        music_list_start_speed.append((startRhythm, speed))
    
    # optionがstartならこの時点で終わり
    if option == "start":
        return music_list_start_speed

    # 楽譜に合わせてリズムを流す
    correct_list = []
    for startRhythm, speed in music_list_start_speed:
        if speed == 0:
            endRhythm = startRhythm + tempo * 2 * 2
        elif speed == 1:
            endRhythm = startRhythm + tempo * 2
        elif speed == 2:
            endRhythm = startRhythm + tempo
        elif speed == 3:
            endRhythm = startRhythm + tempo * 3
        elif speed == 4:
            endRhythm = startRhythm + tempo / 2
        correct_list.append(endRhythm)

    if option == "end":
        return correct_list

# musicスタート 
def play_music(mode, randomColorList):
    if mode == 1 or mode == 3:
        color = "Brue"
    if mode == 1 or mode == 2:
        bpm = SLOW_BPM + 1.9 - 1.5  # ちょっとだけ遅延がある？？
    else:
        bpm = QUICK_BPM + 2.0 # 遅延を考慮
    bps = bpm / 60
    tempo = 1 / bps  #  1拍子の間隔

    music_list_start_speed = music_trans(tempo, mode, "start")
    correct_list = music_trans(tempo, mode, "end")


    if mode == 1 or mode == 2:
        introTime = SLOW_INTRO
    else:
        introTime = QUICK_INTRO

    print(f"intro {introTime}s")
    time.sleep(introTime) # 音源のイントロ、時間が違うかも

    index = 0 # for文のインデックス
    # 楽譜に合わせてリズムを流す
    for startRhythm, speed in music_list_start_speed:
        # mode２と４のときはランダムリストから取り出す
        if mode == 2 or mode == 4:
            color = randomColorList[index]

        # リズムを流す
        if speed == 0:
            slow(color, tempo)
        elif speed == 1:
            normal(color, tempo)
        elif speed == 2:
            quick(color, tempo)
        elif speed == 3:
            half_slow(color, tempo)
        elif speed == 4:
            very_quick(color, tempo)

        # 次のリズムの始まりから現在のリズムの終わりを引いた時間分だけ待機
        time.sleep(music_list_start_speed[index + 1][0] - correct_list[index])

        index += 1


# mp3ファイルからBGMを流す
def backGroundMusic(mode):
    if mode == 1 or mode == 2:
        playsound("パチパチ三人衆.mp3")
    else:
        playsound("バリバリ三人衆.mp3")

# 正しい３のリズムを流すdebug用の関数    
# def correct_debug(mode):
    # if mode == 1 or mode == 3:
    #     bpm = SLOW_BPM
    # else:
    #     bpm = QUICK_BPM
    # bps = bpm / 60
    # tempo = 1 / bps  #  1拍子の間隔
    # correct_list = music_trans(tempo, mode, "end")
    # startTime = time.time()
    # index = 0
    # while True:
    #     nowTime = time.time() - startTime
    #     if correct_list[index] < nowTime:
    #         index += 1
    #         print(f"3 correct {correct_list[index - 1]}") # 正しい３のリズム

# 色を選ぶためのランダムリストを返す
def randList_maker(mode):
    if mode == 1 or mode == 2:
        lengthOfMusic = 29
    elif mode == 3 or mode == 4:
        lengthOfMusic = 40
    # ランダムリストを作る
    if mode == 2 or mode == 4:
        randList = []
        for i in range(lengthOfMusic):
            if random.randint(0, 1) == 0:
                randList.append("Brue")
            else:
                randList.append("White")
    # すべてBrueのリストを作る
    if mode == 1 or mode == 3:
        randList = ["Brue" for i in range(lengthOfMusic)]
    # print(f"randList = {randList}\n") # debug
    return randList

try:
    # ここからmain
    # with ThreadPoolExecutor(max_workers=2) as pool:
    #     future = pool.submit(choose_mode_input)
    #     pool.submit(choose_mode_display) # debug
    # mode = future.result()

    mode = choose_mode() # 難易度選択
    randomColorList = randList_maker(mode) # ランダムリストを作る

    # play_musicとinput_switchを並列実行
    with ThreadPoolExecutor(max_workers=4) as pool:
        future = pool.submit(input_switch_brue, mode, randomColorList)
        pool.submit(play_music, mode, randomColorList)
        pool.submit(backGroundMusic, mode)
        # pool.submit(correct_debug, mode) # debug ここをコメントアウトするとbpmのズレが少なくなる

    
    level = future.result()

    print(f"Your level is {level}")

finally:
    print("end")
    