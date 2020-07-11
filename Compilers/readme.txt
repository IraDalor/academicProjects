This is a series of projects done in python for my compilers course taken in Spring of 2020 at University of North Florida with Dr.Eggen.

There are 5 projects total, of which I have uploaded the last four for the sake of simplicity. Each projects cummulatively builds upon the last, adding a new
component with each iteration. Rules of the grammar used will be listed below. Project requirements will be placed in readme files in each folder for each
respective project, with porject 2 folder containing the requirements for both the first and second projects.

The projects are all implimented in python and the components built are as follows:

Project 1: Lexical Analyzer
Project 2: Syntax Analyzer
Project 3: An Exercise Using Lex and YACC
Project 4: Semantic Analysis
Project 5: Code Generation

The grammar used (The language is a reduced version of C):

1. program → declaration-list
2. declaration-list → declaration-list declaration | declaration
3. declaration → var-declaration | fun-declaration
4. var-declaration → type-specifier ID ; | type-specifier ID [ NUM ] ;
5. type-specifier → int | void
6. fun-declaration → type-specifier ID ( params ) compound-stmt
7. params → param-list | void
8. param-list → param-list , param | param
9. param → type-specifier ID | type-specifier ID [ ]
10. compound-stmt → { local-declarations statement-list }
11. local-declarations → local-declarations var-declarations | empty
12. statement-list → statement-list statement | empty
13. statement → expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt
14. expression-stmt → expression ; | ;
15. selection-stmt → if ( expression ) statement | if ( expression ) statement else statement
16. iteration-stmt → while ( expression ) statement
17. return-stmt → return ; | return expression ;
18. expression → var = expression | simple-expression
19. var → ID | ID [ expression ]
20. simple-expression → additive-expression relop additive-expression | additive-expression
21. relop → <= | < | > | >= | == | !=
22. additive-expression → additive-expression addop term | term
23. addop → + | -
24. term → term mulop factor | factor
25. mulop → * | /
26. factor → ( expression ) | var | call | NUM
27. call → ID ( args )
28. args → arg-list | empty
29. arg-list → arg-list , expression | expression

Keywords: else if int return void while

Special symbols: + - * / < <= > >= == != = ; , ( ) [ ] { } /* */

ID = letter letter*
NUM = digit digit*
letter = a | .. | z | A | .. | Z
digit = 0 | .. | 9

Comments: /* ... */
