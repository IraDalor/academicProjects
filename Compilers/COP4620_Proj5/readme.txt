Project 5 did not work as expected when tested by the professor, but passed all automated test cases before it was submitted for grading.
I continue to tinker witht he project when I have free time and a future update is likely simply for the accomplishment of having a working
front end for a C- compiler built entirely in python.

Intermediate Code Generation

You should generate simple quadruples as explained in class and shown
below.  When  you generate simple quadruples you should use the operators 
as described in class.

Your project should be shar'd containing a makefile, source file, doc
file, and typescript (showing your testing). The makefile file should
be invoked with "make" creating an executable of p5. Your project will
be invoked with p5 fn1 where fn1 is the program file to be analyzed.
The intermediate code should be written to the screen. Of course, fn1 fn2
will be any name of my chosing.

This project must be complete in that the lexical analyzer and
parser must be included to create the parse tree as required.

Use turnin for submission as

turnin fn ree4620_5

where fn is the shar'd file of your complete project.

----------------------------------------------------
Example test files and corresponding code generation:
----------------------------------------------------
----------------------------------------------------
Example 1

void main(void)
{
  int x;
  int y;
  int z;
  int m;
   while(x + 3 * y > 5)
   {
     x = y + m / z;
     m = x - y + z * m / z;
   }
}

----------------------------------------------------

1    func      main       void           0
2    alloc     4                         x
3    alloc     4                         y
4    alloc     4                         z
5    alloc     4                         m
6    mult      3         y              _t0  bpw = 6
7    add       x         _t0            _t1
8    comp      _t1       5              _t2
9    BRLEQ     _t2                      21   bpo = 9
10   block
11   div       m         z              _t3
12   add       y         _t3            _t4
13   assign    _t4                       x
14   sub       x         y              _t5
15   mult      z         m              _t6
16   div       _t6       z              _t7
17   add       _t5       _t7            _t8
18   assign    _t8                       m
19   end       block
20   BR                                 6   val of bpw
21   end            func           main     loc for bpo

----------------------------------------------------
----------------------------------------------------
Example 2

int sub(int z)
{
   if (x > y)
      return(z+z);
   else 
      x = 5;
}
void main(void)
{
  int x;
  int y;
  y = sub(x);
}


----------------------------------------------------

1    func       sub            int            1
2    param                                    z
3    alloc      4                             z
5    compr      x              y              t23
6    brle       t23                           10   bpe = 6
7    add        z              z              _t0
8    return                                   _t0
9    br                                       11   bpo = 9
10   assgn                     5               x   val for bpe
11   end        func           sub                 val for bpo
12   func       main           void           0
13   alloc      4                             x
14   alloc      4                             y
15   arg                                      x              
16   call       sub            1             _t1
17   assign     _t1                           y
18   end        func           main

Example 3

void main(void)
{
   int x[10];
   int y;
   y = (x[5] + 2) * y;
}

----------------------------------------------------

1	func		main		void		0
2  alloc 	 			40			x
3	alloc 	 			4			y
4	disp		x			20			_t0
5  add   	_t0		2			_t1
6  mult     _t1      y        _t2
7	asign		_t2					y
8	end		func		main
