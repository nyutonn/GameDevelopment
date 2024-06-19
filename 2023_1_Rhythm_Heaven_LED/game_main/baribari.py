import wiringpi as wp
import time
from concurrent.futures import ThreadPoolExecutor
from playsound import playsound # 使えないかも, here
import random

# 定数
SLOW_BPM = 117.0 + 0.3 - 0.2 # here
QUICK_BPM = 143.0 * 2 - 70 - 1 - 0.5 # here
SLOW_INTRO = 8.4 - 0.03 - 0.01 # here
QUICK_INTRO = 7.2 # here
CHATTERING = 0.2 # here

# 7セグ消灯
def led7_dark():
    wp.digitalWrite(pinLedA, wp.GPIO.LOW)
    wp.digitalWrite(pinLedB, wp.GPIO.LOW)
    wp.digitalWrite(pinLedC, wp.GPIO.LOW)
    wp.digitalWrite(pinLedD, wp.GPIO.LOW)
    wp.digitalWrite(pinLedE, wp.GPIO.LOW)
    wp.digitalWrite(pinLedF, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG, wp.GPIO.LOW)
    wp.digitalWrite(pinLedDP, wp.GPIO.LOW)

# 7セグに点灯, 引数は点灯させる秒数
def light_0(t):
    wp.digitalWrite(pinLedA, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedC, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedD, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedE, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedF, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG, wp.GPIO.LOW)
    wp.digitalWrite(pinLedDP, wp.GPIO.LOW)
    time.sleep(t)
    led7_dark()

def light_1(t):
    wp.digitalWrite(pinLedA, wp.GPIO.LOW)
    wp.digitalWrite(pinLedB, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedC, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedD, wp.GPIO.LOW)
    wp.digitalWrite(pinLedE, wp.GPIO.LOW)
    wp.digitalWrite(pinLedF, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG, wp.GPIO.LOW)
    wp.digitalWrite(pinLedDP, wp.GPIO.LOW)
    time.sleep(t)
    led7_dark()

def light_2(t):
    wp.digitalWrite(pinLedA, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedC, wp.GPIO.LOW)
    wp.digitalWrite(pinLedD, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedE, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedF, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedDP, wp.GPIO.LOW)
    time.sleep(t)
    led7_dark()

def light_3(t):
    wp.digitalWrite(pinLedA, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedC, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedD, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedE, wp.GPIO.LOW)
    wp.digitalWrite(pinLedF, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedDP, wp.GPIO.LOW)
    time.sleep(t)
    led7_dark()

def light_4(t):
    wp.digitalWrite(pinLedA, wp.GPIO.LOW)
    wp.digitalWrite(pinLedB, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedC, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedD, wp.GPIO.LOW)
    wp.digitalWrite(pinLedE, wp.GPIO.LOW)
    wp.digitalWrite(pinLedF, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedDP, wp.GPIO.LOW)
    time.sleep(t)
    led7_dark()

def light_5(t):
    wp.digitalWrite(pinLedA, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB, wp.GPIO.LOW)
    wp.digitalWrite(pinLedC, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedD, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedE, wp.GPIO.LOW)
    wp.digitalWrite(pinLedF, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedDP, wp.GPIO.LOW)
    time.sleep(t)
    led7_dark()

def light_6(t):
    wp.digitalWrite(pinLedA, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB, wp.GPIO.LOW)
    wp.digitalWrite(pinLedC, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedD, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedE, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedF, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedDP, wp.GPIO.LOW)
    time.sleep(t)
    led7_dark()

def light_7(t):
    wp.digitalWrite(pinLedA, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedC, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedD, wp.GPIO.LOW)
    wp.digitalWrite(pinLedE, wp.GPIO.LOW)
    wp.digitalWrite(pinLedF, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG, wp.GPIO.LOW)
    wp.digitalWrite(pinLedDP, wp.GPIO.LOW)
    time.sleep(t)
    led7_dark()

def light_8(t):
    wp.digitalWrite(pinLedA, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedC, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedD, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedE, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedF, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedDP, wp.GPIO.LOW)
    time.sleep(t)
    led7_dark()

