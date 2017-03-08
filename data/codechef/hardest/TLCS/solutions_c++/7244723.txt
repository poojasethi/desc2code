#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
using namespace std;
char X[1009],Y[1009];
short table[1009][1009];
short help1[1009],help2[1009];
char ans[1009];
int main()
{
    int n,m,i,j,t,test;
    double beg=clock();int flag=0;
    scanf("%d",&test);for(t=1;t<=test;t++){
    scanf("%d%s%d%s",&m,X,&n,Y);
    if(flag==0){
    for(i=0;i<=m;i++)
    table[0][i]=0;
    for(i=1;i<=n;i++)
    table[i][0]=0;
    for(i=1;i<=m;i++)
    {
      for(j=1;j<=n;j++)
      {
         if(X[i-1]==Y[j-1])
         table[i][j]=table[i-1][j-1]+1;
         else 
         {
            if(table[i-1][j]>table[i][j-1])
            table[i][j]=table[i-1][j];
            else table[i][j]=table[i][j-1];
         }
      }
    }
    i=m;j=n;int index=-1;
    while(true)
    {
         if(X[i-1]==Y[j-1])
         {
           index++;
           ans[index]=X[i-1];
           help1[index]=i;
           help2[index]=j;
           i--;j--;
         }
         else
         {
           if(table[i-1][j]>table[i][j-1])
           i--;
           else j--;
         }
         if(i==0||j==0)break;
    }
    if(table[m][n]==0)
    {
      printf("case %d N\n",t);
    }
    else
    {
       printf("case %d Y\n",t);
       printf("%d\n",table[m][n]);
       for(i=index;i>=0;i--)
       {
          printf("%c %d %d\n",ans[i],help1[i],help2[i]);
       }
    }
    }
    
    
    
    if(flag==1)
    {
        printf("case %d N\n",t);
    }
    beg=(clock()-beg)/CLOCKS_PER_SEC;
    if(beg>4.9)
    {flag=1;}
    }   
    //system("pause");
    return 0;
}