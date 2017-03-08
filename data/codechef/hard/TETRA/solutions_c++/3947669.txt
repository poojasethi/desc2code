#include <iostream>
#include <stdio.h>
#include <cmath>
using namespace std;

double SQ(double a)
{
  return (a)*(a);
}
 
 
int main(int argc, char const *argv[])
{
	int testcases;
	cin >> testcases;
	for (int i = 0; i < testcases; ++i)
	{
		double a,b,c,d,e,f;
		cin>>a>>c>>b>>e>>d>>f;
		double total_vol,area1,area2,area3,area4;
		double s1,s2,s3,s4,r;
		s1=(a+b+d)/2.0;
		s2=(d+e+f)/2.0;
		s3=(b+f+c)/2.0;
		s4=(a+e+c)/2.0;
		area1 = sqrt(s1*(s1-a)*(s1-b)*(s1-d));
		area2 = sqrt(s2*(s2-d)*(s2-e)*(s2-f));
		area3 = sqrt(s3*(s3-b)*(s3-f)*(s3-c));
		area4 = sqrt(s4*(s4-a)*(s4-e)*(s4-c));
		double area_sum = area1+area2+area3+area4 ;
		

		//r = sqrt(abs(a*f*(b-a+c+d+e-f) + b*e*(a-b+c+d-e+f) + c*d*(a+b-c-d+e+f) - (a+f)*(b+e)*(c+d)/2.0 - (a-f)*(b-e)*(c-d)/2.0 ))/12.0;
		r = sqrt(
           (4*SQ(b)*SQ(d)*SQ(f)
            -SQ(b)*SQ(SQ(d)+SQ(f)-SQ(e))
            - SQ(d)*SQ(SQ(f)+SQ(b)-SQ(c))
            - SQ(f)*SQ(SQ(b)+SQ(d)-SQ(a)) 
            + (SQ(d)+SQ(f)-SQ(e))
              *(SQ(f)+SQ(b)-SQ(c))
              *(SQ(b)+SQ(d)-SQ(a))
           ))/12.0;

		printf("%.4lf\n",r*3.0/area_sum);
	}
	return 0;
}