def light_9(t):
    wp.digitalWrite(pinLedA, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedC, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedD, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedE, wp.GPIO.LOW)
    wp.digitalWrite(pinLedF, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedDP, wp.GPIO.LOW)
    time.sleep(t)
    led7_dark()

def light_10(t):
    wp.digitalWrite(pinLedA, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedC, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedD, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedE, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedF, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG, wp.GPIO.LOW)
    wp.digitalWrite(pinLedDP, wp.GPIO.HIGH)
    time.sleep(t)
    led7_dark()

# ７セグでノリ感レベルを表示, ５回点滅させる
def display_level(level):
    for i in range(5):
        # もっときれいに書ける？？関数名の中に変数が入っているかどうかがわかればできるけど
        if level == 0:
            light_0(1)
            time.sleep(0.5)
        elif level == 1:
            light_1(1)
            time.sleep(0.5)
        elif level == 2:
            light_2(1)
            time.sleep(0.5)
        elif level == 3:
            light_3(1)
            time.sleep(0.5)
        elif level == 4:
            light_4(1)
            time.sleep(0.5)
        elif level == 5:
            light_5(1)
            time.sleep(0.5)
        elif level == 6:
            light_6(1)
            time.sleep(0.5)
        elif level == 7:
            light_7(1)
            time.sleep(0.5)
        elif level == 8:
            light_8(1)
            time.sleep(0.5)
        elif level == 9:
            light_9(1)
            time.sleep(0.5)
        elif level == 10:
            light_10(1)
            time.sleep(0.5)

# LED1を消す
def led1_dark():
    wp.digitalWrite(pinLedR_1, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG_1, wp.GPIO.LOW)
    wp.digitalWedrite(pinLedB_1, wp.GPIO.LOW)

# LED2を消す
def led2_dark():
    wp.digitalWrite(pinLedR_2, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG_2, wp.GPIO.LOW)
    wp.digitalWedrite(pinLedB_2, wp.GPIO.LOW)

# LED3を消す
def led3_dark():
    wp.digitalWrite(pinLedR_3, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG_3, wp.GPIO.LOW)
    wp.digitalWedrite(pinLedB_3, wp.GPIO.LOW)

# 判定用LEDを消す
def led_judge_dark():
    wp.digitalWrite(pinLedR_judge, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG_judge, wp.GPIO.LOW)
    wp.digitalWedrite(pinLedB_judge, wp.GPIO.LOW)

# LED1 赤, 引数は点灯させる秒数
def led1_Red(t):
    wp.digitalWrite(pinLedR_1, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG_1, wp.GPIO.LOW)
    wp.digitalWedrite(pinLedB_1, wp.GPIO.LOW)
    time.sleep(t)
    led1_dark()
    
# LED2 赤, 引数は点灯させる秒数
def led2_Red(t):
    wp.digitalWrite(pinLedR_2, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG_2, wp.GPIO.LOW)
    wp.digitalWrite(pinLedB_2, wp.GPIO.LOW)
    time.sleep(t)
    led2_dark()

# LED3 赤, 引数は点灯させる秒数
def led3_Red(t):
    wp.digitalWrite(pinLedR_3, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG_3, wp.GPIO.LOW)
    wp.digitalWrite(pinLedB_3, wp.GPIO.LOW)
    time.sleep(t)
    led3_dark()

# 判定用LED 赤, 引数は点灯させる秒数
def led_judge_Red(t):
    wp.digitalWrite(pinLedR_judge, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG_judge, wp.GPIO.LOW)
    wp.digitalWrite(pinLedB_judge, wp.GPIO.LOW)
    time.sleep(t)
    led_judge_dark()

# LED1 緑, 引数は点灯させる秒数
def led1_Green(t):
    wp.digitalWrite(pinLedR_1, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG_1, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB_1, wp.GPIO.LOW)
    time.sleep(t)
    led1_dark()

# LED2 緑, 引数は点灯させる秒数
def led2_Green(t):
    wp.digitalWrite(pinLedR_2, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG_2, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB_2, wp.GPIO.LOW)
    time.sleep(t)
    led2_dark()

