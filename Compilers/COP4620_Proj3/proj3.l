%{
#include "proj3.tab.h"
extern int yylval;
void lexerror();
%}
Newline       [\r\n]
Delimiter     [ \t]
Whitespace    {Delimiter}+
Digit         [0-9]
%%
{Newline}        ;
{Delimiter}      ;
{Whitespace}     ;
{Digit}          {return(DIGIT);}
","              {return(COMMA);}
"["             {return(LBRACK);}
"]"             {return(RBRACK);}
"("             {return(LPAR);}
")"             {return(RPAR);}
"<>"             {return(LTGT);}
"<="             {return(LTEQ);}
">="             {return(GTEQ);}
"<"              {return(LT);}
">"              {return(GT);}
"="              {return(EQ);}
"RENAME"         {return(RENAME);}
"AS"             {return(AS);}
"WHERE"          {return(WHERE);}
"UNION"          {return(UNION);}
"INTERSECT"      {return(INTERSECT);}
"MINUS"          {return(MINUS);}
"TIMES"          {return(TIMES);}
"JOIN"           {return(JOIN);}
"DIVIDEBY"       {return(DIVIDEBY);}
"CNO"            {return(CNO);}
"CITY"           {return(CITY);}
"CNAME"          {return(CNAME);}
"SNO"            {return(SNO);}
"PNO"            {return(PNO);}
"TQTY"           {return(TQTY);}
"SNAME"          {return(SNAME);}
"QUOTA"          {return(QUOTA);}
"PNAME"          {return(PNAME);}
"COST"           {return(COST);}
"AVQTY"          {return(AVQTY);}
"S#"             {return(SPOUND);}
"STATUS"         {return(STATUS);}
"P#"             {return(PPOUND);}
"COLOR"          {return(COLOR);}
"WEIGHT"         {return(WEIGHT);}
"QTY"            {return(QTY);}
"S"              {return(S);}
"P"              {return(P);}
"SP"             {return(SP);}
"PRDCT"          {return(PRDCT);}
"CUST"           {return(CUST);}
"ORDERS"         {return(ORDERS);}
.                {lexerror();}
%%
void lexerror(){
    printf("REJECT\n");
    exit(0);
}
