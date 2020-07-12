Both projects 1 and 2 function as expected.

SPECIFICATIONS FOR PROJECT 1:
Your project is to use the grammar definition in the appendix
of your text to guide the construction of a lexical analyzer. 
The lexical analyzer should return tokens as described. Keep 
in mind these tokens will serve as the input to the parser.

Page 491 and 492 should be used to guide the construction of the
lexical analyzer. A few notable features:
0) the project's general goal is to construct a list of tokens capable
   of being passed to a parser.
1) comments should be totally ignored, not passed to the parser and
   not reported.
2) one line comments are designated by //
3) multiple line comments are designated by /* followed by */ in 
   a match up fashion for the nesting.

Appropriate documentation as described in the Syllabus should 
be included. A shar file, including all files necessary, 
(makefile, source files, test files, documentation file
("text" in ascii format), and any other files) should be submitted 
by the deadline using turnin as follows:

   turnin fn ree4620_1

By my typing    make    after unsharing your file, I should see an
executable called anything but p1, 

The analyzer will be invoked with:

   p1 test_fn

where p1 is the scirpt that will execute your scanner and
test_fn is the test filename upon which lexical analysis is to be 
done. You must supply a makefile for any language you chose to use,
including scripting languages. 

If you write in any language, you must supply at p1 file 
that will execute your program.
For example, such a p1 file might appear as:

#!/bin/ksh
ruby your_ruby_script $1

OR

#!/bin/ksh
java your_java_pgm $1

OR

#!/bin/ksh
python your_python_script $1

OR

#!/bin/ksh
yourpgmname $1

Note that turnin will report the 2 day late date, if the project
is submitted on this date the penalty will be assessed.

The shar file can be created as follows:

shar fn1 fn2 fn3 fn4 > fn

You should NOT shar a directory, i.e. when I unshar your project
a new subdirectory should not be created.

You should test the integrity of your shar by: 
1)copying your shar to a temporary directory, 
2)unsharing, 
3)make, and 
4)execute to see that all files are present and that the 
project works appropriately. 

Failure to carefully follow these guidelines will result in penalty.
If you are not sure of some characteristic, ask to verify the 
desired procedure.

You should echo the input line followed by the output in a
sequential fashion.

Note: you may have an additional project assigned before this one is
due.

SAMPLE INPUT:
/****This**********/
/**************/
/*************************
i = 333;        ******************/       */

iiii = 3@33;

int g 4 cd (int u, int v)      {
if(v == >= 0) return/*a comment*/ u;
else ret_urn gcd(vxxxxxxvvvvv, u-u/v*v);
       /* u-u/v*v == u mod v*/
!
}

return void while       void main()

!=

SAMPLE OUTPUT:
INPUT: /****This**********/
INPUT: /**************/
INPUT: /*************************
INPUT: i = 333;        ******************/       */
*  
/  
INPUT: iiii = 3@33;
ID: iiii 
=
INT: 3
Error: @33
;

INPUT: int g 4 cd (int u, int v)      {
KW: INT
ID: g
INT: 4
ID: cd
(
KW: INT
ID: u
,
KW: INT
ID: v
)
{

INPUT: if(v == >= 0) return/*a comment*/ u;
KW: if
(
ID: v
==
>=
INT: 0
)
KW: return
ID: u
;

INPUT: else ret_urn gcd(vxxxxxxvvvvv, u-u/v*v);
KW: else
ID: ret
Error: _urn
ID: gcd
(
ID: vxxxxxxvvvvv
,
ID: u
-
ID: u
/
ID: v
*
ID: v
)
;
INPUT: /* u-u/v*v == u mod v*/

INPUT: !   
Error: !
INPUT: }
}
INPUT: return void while       void main()
KW: return
KW: void
KW: while
KW: void
ID: main
(
)

INPUT: !=
!=

SPECIFICATION FOR PROJECT 2:
Your project is to use the grammar definition in the appendix
of your text to guide the construction of a recursive descent parser.
The parser should follow the grammar as described in A.2 page 492.

Upon execution, your project should report 

ACCEPT

or 

REJECT

exactly. Failure to print ACCEPT or REJECT appropriately will
result penalty for the test file. 

Appropriate documentation as described in the Syllabus should 
be included. A shar file, including all files necessary, 
(makefile, source files, test files, documentation file
(p2.txt in ascii format), and any other files) should be submitted 
by the deadline using turnin as follows:

   turnin fn ree4620_2

By my typing    make    after unsharing your file I should see an
executable called p2 (if you did your project in C) that will 
perform the syntax analysis. The analyzer will be invoked with:

   p2 test_fn

where p2 is the executable resulting from the make command 
(if done in C or C++) or is a script that executes your project (if
done in anyother language) and test_fn is the test filename upon 
which parsing is to be done. You must supply a makefile for any 
language. If your project is written in a pure interpreter (python, 
ruby, perl, etc.), provide a makefile and indicate such. 
(that is,  print "No makefile necessary" from your makefile).

Note that turnin will report the 2 day late date, if the project
is submitted on this date a penalty will be assessed.

Thus, the makefile might be (as needed for python):

-------------------------------------------------
all:
	@echo "no makefile necessary, project in python"
-------------------------------------------------

the p1 script would then be:

-------------------------------------------------
#!/bin/bash
python myprj.py $1
-------------------------------------------------

The shar file can be created as follows:

shar makefile p1 myprj.py p2.txt  > fn

You should not shar a directory, ie when I unshar your project
a new subdirectory should not be created.

You should test the integrity of your shar by copying it to a
temporary directory, unsharing, make, and execute to see that
all files are present and that the project works
appropriately.

Note: you may have an additional project assigned before this one is
due.

You must enhance your symbol table in preparation for the semantic
analysis project (Project 4). You do not need to print the table.

You do not need to do error recovery, upon detection of the error,
simply report such and stop the program.
