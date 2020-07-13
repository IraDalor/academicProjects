Specifications for the DOS interpreter project are as follows, the project functioned as expected per specification:

Write a program in C which functions as a DOS command interpreter. 

DOS uses the commands cd, dir, type, del, ren, and copy to do the same functions as the UNIX commands cd, ls, cat, rm, mv, and cp. 

Your program loops continuously, allowing the user to type in DOS commands, which are stored in the variables command, arg1 and arg2. 
The command should be considered by a case statement, which executes an appropriate UNIX command, depending on which DOS command has 
been given. 

The program should echo the following instruction to the user: Type Ctrl-C to exit.
