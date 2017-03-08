#include <bits/stdc++.h>

using namespace std;

#define int long double

const int pi=acos(-1);

int ghadr(int x){
	return max(x,-x);
}

int32_t main(){
	int x1,y1,r1,x2,y2,r2;
	cin >> x1 >> y1 >> r1;
	cin >> x2 >> y2 >> r2;
	int dx=x1-x2;
	int dy=y1-y2;
	int d=sqrt(dx*dx+dy*dy);
	if (d>r1+r2){
		cout << 0;
		return 0;
	}
	if (d<=ghadr(r1-r2)){
		int r=min(r1,r2);
		cout << setprecision(15) << r*r*pi;
		return 0;
	}
	int x=2*acos((d*d+r1*r1-r2*r2)/(2*d*r1));
	int y=2*acos((d*d+r2*r2-r1*r1)/(2*d*r2));
	int ans1=(x*r1*r1-r1*r1*sin(x))/2;
	int ans2=(y*r2*r2-r2*r2*sin(y))/2;
	cout << setprecision(15) << ans1+ans2;
}