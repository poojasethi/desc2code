#include <iostream>

using namespace std;

int main(){
	long long a,b,c,w,x;
	cin>>a>>b>>w>>x>>c;
	long long answer=0;
	long long s,y;
	s=w-x;
	y=c-a;
	if(y>0)
		answer=(y*x-b+s-1)/s+y;
	cout<<answer<<endl;
}
