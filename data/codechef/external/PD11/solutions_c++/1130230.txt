#include<stdio.h>

int compare(char x[],char y[])
{
   int i,j; for(i=0;x[i]!='\0';i++)
    {
        if(x[i]!=y[i]){return 1;}
    }
    return 0;
};
int main()
{
    int n,m,i,j,k,cnt,a[20000];
    char dna[20000][21],ch[21];
    while(1)
    {
        scanf("%d %d",&n,&m);
        if(n==0&&m==0){break;}
        for(i=0;i<n;i++)
        {a[i]=0;}
        for(i=0;i<n;i++)
        {
            scanf("%s",dna[i]);
        }
        for(j=0;j<n;j++)
        {
            if(dna[j][0]=='-'){continue;}
            cnt=0;
            for(k=0;k<m+1;k++)
            {ch[k]=dna[j][k];}

            for(i=0;i<n;i++)
            {
                if(compare(ch,dna[i])==0){cnt++;dna[i][0]='-';}
            }
            a[cnt-1]++;
        }
        for(j=0;j<n;j++)
        {
            printf("%d\n",a[j]);
        }
    }
    return 0;
}
