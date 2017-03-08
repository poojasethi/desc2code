#include<bits/stdc++.h>
using namespace std;
int main()
{
	double a,v,w,l,d,s,t;
	cin>>a>>v;
	cin>>l>>d>>w;
	w=min(min(w,v),sqrt(2*a*d));
	if(w*w + 2*a*d > 2*v*v)
		t=(2*v - w)/a + (d- (v*v)/a + (w*w)/(2*a))/v;
	else
		t=(2*sqrt(a*d + (w*w)/2))/a - w/a;
	s=(v*v - w*w)/(2*a);
	l=l-d;
	if(s<l)
		t+=(v - w)/a + (l - s)/v;
	else
		t+=(-w + sqrt(w*w + 2*a*l))/a;
	printf("%.12lf\n",t);
	return 0;
}