# LED3 緑, 引数は点灯させる秒数
def led3_Green(t):
    wp.digitalWrite(pinLedR_3, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG_3, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB_3, wp.GPIO.LOW)
    time.sleep(t)
    led3_dark()

# 判定用LED 緑, 引数は点灯させる秒数
def led_judge_Green(t):
    wp.digitalWrite(pinLedR_judge, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG_judge, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB_judge, wp.GPIO.LOW)
    time.sleep(t)
    led_judge_dark()

# LED1 青, 引数は点灯させる秒数
def led1_Brue(t):
    wp.digitalWrite(pinLedR_1, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG_1, wp.GPIO.LOW)
    wp.digitalWrite(pinLedB_1, wp.GPIO.HIGH)
    time.sleep(t)
    led1_dark()

# LED2 青, 引数は点灯させる秒数
def led2_Brue(t):
    wp.digitalWrite(pinLedR_2, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG_2, wp.GPIO.LOW)
    wp.digitalWrite(pinLedB_2, wp.GPIO.HIGH)
    time.sleep(t)
    led2_dark()

# LED3 青, 引数は点灯させる秒数
def led3_Brue(t):
    wp.digitalWrite(pinLedR_3, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG_3, wp.GPIO.LOW)
    wp.digitalWrite(pinLedB_3, wp.GPIO.HIGH)
    time.sleep(t)
    led3_dark()

# 判定用LED 青, 引数は点灯させる秒数
def led_judge_Brue(t):
    wp.digitalWrite(pinLedR_judge, wp.GPIO.LOW)
    wp.digitalWrite(pinLedG_judge, wp.GPIO.LOW)
    wp.digitalWrite(pinLedB_judge, wp.GPIO.HIGH)
    time.sleep(t)
    led_judge_dark()

# LED1 黄, 引数は点灯させる秒数
def led1_Yellow(t):
    wp.digitalWrite(pinLedR_1, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG_1, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB_1, wp.GPIO.LOW)
    time.sleep(t)
    led1_dark()

# LED2 黄, 引数は点灯させる秒数
def led2_Yellow(t):
    wp.digitalWrite(pinLedR_2, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG_2, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB_2, wp.GPIO.LOW)
    time.sleep(t)
    led2_dark()

# LED3 黄, 引数は点灯させる秒数
def led3_Yellow(t):
    wp.digitalWrite(pinLedR_3, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG_3, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB_3, wp.GPIO.LOW)
    time.sleep(t)
    led3_dark()

# 判定用LED 黄, 引数は点灯させる秒数
def led_judge_Yellow(t):
    wp.digitalWrite(pinLedR_judge, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG_judge, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB_judge, wp.GPIO.LOW)
    time.sleep(t)
    led_judge_dark()

# LED1 白, 引数は点灯させる秒数
def led1_White(t):
    wp.digitalWrite(pinLedR_1, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG_1, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB_1, wp.GPIO.HIGH)
    time.sleep(t)
    led1_dark()

# LED2 白, 引数は点灯させる秒数
def led2_White(t):
    wp.digitalWrite(pinLedR_2, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG_2, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB_2, wp.GPIO.HIGH)
    time.sleep(t)
    led2_dark()

# LED3 白, 引数は点灯させる秒数
def led3_White(t):
    wp.digitalWrite(pinLedR_3, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG_3, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB_3, wp.GPIO.HIGH)
    time.sleep(t)
    led3_dark()

# 判定用LED 白, 引数は点灯させる秒数
def led_judge_White(t):
    wp.digitalWrite(pinLedR_judge, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedG_judge, wp.GPIO.HIGH)
    wp.digitalWrite(pinLedB_judge, wp.GPIO.HIGH)
    time.sleep(t)
    led_judge_dark()

