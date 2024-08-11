## LEDリズム天国
<img src="/2023_1_Rhythm_Heaven_LED/game_play_captures/ポスター_オリジナルバリバリ三人衆.png" width="600x600">

### フォルダ概要
* Pythonとラズベリーパイで開発したLEDリズム天国風ゲームです
* game_main フォルダにはメインのPythonプログラムが入っています
* game_play_captures フォルダにはゲームのプレイ動画が入っています
* project_drawings フォルダにはゲーム開発時に用いた配線図や楽譜，ラズベリーパイの写真が入っています
* Rhythm_Heaven_original_bgm フォルダには，パチパチ三人衆とバリバリ三人衆の元の音源が入っています．

### ゲーム概要
* ラズベリーパイを用いて開発したリズム天国風リズムゲーム
* 初代リズム天国GBA「パチパチ三人衆」「バリバリ三人衆」の音楽にノッて，リズムに合わせてボタンを押す
* 2つのLEDが順に光るので，リズムに合わせて3つめのLEDを点灯させる
* 押したタイミングに合わせて4つめのLEDの色が変化する
* 曲が終わった際に得点を集計し，7セグメントLEDでレベル 0 ~ 9 で表示される
* ゲームプログラムは[GitHub](https://github.com/nyutonn/GameDevelopment/tree/main/2023_1_Rhythm_Heaven_LED/game_main)にて公開

### 開発期間
* 2022.12-2023.1
* 約1ヶ月

### 使用言語・ツール
* ハードウェア: ラズベリーパイ (Raspberry Pi)
  <img src="/2023_1_Rhythm_Heaven_LED/game_play_captures/プレイ画像1.jpg" width="300x300">
* 言語: Python
* OS: Windows OS
* ターミナル: Windows Terminal
* エディター: VS Code