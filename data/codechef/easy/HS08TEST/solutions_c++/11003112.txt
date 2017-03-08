#include <iostream>
#include<iomanip>

using namespace std;



int main()
{
	float a,b;
	float A,B;
	cin>>a>>b;
	if((int(a)%5==0&&a+0.5<=b))
	{
		a+=0.5;}
		else a=0.0;
	cout<<fixed<<setprecision(2)<<b-a<<endl;
}