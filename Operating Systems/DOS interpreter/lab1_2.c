#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char cmd [540];
    char arg1[260];
    char arg2[260];
    
    while(1)
    {
        printf("\nCommand (Type Ctrl-C to exit): ");
        scanf("%s", cmd);
        
        if (strcmp(cmd, "cd") == 0)
        {
            printf("\nEnter directory name (enter ../ for parent): ");
            scanf("%s", arg1);
            strcat(cmd, " ");
            strcat(cmd, arg1);
            system(cmd);
            continue;
        }
        else if (strcmp(cmd, "dir") == 0)
        {
            system("ls");
            continue;
        }
        else if (strcmp(cmd, "type") == 0)
        {
            printf("\nEnter file to cat: ");
            scanf("%s", arg1);
            strcpy(cmd, "cat ");
            strcat(cmd, arg1);
            system(cmd);
            continue;
        }
        else if (strcmp(cmd, "del") == 0)
        {
            printf("\nEnter file to delete: ");
            scanf("%s", arg1);
            strcpy(cmd, "rm ");
            strcat(cmd, arg1);
            system(cmd);
            continue;
        }
        else if (strcmp(cmd, "ren") == 0)
        {
            printf("\nEnter file to move: ");
            scanf("%s", arg1);
            printf("\nEnter destination: ");
            scanf("%s", arg2);
            strcpy(cmd, "mv ");
            strcat(cmd, arg1);
            strcat(cmd, " ");
            strcat(cmd, arg2);
            system(cmd);
            continue;
        }
        else if (strcmp(cmd, "copy") == 0)
        {
            printf("\nEnter file to copy: ");
            scanf("%s", arg1);
            printf("\nEnter destination: ");
            scanf("%s", arg2);
            strcpy(cmd, "cp ");
            strcat(cmd, arg1);
            strcat(cmd, " ");
            strcat(cmd, arg2);
            system(cmd);
            continue;
        }
        else
        {
            printf("\nInvalid input");
            printf("\nValid inputs: cd, dir, type, del, ren and copy");
            continue;
        }
    }
}