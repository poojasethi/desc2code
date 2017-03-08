//Author : pakhandi
 
#include<stdio.h>
 
int main()
{
    int cases, n;
    scanf("%d",&cases);
    while(cases--)
    {
              scanf("%d",&n);
              if(n&1)
                printf("Lannisters always pays their debts\n");
              else
                printf("Valar Morghulis\n");
    }
    return 0;
} 