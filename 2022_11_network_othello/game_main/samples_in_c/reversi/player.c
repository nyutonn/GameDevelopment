#include "player.h"
#include "board.h"
#include "color.h"

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

static void do_nothing( void* state ) {}



static int get_input( const board_t* board, const color_t color,
                int* i, int* j ) {

  while ( true ) {
    printf( (color==BLACK) ? "BLACK> " : "WHITE> " );
    fflush( stdout );

    char* buf  = NULL;
    size_t len = 0;
    ssize_t read;

    if ( (read = getline(&buf, &len, stdin) ) > 0 ) {
      if ( read > 2 ) {
        *j = buf[0] - 'A' + 1;
        *i = buf[1] - '1' + 1;

        if ( is_legal_move(board, color, make_move(*i,*j)) ) {
          break;
        }
        else {
          puts("Illegal move! Input another.");
        }
      }
      free( buf );
    }
    else {
      return -1;
    }
  }
  return 0;
}

static int human_play( const board_t* board, const color_t color, struct move_t* mp, void* dummy ) {
  print_board_with_legal_moves( board, color );
  int i = 4; int j = 4;
  if ( !is_playable( board, color ) ) {
    puts("You have no chance to move!");
    *mp = passed();
  }
  else {
    if ( get_input( board, color, &i, &j ) < 0 ) {
      return -1;
    }
    *mp = make_move( i, j );
  }
  return 0;
}

struct player_t* make_human_player() {
  struct player_t* t = 
    (struct player_t*) malloc( sizeof( struct player_t ) );
  t->_hidden_state = NULL;
  t->_play         = human_play;
  t->_clean_up     = do_nothing;
  
  return t;
}

static int random_play( const board_t* board, const color_t color, struct move_t* mp, void* state  ) {
  struct move_t buf[64];
  int  len;
  legal_moves( board, color, buf, &len );
  if ( len > 0 ) {
    int k = random() % len;
    *mp = buf[ k ];
  }
  else {
    *mp = passed();
  }
  if ( state != NULL ) { 
    int microsec = *((int*) state);
    struct timespec tspec; 
    tspec.tv_sec  = microsec / 1000000;;
    tspec.tv_nsec = microsec * 1000;
    nanosleep( &tspec, NULL ); 
  }
  return 0;
}

struct player_t* make_random_player() {
  struct player_t* t = 
    (struct player_t*) malloc( sizeof( struct player_t ) );
  t->_hidden_state = NULL;
  t->_play         = random_play;
  t->_clean_up     = free;
  
  return t;
}

struct player_t* make_slow_random_player( int wait ) {
    struct player_t* p = malloc( sizeof(struct player_t) );
    int*   q = malloc( sizeof( int ) );
    *q = wait;
    p->_hidden_state = q;
    p->_play = random_play;
    p->_clean_up = free;
    return p;
}


static int replaying_random_play( const board_t* board, const color_t color, struct move_t* mp, void* state  ) {
  FILE* fp = (FILE*) state; 

  struct move_t buf[64];
  int  len;
  legal_moves( board, color, buf, &len );
  if ( len > 0 ) {
    unsigned int r = 0;
    int ret = fread( &r, sizeof(unsigned int), 1, fp );
    if ( ret < 0  ) {
      fputs( "The file ends too early", stderr );
      return -1;      
    }

    int k = r % len;
    *mp = buf[ k ];
  }
  else {
    *mp = passed();
  }
  return 0;
}

static void myfclose( void* p ) {
  fclose( (FILE*) p );
}

struct player_t* make_replaying_random_player( const char* filepath ) {
  FILE* fp = fopen( filepath, "r" );
  if ( fp == NULL ) {
    exit(1); 
  }

  struct player_t* p = malloc( sizeof(struct player_t) );

  p->_hidden_state = fp;
  p->_play = replaying_random_play;
  p->_clean_up = myfclose;
  return p;
}