# switch1を押したら３つめのLEDが青色に点灯、switch2を押したら３つめのLEDがオレンジ色に点灯
def switch_led_brue_or_white(mode, randomColorList):
    # 最初の状態はFalseにする
    lastState_brue = False
    # newState_brue = wp.digitalRead(pinSw_1)
    if mode == 2 or mode == 4:
        lastState_white = False
        # newState_white = wp.wpdigitalRead(pinSw_2)

    if mode == 1 or mode == 2:
        bpm = SLOW_BPM
        music_len = 150  #  小節数
        play_time = tempo * music_len  #  終了させる時間
        introTime = SLOW_INTRO  #  イントロの長さ

    else:
        bpm = QUICK_BPM
        music_len = 218
        play_time = tempo * music_len
        introTime = QUICK_INTRO
    bps = bpm / 60
    tempo = 1 / bps  #  1拍子の間隔

    startTime = time.time()

    judge_dict = {"perfect" : 0, "good" : 0, "bad" : 0} # 判定のリスト
    print("Push Switch") # タクトスイッチでタイミングを取る

    # 音楽の終了まで回し続ける
    # inputを待たないといけないので最後のinputで関数が終わるように調整する
    while time.time() - startTime < play_time + introTime:  #  受付時間中ならTrue
        newState_brue = wp.digitalRead(pinSw_1)
        if mode == 2 or mode == 4:
            newState_white = wp.digitalRead(pinSw_2)
        # 青色スイッチが押されたときの判定
        if (newState_brue == True) and (lastState_brue == False):
            led3_Brue(0.1)
            print("3 input Brue", end = " ") # 入力した３のリズム, debug
            inputTime = time.time() - startTime
            judge = checkInput(inputTime, tempo, mode, "Brue", randomColorList)
            judge_dict[judge] += 1 # 判定リストに追加
            if judge == "perfect":
                led_judge_Green(0.5) # 長すぎて他に影響させる？, here
            elif judge == "good":
                led_judge_Yellow(0.5)
            elif judge == "bad":
                led_judge_Red(0.5)
            # time.sleep(CHATTERING)  # 上でsleepしてるのでチャタリング除去いらない, here
        
        # オレンジスイッチが押されたときの判定
        if (mode == 2 or mode == 4) and (newState_white == True) and (lastState_white == False):
            led3_Brue(0.1)
            print("3 input White", end = " ") # 入力した３のリズム, debug
            inputTime = time.time() - startTime
            judge = checkInput(inputTime, tempo, mode, "Brue", randomColorList)
            judge_dict[judge] += 1 # 判定リストに追加
            if judge == "perfect":
                led_judge_Green(0.5)
            elif judge == "good":
                led_judge_Yellow(0.5)
            elif judge == "bad":
                led_judge_Red(0.5)
                # time.sleep(CHATTERING)  # 上でsleepしてるのでチャタリング除去いらない, here

        lastState_brue = newState_brue
        if mode == 2 or mode == 4:
            lastState_white = newState_white
    
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
    maxScore = totalRhythm * 2 # 全部perfectのときのスコア
    score = judge_dict["perfect"] * 2 + judge_dict["good"] # ゲットした最終スコア
    level = int(10 * score / maxScore) # 最後に７セグへ表示するノリ感レベル
    
    # コンソールへの結果の表示
    print()
    print("perfect : " + str(judge_dict["perfect"]))
    print("good    : " + str(judge_dict["good"]))
    print("bad     : " + str(judge_dict["bad"]))
    print(f"your score : {score} / {maxScore}")

    return level


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


# 難易度選択入力
# mode 1 > easy,      1 LED
# mode 2 > easy,      2 LED
# mode 3 > difficult, 1 LED
# mode 4 > difficult, 2 LED
def choose_mode_input():
    mode = 0 # modeの初期値
    startTime = time.time()
    while mode == 0:
        inputTime = time.time() - startTime # 経過時間
        # スタート時間のリセット
        if inputTime >= 4:
            startTime = time.time()
        # 7セグを見てボタンを押したらモードが選択される
        if (0 <= inputTime and inputTime < 1) and (wp.digitalWrite(pinSw_1) == True or wp.digitalWrite(pinSw_2) == True):
            mode = 1
        if (1 <= inputTime and inputTime < 2) and (wp.digitalWrite(pinSw_1) == True or wp.digitalWrite(pinSw_2) == True):
            mode = 2
        if (2 <= inputTime and inputTime < 3) and (wp.digitalWrite(pinSw_1) == True or wp.digitalWrite(pinSw_2) == True):
            mode = 3
        if (3 <= inputTime and inputTime < 4) and (wp.digitalWrite(pinSw_1) == True or wp.digitalWrite(pinSw_2) == True):
            mode = 4
    return mode

