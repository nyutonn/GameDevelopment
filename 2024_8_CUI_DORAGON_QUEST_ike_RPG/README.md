### 概要
* C++で作成したCUIドラクエ風RPGです
  * １週間の短期インターンシップの提出課題として作成しました
  * メモリアロケーター（Pool Allocator）を用いたメモリ管理を行っています
  * ステートマシンを用いたゲーム状態の管理を行っています（状態遷移の詳細は project_drawings フォルダのPDFに記載）
* game_main フォルダにはメインのPythonプログラムが入っています
* game_play_captures フォルダにはゲームのプレイ動画が入っています
* project_drawings フォルダにはゲーム状態の遷移を表したPDFが入っています

### 実行方法(mac)
ターミナルで以下のコードを実行する
```
git clone https://github.com/nyutonn/GameDevelopment.git
cd GameDevelopment/2024_8_CUI_DORAGON_QUEST_like_RPG/game_main/CUIドラクエ風RPG_mac
g++ -o run run.cpp
./run
```

### 実行方法(Windows)
2024_8_CUI_DORAGON_QUEST_like_RPG/game_main/CUIドラクエ風RPG_windows/Win32/rpg.exe を実行
