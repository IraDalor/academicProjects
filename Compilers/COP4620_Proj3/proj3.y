%{
#include <stdio.h>
#include <stdlib.h>
extern yylex();
extern yytext[];
extern FILE *yyin;
%}
%start start
%token DIGIT COMMA LBRACK RBRACK LPAR RPAR LTGT LTEQ GTEQ LT GT EQ RENAME AS WHERE UNION INTERSECT 
%token MINUS TIMES JOIN DIVIDEBY CNO CITY CNAME SNO PNO TQTY SNAME COST AVQTY SPOUND STATUS PPOUND
%token COLOR WEIGHT QTY S P SP PRDCT CUST ORDERS PNAME QUOTA
%%
start                      : expression                                {
                                                    // printf("ACCEPT\n") 
                                                                       };
expression                 : one_relation_expression                   {
                                                                       };
                           | two_relation_expression                   {
                                                                       };
one_relation_expression    : renaming                                  {
                                                                       };
                           | restriction                               {
                                                                       };
                           | projection                                {
                                                                       };
renaming                   : term RENAME attribute AS attribute        {
                                                                       };
term                       : relation                                  {
                                                                       };
                           | LPAR expression RPAR                      {
                                                                       };
restriction                : term WHERE comparison                     {
                                                                       };
projection                 : term                                      {
                                                                       };
                           | term LBRACK attribute_commalist RBRACK    {
                                                                       };
attribute_commalist        : attribute                                 {
                                                                       };
                           | attribute COMMA attribute_commalist       {
                                                                       };
two_relation_expression    : projection binary_operation expression    {
                                                                       };
binary_operation           : UNION                                     {
                                                                       };
                           | INTERSECT                                 {
                                                                       };
                           | MINUS                                     {
                                                                       };
                           | TIMES                                     {
                                                                       };
                           | JOIN                                      {
                                                                       };
                           | DIVIDEBY                                  {
                                                                       };
comparison                 : attribute compare number                  {
                                                                       };
compare                    : LT                                        {
                                                                       };
                           | GT                                        {
                                                                       };
                           | LTEQ                                      {
                                                                       };
                           | GTEQ                                      {
                                                                       };
                           | EQ                                        {
                                                                       };
                           | LTGT                                      {
                                                                       };
number                     : val                                       {
                                                                       };
                           | val number                                {
                                                                       };
val                        : DIGIT                                     {
                                                                       };
attribute                  : CNO                                       {
                                                                       };
                           | CITY                                      {
                                                                       };
                           | CNAME                                     {
                                                                       };
                           | SNO                                       {
                                                                       };
                           | PNO                                       {
                                                                       };
                           | TQTY                                      {
                                                                       };
                           | SNAME                                     {
                                                                       };
                           | QUOTA                                     {
                                                                       };
                           | PNAME                                     {
                                                                       };
                           | COST                                      {
                                                                       };
                           | AVQTY                                     {
                                                                       };
                           | SPOUND                                    {
                                                                       };
                           | STATUS                                    {
                                                                       };
                           | PPOUND                                    {
                                                                       };
                           | COLOR                                     {
                                                                       };
                           | WEIGHT                                    {
                                                                       };
                           | QTY                                       {
                                                                       };
relation                   : S                                         {
                                                                       };
                           | P                                         {
                                                                       };
                           | SP                                        {
                                                                       };
                           | PRDCT                                     {
                                                                       };
                           | CUST                                      {
                                                                       };
                           | ORDERS                                    {
                                                                       };
%%
int main(int argc, char *argv[])
{
    yyin = fopen(argv[1], "r");
    if (!yyin)
    {
        printf("File not found\n");
        exit(0);
    }
    yyparse();
    printf("ACCEPT\n");
}
yyerror()
{
    printf("REJECT\n");
    exit(0);
}
yywrap()
{
}
