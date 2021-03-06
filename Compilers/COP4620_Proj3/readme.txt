Project 3 functions as expected per specifications.

SPECIFICATIONS:
This is a small assignment designed to give you experience
using LEX (flex)  and YACC (bison).

For this exercise you are to generate a LEX (.l) file to
recognize tokens that are to be input to the parser (.y). Use
YACC to recognize (or report) errors for the strings of the
following grammar that generates sql queries. 

-------------------------------------------------------------
The following is a grammar for SQL syntax. 

start 
	::= expression

expression
	::= one-relation-expression | two-relation-expression

one-relation-expression
	::= renaming | restriction | projection

renaming 
	::= term RENAME attribute AS attribute

term 
	::= relation | ( expression )

restriction
	::= term WHERE comparison

projection 
	::= term | term [ attribute-commalist ]

attribute-commalist
	::= attribute | attribute , attribute-commalist

two-relation-expression
	::= projection binary-operation expression

binary-operation
	::= UNION | INTERSECT | MINUS | TIMES | JOIN | DIVIDEBY

comparison
	::= attribute compare number

compare
	::= < | > | <= | >= | = | <>

number
	::= val | val number

val 
	::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

attribute 
	::= CNO | CITY | CNAME | SNO | PNO | TQTY | 
		  SNAME | QUOTA | PNAME | COST | AVQTY |
		  S# | STATUS | P# | COLOR | WEIGHT | QTY

relation 
	::= S | P | SP | PRDCT | CUST | ORDERS

-----------------------------------------------------------

Shar the .l file (for lex), the .y (for yacc) file, typescript,
documentation and makefile only (no y.tab.c or lex.yy.c files).
I should type "make" to cause the program to compile
all appropriate portions (lex/flex fn.l and yacc/bison fn.y and cc
fn.c ...) to an executable called p3.

Program output should be one of two messages "ACCEPT"
or "REJECT".

Use turnin fn ree4620_3

Your project will be invoked with p3 test_file