# 難易度選択表示, choose_mode_inputと並列に動かす
def choose_mode_display():
    # 入力し終わるまで回し続けたい、条件あってる？, here
    while wp.digitalWrite(pinSw_1) == False and wp.digitalWrite(pinSw_2) == False:
        light_1(1)
        if wp.digitalWrite(pinSw_1) == True or wp.digitalWrite(pinSw_2) == True:
            break
        light_2(1)
        if wp.digitalWrite(pinSw_1) == True or wp.digitalWrite(pinSw_2) == True:
            break
        light_3(1)
        if wp.digitalWrite(pinSw_1) == True or wp.digitalWrite(pinSw_2) == True:
            break
        light_4(1)

# 上の２つの関数がうまく動かないときはコンソールからモード選択を行う
# モード選択入力
def choose_mode():
    mode = 0
    while mode == 0:
        mode = int(input("choose mode : "))
    return mode

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
    
    # print(music_list_start_speed[0][0])
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

# 三連符のリズム、引数は間隔、色
def rhythm3(t_bitween, color):
    debugFlag = False # TrueにしたらLED、Falseにしたらコンソールで表示
    if color == "Brue" and debugFlag == False:
        print(1, color)
        led1_Brue(0.1)
        time.sleep(t_bitween - 0.1)
        print(2, color)
        led2_Brue(0.1)
        time.sleep(t_bitween - 0.1)
        print(3, color) # debug
        # led3_Brue(0.1) # debug, コメント解除すると0.1秒止まるのでずれるかも

    elif color == "White" and debugFlag == False:
        print(1, color)
        led1_White(0.1)
        time.sleep(t_bitween - 0.1)
        print(2, color)
        led2_White(0.1)
        time.sleep(t_bitween - 0.1)
        print(3, color) # debug
        # led3_White(0.1) # debug、コメント解除すると0.1秒止まるのでずれるかも
    
    # コンソール飲みに表示, debug
    if debugFlag == True:
        print(1, color)
        time.sleep(t_bitween)
        print(2, color)
        time.sleep(t_bitween)
        print(f"3 {color} wrong") # ３連符の最後の３とその秒数 # debug 後で消す

# 難易度easy_1LEDをスタート here
def play_music(mode, randomColorList):
    # mode１と３のときは青色LEDで固定, mode2と4はwhile文の中でランダムに変える
    if mode == 1 or mode == 3:
        color = "Brue"
    if mode == 1 or mode == 2:
        bpm = SLOW_BPM + 1.9 - 1.5  # ちょっとだけ遅延がある？？
        introTime = SLOW_INTRO
    else:
        bpm = QUICK_BPM + 2.0 # 遅延を考慮
        introTime = QUICK_INTRO
    bps = bpm / 60
    tempo = 1 / bps  #  1拍子の間隔

    music_list_start_speed = music_trans(tempo, mode, "start")
    correct_list = music_trans(tempo, mode, "end")        

    print(f"intro {introTime}s")
    time.sleep(introTime) # 音源のイントロ、時間が違うかも

    index = 0 # for文のインデックス
    # 楽譜に合わせてリズムを流す
    for startRhythm, speed in music_list_start_speed:
        # mode２と４のときは色をランダムに変える
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

# playsoundを用いるにはターミナルでインストールが必要かも
# mp3ファイルからBGMを流す
def backGroundMusic(mode):
    if mode == 1 or mode == 2:
        playsound("パチパチ三人衆.mp3")
    else:
        playsound("バリバリ三人衆.mp3")

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
    print(f"randList = {randList}\n") # debug
    return randList

# LED_1
pinLedR_1 = 2
pinLedG_1 = 3
pinLedB_1 = 4

# LED_2
pinLedR_2 = 17
pinLedG_2 = 27
pinLedB_2 = 22

# LED_3
pinLedR_3 = 10
pinLedG_3 = 9
pinLedB_3 = 11

# LED_judge
pinLedR_judge = 25
pinLedG_judge = 8
pinLedB_judge = 7

