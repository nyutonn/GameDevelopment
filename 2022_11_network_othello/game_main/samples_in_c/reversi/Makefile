OBJS = color.o board.o player.o game.o 

DEFS = -D_POSIX_C_SOURCE=200809L -D_ISOC99_SOURCE -D_XOPEN_SOURCE=500
OPTS = -std=c99 -Wall -g $(DEFS)

CC = gcc $(OPTS)
INCLUDE = -I ./

TARGET_SINGLE = single_play

.PHONY: all 
all: $(TARGET_SINGLE)

$(TARGET_SINGLE): single_play.c $(OBJS)
	$(CC) $(INCLUDE) -o $(TARGET_SINGLE) $(OBJS) $<

%.o:%.c %.h
	$(CC) $(INCLUDE) -o $@ -c $<

.PHONY: doc
doc:
	doxygen doxygen.conf

.PHONY: clean
clean:
	rm -f  $(TARGET_SINGLE)
	rm -rf *.dSYM
	rm -f $(OBJS)
	rm -rf ./doc
