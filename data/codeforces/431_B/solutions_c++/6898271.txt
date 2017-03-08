#include<bits/stdc++.h>
using namespace std;
int main()
{
  int a[10]={0,1,2,3,4},b[10][10];
  for(int i=0;i<5;i++)
  for(int j=0;j<5;j++)
  cin>>b[i][j];
  int m=-1000000000,sum;
  do
  {
   sum=0;
   for(int i=0;i<4;i++)
    for(int j=i;j<5;j+=2)
    {
      if(j+1<5)
      sum+=(b[a[j]][a[j+1]]+b[a[j+1]][a[j]]);
    }
    m=max(sum,m);
  }while(next_permutation(a,a+5));
  cout<<m<<endl;
}
