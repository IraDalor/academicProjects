p3:  proj3.tab.o lex.yy.o 
	cc -o p3 lex.yy.o proj3.tab.o 

proj3.tab.o: proj3.tab.c
	cc -c proj3.tab.c

proj3.tab.c: proj3.y
	bison -d proj3.y

lex.yy.o: lex.yy.c proj3.tab.h
	cc -c lex.yy.c

lex.yy.c: proj3.l proj3.tab.c
	flex proj3.l
