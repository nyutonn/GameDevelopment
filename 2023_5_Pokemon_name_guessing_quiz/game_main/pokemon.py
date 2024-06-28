import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk
import jaconv
from playsound import playsound

# bgmは以下のサイトから流すこと
# https://soundlibrary.pokemon.co.jp/musicbox?version=rg

# ウィンドウ
root = tk.Tk()
root.geometry('500x500')
root.title('ポケモン名前当てクイズ')

# 固定テキスト
main_label = tk.Label(root, text='このポケモンの名前を入力してね', font=('', 20))
main_label.place(x=10, y=10)

# 名前入力テキスト
name_txt = tk.Entry(root, width=10)
name_txt.place(x=170, y=370)
name_label = tk.Label(root, text='このポケモンの名前は？', font=('', 15))
name_label.place(x=10, y=370)

# 決定ボタン
value_var = tk.StringVar()
value_label = tk.Label(root, textvariable=value_var)
def on_ok():
    global ans
    if ans == jaconv.hira2kata(name_txt.get()):
        value_var.set('正解！')
        value_label.place(x=320, y=400)
        # nextを押せるようにする
        next_btn['state'] = tk.NORMAL
        # 正答率の更新
        global maru_cnt
        global batu_cnt
        global rate
        maru_cnt += 1
        rate = int(maru_cnt / (batu_cnt + maru_cnt) * 100)
        maru_var.set(f'正答数：{maru_cnt}')
        rate_var.set(f'正答率：{rate}％')
        # 正解音楽を鳴らす
        playsound('../bgm/クイズ正解1.mp3')

    else:
        value_var.set('違います')
        value_label.place(x=320, y=400)
        # 不正解音楽を鳴らす
        playsound('../bgm/クイズ不正解1.mp3')

ok_btn = tk.Button(root, text='キミにきめた！', command=on_ok)
ok_btn.place(x=300, y=370)

# 降参ボタン
ans_label = tk.Label(root, font=('', 20))
def on_giveup():
    global ans
    global ans_label
    ans_label = tk.Label(root, text=ans, font=('', 20))
    ans_label.place(x=350, y=320)
    next_btn['state'] = tk.NORMAL
    # 正答率の更新
    global maru_cnt
    global batu_cnt
    global rate
    batu_cnt += 1
    rate = int(maru_cnt / (batu_cnt + maru_cnt) * 100)
    batu_var.set(f'誤答数：{batu_cnt}')
    rate_var.set(f'正答率：{rate}％')

# 次の問題に行くボタン
def on_next():
    try:
        # 全てのラベルのリセットをする
        value_label.place_forget()
        global hint_label
        hint_label.place_forget()
        global ans_label
        ans_label.place_forget()
    except:
        ans_label.place_forget()
    finally:
        # nextを押せないようにする
        next_btn['state'] = tk.DISABLED
        # ポケモン選択
        choice_pokemon()

next_btn = tk.Button(root, text='次の問題へ', command=on_next)
next_btn.place(x=370, y=450)
# 降参するか正解するまで押せない
next_btn['state'] = tk.DISABLED

giveup_btn = tk.Button(root, text='降参', command=on_giveup)
giveup_btn.place(x=10, y=430)


# ヒント表示テキスト
# hint_label = tk.Label(root, text=ans)
def on_hint():
    global ans
    hint = ans[0]
    for i, c in enumerate(ans):
        if i == 0: 
            continue
        hint += ' _ '
    global hint_label
    hint_label = tk.Label(root, text=hint)
    hint_label.place(x=150, y=433)
    # ヒント音楽を鳴らす
    global area
    # デモプレイ用の「オリジナル」の場合はポケセンの音楽ではない音楽にする
    if area == 'オリジナル':
        pass
    else:
        playsound('../bgm/ポケセン回復.mp3')

# ヒントボタン
hint_btn = tk.Button(root, text='ヒント', command=on_hint)
hint_btn.place(x=70, y=430)

# 地方を決定するボタン
def on_area_ok():
    global area
    area = cmb.get()
    if area == '':
        return 0    
    choice_pokemon()

area_ok_btn = tk.Button(root, text='この地方で遊ぶ', command=on_area_ok)
area_ok_btn.place(x=350, y=70)

# 地方を選ぶコンボボックス
area_label = tk.Label(root, text='地方選択', font=('', 15))
area_label.place(x=350, y=10)
areas = ['カントー地方', 'ジョウト地方', 'ホウエン地方', 'シンオウ地方', 'イッシュ地方', 'カロス地方', 'アローラ地方', 'ガラル地方', 'パルデア地方', '全て', 'オリジナル']
cmb = ttk.Combobox(root, values=areas, width=10)
cmb.place(x=350, y=40)

# デモプレイ用 random.seed固定
global random_seed_index
random_seed_index = -1

# 問題選出
def choice_pokemon():
    # オリジナル版の場合
    global area
    if area == 'オリジナル':
        numbers = [0, 1, 2]
        names = ['ニャオハ', 'ヒバニー', 'ポッチャマ']
    # オリジナル版ではない場合
    else:
        with open(f'../data/pokemon.csv') as fr:
            numbers, names, local_areas = [], [], []
            for line in fr:
                line = line.rstrip()
                if line == 'area,id,name,img':
                    continue
                local_area_num, number, name, _ = line.split(',')
                # エリアを合わせる
                if int(local_area_num) == 10:
                    local_area = 'パルデア地方'
                else:
                    local_area = areas[int(local_area_num)-1]
                # エリア指定
                # global area
                if area == local_area:
                    numbers.append(number)
                    names.append(name)
                # エリアを全てにしていたら全部ぶちこむ
                elif area == '全て':
                    numbers.append(number)
                    names.append(name)
                    local_areas.append(local_area)
    # ランダムで１つ取り出す
    # デモプレイ用シード固定
    random_seed_list = [5, 0, 1]
    global random_seed_index
    random_seed_index += 1
    random.seed(random_seed_list[random_seed_index]) # 0: ヒバニー, 1: ニャオハ 5:ポッチャマ

    rnd_index = random.randint(0, len(numbers)-1)
    ans_num = numbers[rnd_index]
    global ans
    ans = names[rnd_index]
    print(ans, ans_num)

# 写真表示
# キャンバス
    canvas = tk.Canvas(root, bg='white', height=300, width=300)
    canvas.place(x=10, y=50)
    if area == '全て':
        ans_area = local_areas[rnd_index]
        img = Image.open(f'../pokemon_picture/{ans_area}/{ans_num}.png')
    # 追記，オリジナル版
    elif area == 'オリジナル':
        img = Image.open(f'../original_picture/{names[rnd_index]}.jpg')
    else:
        img = Image.open(f'../pokemon_picture/{area}/{ans_num}.png')
    img = img.resize((300, 300))
    img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image=img, anchor=tk.NW)
    root.mainloop()


# 正解率表示
# 正解率を出すためのデータ
global maru_cnt
maru_cnt = 0
global batu_cnt
batu_cnt = 0
global rate
rate = 0
# 正解数, 不正解数, 正答率のラベル
maru_var = tk.StringVar()
maru_var.set('正答数：0')
maru_label = tk.Label(root, textvariable=maru_var)
maru_label.place(x=350, y=250)
batu_var = tk.StringVar()
batu_var.set('誤答数：0')
batu_label = tk.Label(root, textvariable=batu_var)
batu_label.place(x=350, y=270)
rate_var = tk.StringVar()
rate_var.set('正答率：0％')
rate_label = tk.Label(root, textvariable=rate_var)
rate_label.place(x=350, y=290)

# 音楽を鳴らす？


root.mainloop()