## ネットワーク対戦型オセロゲーム
<img src="/2022_11_network_othello/game_play_caprures/othello_終了画面.png" width="500x500">

### フォルダ概要
* C言語で開発したネットワークオセロゲームです
  * 2つの端末でオセロを楽しむことができます
* game_main フォルダにはメインのCプログラムなどが入っています
* game_play_captures フォルダにはゲームのプレイ動画が入っています
* project_drawings フォルダにはゲーム開発時に作成した概要が入っています

### ゲーム概要
* 2つの端末で遊べるネットワークオセロゲーム
* Oは白，Xが黒を表す
* VS人間，VSコンピュータ どちらも可能
* サーバのコンピュータはランダムではなく盤面を参考にした内部のアルゴリズムに従って指す
  <!-- * todo モンテカルロ法だっけ？ -->
* クライアントのコンピュータはランダムに指す
* オセロのマス目を左右にABCDEFGH，上下に12345678と表す
* 手筋を表すときには左右から先に指定（例：D3）
* ゲームプログラムは[GitHub](https://github.com/nyutonn/GameDevelopment/tree/main/2022_11_network_othello/game_main)にて公開

### 開発期間
* 2022.10-2022.11
* 約1ヶ月

### 使用言語・ツール
* 言語: Python
* OS: Windows OS
* ターミナル: Windows Terminal
* エディター: VS Code

### １つのPCを用いたプレイの仕方
* [Gitリポジトリ](https://github.com/nyutonn/GameDevelopment)をクローンする
* カレントディレクトリを以下にする`GameDevelopment/2022_11_network_othello/game_main`
* ターミナルを2つ立ち上げ，どちらもgame_mainフォルダへ移動する
 * 片方をサーバ，もう片方をクライアントとして扱う
* サーバ側で `java -jar reversi-net.jar server 3000` を実行
  * -hオプションを付けると手動で手を入力する
  * -hオプションを付けないと内部のアルゴリズムに従ってランダムより良い手を指す
  * `server`の後の`3000`はポート番号であり，サーバ側とクライアント側で同じ番号を用いること
* クライアント側で `java -jar reversi-net.jar client -h localhost 3000` を実行
  * -hオプションを付けると手動で手を入力する
  * -hオプションを付けないとランダムに手を決める