# switch_1
pinSw_1 = 12

# switch_2
pinSw_2 = 7

# 7セグメントLED
pinLedA = 6
pinLedB = 5
pinLedC = 21
pinLedD = 20
pinLedE = 16
pinLedF = 13
pinLedG = 19
pinLedDP = 26


wp.wiringPiSetupSys()

wp.pinMode(pinLedR_1, wp.GPIO.OUTPUT)
wp.pinMode(pinLedG_1, wp.GPIO.OUTPUT)
wp.pinMode(pinLedB_1, wp.GPIO.OUTPUT)
wp.pinMode(pinLedR_2, wp.GPIO.OUTPUT)
wp.pinMode(pinLedG_2, wp.GPIO.OUTPUT)
wp.pinMode(pinLedB_2, wp.GPIO.OUTPUT)
wp.pinMode(pinLedR_3, wp.GPIO.OUTPUT)
wp.pinMode(pinLedG_3, wp.GPIO.OUTPUT)
wp.pinMode(pinLedB_3, wp.GPIO.OUTPUT)
wp.pinMode(pinLedR_judge, wp.GPIO.OUTPUT)
wp.pinMode(pinLedG_judge, wp.GPIO.OUTPUT)
wp.pinMode(pinLedB_judge, wp.GPIO.OUTPUT)

wp.pinMode(pinSw_1, wp.GPIO.INPUT)
wp.pinMode(pinSw_2, wp.GPIO.INPUT)

wp.pinMode(pinLedA, wp.GPIO.OUTPUT)
wp.pinMode(pinLedB, wp.GPIO.OUTPUT)
wp.pinMode(pinLedC, wp.GPIO.OUTPUT)
wp.pinMode(pinLedD, wp.GPIO.OUTPUT)
wp.pinMode(pinLedE, wp.GPIO.OUTPUT)
wp.pinMode(pinLedF, wp.GPIO.OUTPUT)
wp.pinMode(pinLedG, wp.GPIO.OUTPUT)
wp.pinMode(pinLedDP, wp.GPIO.OUTPUT)

try:
    # light debug
    time.sleep(1)
    light_0(0.5)
    light_1(0.5)
    light_2(0.5)
    light_3(0.5)
    light_4(0.5)
    light_5(0.5)
    light_6(0.5)
    light_7(0.5)
    light_8(0.5)
    light_9(0.5)
    light_10(0.5)

    # LED debug
    led1_Red(0.5)
    led2_Red(0.5)
    led3_Red(0.5)
    led1_Green(0.5)
    led2_Green(0.5)
    led3_Green(0.5)
    led1_Brue(0.5)
    led2_Brue(0.5)
    led3_Brue(0.5)
    led1_Yellow(0.5)
    led2_Yellow(0.5)
    led3_Yellow(0.5)
    led1_White(0.5)
    led2_White(0.5)
    led3_White(0.5)

    # ここからmain
    # 難易度選択入力と表示を並列させる
    with ThreadPoolExecutor(max_workers=2) as pool:
        future = pool.submit(choose_mode_input)
        pool.submit(choose_mode_display) # debug
    
    mode = future.result()

    # 上の並列実行している難易度選択がうまく行かないときはコンソールから行う
    # mode = choose_mode()

    randomColorList = randList_maker(mode) # ランダムリストを作る

    # play_musicとinput_switchを並列実行
    with ThreadPoolExecutor(max_workers=4) as pool:
        future = pool.submit(switch_led_brue_or_white, mode, randomColorList)
        pool.submit(play_music, mode, randomColorList)
        # pool.submit(backGroundMusic, mode) # debug, できれば音源を流したい
        # pool.submit(correct_debug, mode) # debug ここをコメントアウトするとbpmのズレが少なくなる, 今は音楽を流すのに使っている

    level = future.result()

    # ノリ感レベルの表示
    print(f"Your level is {level}\n")
    display_level(level)
    
finally:
    # LEDを消す
    led1_dark()
    led2_dark()
    led3_dark()
    led_judge_dark()
    # 7セグを消す
    led7_dark()
    print("end\n")
    