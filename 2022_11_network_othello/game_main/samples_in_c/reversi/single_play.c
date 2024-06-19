/**


@mainpage

一人用リバーシの実装．

@section 使い方

引数なしで\c single_play を起動すると，ランダムプレイヤーと対戦できる．
@verbatim
$ ./single_play 
@endverbatim
上記を入力すると，以下が表示される．`BLACK>`はあなたが黒であることを表している．
@verbatim
You are a black player.
 |A B C D E F G H
-+----------------
1|- - - - - - - -
2|- - - - - - - -
3|- - - . - - - -
4|- - . O X - - -
5|- - - X O . - -
6|- - - - . - - -
7|- - - - - - - -
8|- - - - - - - -
Black: 2
White: 2
BLACK>
@endverbatim
ここで，「`.`」で表されているのが着手可能な場所である．手を入力するには石を置く座標を入力する．たとえば「`F5`」と入力すると相手は適当に場所に打ち，またプレイヤーの手番となる．
@verbatim
...
BLACK> F5
 |A B C D E F G H
-+----------------
1|- - - - - - - -
2|- - - - - - - -
3|- - . . . . . -
4|- - - O O O - -
5|- - - X X X - -
6|- - - - - - - -
7|- - - - - - - -
8|- - - - - - - -
Black: 3
White: 3
BLACK>
@endverbatim
これを繰り返し，ゲームが進んでいく．途中でやめるには`CTRL+D`を入力する．

また，以下のように`-r`オプションを付けて起動すると，ランダムプレイヤー同士の対戦ができる．
@verbatim
$ ./single_play -r
@endverbatim

@section ファイル構成

上の「ファイル」も参考にせよ．

  \li `color.h`，`color.c`   石の色あるいは手番を実装．
  \li `board.h`，`board.c`   盤面のデータおよび操作（合法手の判定や石をひっくり返す処理）を実装．
  \li `player.h`，`player.c` 抽象化されたプレイヤー（人，ランダム等）を実装．`player_t` 構造体の理解は実験の遂行において重要．
  \li `game.h`，`game.c`     プレイヤー同士のリバーシの対戦を実装．
  \li `debug.h`              デバッグ用マクロを提供．
  \li `single_play.c`        このプログラムのmain関数を定義．

実験の遂行にあたっては上記のファイルは書き換える必要はない．別のファイルに関数を実装していけばよいだろう．

*/


#include "game.h"
#include "board.h"
#include "color.h"
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <stdio.h>

void usage( const char* prog_name ) {
  printf("usage: %s [-r]\n", prog_name );
  exit(0);
}

int main( int argc, char* argv[] ) {
  srandom( time(NULL) ^ getpid() );
  int is_random = 0;
  int ch = 0;

  /* 引数をパース */
  while ( (ch = getopt( argc, argv, "r" )) != -1 ) {
    switch (ch) {
    case 'r':
      is_random = 1;
      break;
    default:
      /* 他のオプションが渡されたとき */
      usage( argv[0] );
    }
  }

  struct player_t* my_player;
  struct player_t* op_player = make_random_player();

  if ( is_random ) {
    my_player = make_random_player();
  }
  else {
    my_player = make_human_player();
  }

  board_t* b;

  int my_color = random() & 0x01; 

  /* ランダムにプレイヤーが黒番か白番かを選択 */
  if ( my_color ) {
    /* プレイヤーは黒番 */ 
    puts("You are a black player.");
    game( my_player, op_player, &b );
  }
  else {
    /* プレイヤーは白番 */ 
    puts("You are a white player.");
    game( op_player, my_player, &b );
  }
  destruct_player( my_player );
  destruct_player( op_player );

  puts("Game finished.");
  print_board( b );

  printf("You played %s.\n", (my_color ? "black" : "white"));

  destruct_board( b );

  return 0;
}
