#include <cstdio>
int card[125];
int main()
{
    int n;
    char c;
    scanf("%d",&n);
    for(int i=0; i<n; i++)
    {
        scanf(" %c",&c);
        card[c]++;
    }
    if(card['G']==n || card['R']==n || card['B']==n)
        printf("%c",c);
    else
    {
        if((card['G']>0 && card['R']>0)|| card['R']>1 || card['G']>1 )
            printf("B") ;
        if((card['B']>0 && card['R']>0)|| card['R']>1 || card['B']>1 )
            printf("G") ;
        if((card['G']>0 && card['B']>0)|| card['B']>1 || card['G']>1 )
            printf("R") ;
    }
    return 0;
}
