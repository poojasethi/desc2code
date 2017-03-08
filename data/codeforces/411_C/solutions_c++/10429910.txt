#include<stdio.h>
short i,def[4],atk[4],a1,d1;
main()
{
    for(i=0;i<4;i++)scanf("%hd %hd",&def[i],&atk[i]);
    if(atk[0]+def[1]>atk[1]+def[0])a1=atk[0],d1=def[1];
    else a1=atk[1],d1=def[0];
    if(atk[2]>d1&&def[3]>a1)printf("Team 2");
    else if(atk[3]>d1&&def[2]>a1)printf("Team 2");
    else if(atk[2]<d1&&atk[3]<d1&&def[2]<a1&&def[3]<a1)printf("Team 1");
    else printf("Draw");
}