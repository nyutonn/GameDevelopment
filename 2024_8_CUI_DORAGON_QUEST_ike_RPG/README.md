## 概要
* 趣味のゲーム開発の記録です
* ゲームの概要，開発期間，使用言語・ツール，プレイ動画をまとめています
* [GitHub](https://github.com/nyutonn/GameDevelopment/tree/main)にてプログラムを公開しているものもあります

<br>

## 目次
1. [CUIドラクエ風RPG](#cuiドラクエ風rpg)
2. [GUIポケモン名前当てクイズ](#イラスト名前当てクイズ)
3. [CUIテトリス](#guiテトリス)
4. [LEDリズム天国](#ledリズム天国)
5. [ネットワーク対戦型オセロゲーム](#ネットワーク対戦型オセロゲーム)
6. [Unity](#unity)

## CUIドラクエ風RPG
<img src="/assets/img/rpg_ドラクエ風RPGサムネイル.png" width="800x400">

##### 概要
* 短期間でC++を用いて作成したCUIドラクエ風RPG
* １週間のC++新人研修体験短期インターンシップの最終提出課題として作成
* メモリアロケーター（Pool Allocator）を用いたメモリ管理
* ステートマシンを用いたゲーム状態の管理
  * 状態遷移の詳細は [GitHub 上の project_drawings フォルダ内のPDF](https://github.com/nyutonn/GameDevelopment/blob/main/2024_8_CUI_DORAGON_QUEST_ike_RPG/project_drawings/ドラクエ風RPG操作説明.pdf)に記載
* ゲームプログラムは[GitHub](https://github.com/nyutonn/GameDevelopment/blob/main/2024_8_CUI_DORAGON_QUEST_ike_RPG/game_main/CUIドラクエ風RPG_mac/run.cpp)にて公開

##### 開発期間
* 2024.8.8-2024.8.9
* 2 日

##### 使用言語・ツール
* 使用言語: C++
* OS: macOS・WindowsOS
* エディター: VS Code・Visual Studio 2022

##### プレイ動画
* ゲームオーバー
    <ul class="no-bullet"><li>
    <video width="800" controls>
    <source src="/assets/movie/rpg_ゲームオーバー.mp4" type="video/mp4">
    </video></li></ul>
* ゲームクリア
    <ul class="no-bullet"><li>
    <video width="800" controls>
    <source src="/assets/movie/rpg_ゲームクリア.mp4" type="video/mp4">
    </video></li></ul>