#include<iostream>
#include<stdio.h>
#include<vector>
#include<math.h>
#include<algorithm>
 
#define RIGSIZE 1000
#define x first
#define y second
#define INF 100000000
 
using namespace std;
 
float dist(pair <int,int>P1,pair <int,int>P2);
 
int main()
{
    int t, last,curr,trips,counter;
    float term;
    int w,n=-1,tempweight,cx,cy,r;
    bool C[RIGSIZE];
    pair <int,int> R[RIGSIZE];
    float food[RIGSIZE],d;
 
    scanf("%d",&t);
    for (int it=0;it<t;it++)
    {
        n=-1;
        r=0;
        scanf("%d",&w);
        do
        {
            scanf("%d",&tempweight);
            w-=tempweight;
            n++;
        }while(tempweight!=-1);
        w--;
        do
        {
            scanf("%d%d",&cx,&cy);
            R[r].x=cx;
            R[r].y=cy;
            r++;
        }while(!((cx==0)&&(cy==0)));
        r--;
        fill(food,food+r,(float)(INF));
        food[r-1]=0;
        fill(C,C+r,false);
        C[r-1]=true;
        last=r-1;
        counter=0;
        while(counter<r)
        {
            curr=0;
            if (C[0])
                break;
            for (int j=0;j<r-1;j++)
            {
                if (!C[j])
                {
                    d=dist(R[j],R[last]);
                    if (w-(d+n*d)>=food[last])
                        food[j]=min(n*d+food[last],food[j]);
                    else
                    {
                        term=w-(d+2*n*d);
                        if(term>0)
                           {
                              // printf("j:%d,%f,d:%f\n",j,((w-(n+1)*d)),d);
                                trips=(int)ceil((food[last]-(w-(n+1)*d))/term);
                             /*   printf("foodlast:%lf,j:%d,trips:%d\n",food[last],j,trips);
                                printf("thing:%lf\n",term);*/
                                food[j]=min((1+2*trips)*n*d+food[last],food[j]);
                           }
                    }
                    curr=food[curr]>food[j]?j:curr;
                }
            }
            //printf("curr %d\n",curr);
            C[curr]=true;
            last=curr;
            counter++;
        }
        if (food[0]>INF-5)
            printf("-1\n");
        else
            printf("%d\n",(int)ceil(food[0]));
    }
	return 0;
}
 
float dist(pair <int,int>P1,pair <int,int>P2)
{
     return (sqrt((P1.x-P2.x)*(P1.x-P2.x)+(P1.y-P2.y)*(P1.y-P2.y)));
}
 