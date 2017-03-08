#include<iostream>
#include<map>
#include<cstdio>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<cmath>
#include<climits>

using namespace std;
#define EPS (double)1e-6

int n,a,b,c;
int p[2007][2];

double gety(double x)
{
  return (double)((-1.0)*((((double)a*x)+(double)c)/(double)b));
}

double gd(double x,double y)
{
  double res=0.0;

  for(int i=0;i<n;i++)
    {
      res+=sqrt((y-p[i][1])*(y-p[i][1])+(x-p[i][0])*(x-p[i][0]));
    }
  return res;
}

double ter_srch(double l,double r)
{

  double m1,m2;
  double fm1,fm2;
  double m1y,m2y;

  while(r-l>EPS)
    {
  m1=l+(r-l)/3;
  m2=l+2*(r-l)/3;

  m1y=gety(m1);
  m2y=gety(m2);



  fm1=gd(m1,m1y);
  fm2=gd(m2,m2y);


  if(fm1<fm2)
    r=m2;
  else if(fm1>fm2)
    l=m1;
  else
    {l=m1;r=m2;}

    }

  return gd((m1+m2)/2,(m1y+m2y)/2);
}



int main()
{
  int t;
  scanf("%d",&t);

  for(int tt=0;tt<t;tt++)
    {

      scanf("%d",&n);
      scanf("%d %d %d",&a,&b,&c);

      
      for(int i=0;i<n;i++)
	scanf("%d %d",&p[i][0],&p[i][1]); 

      double res;
      res=ter_srch(-5000.00,5000.00);

      printf("%.6f\n",res);

    }



  return 0;
}
