#include <iostream>
#include <math.h>


using namespace std;


int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		double max_dist,x1,y1,x2,y2,x3,y3;
		cin>>max_dist;
		cin>>x1>>y1>>x2>>y2>>x3>>y3;
		double d1,d2,d3;
		d1=sqrt(pow(x2-x1,2)+pow(y2-y1,2));
		d2=sqrt(pow(x3-x1,2)+pow(y3-y1,2));
		d3=sqrt(pow(x3-x2,2)+pow(y3-y2,2));
		if(d1<=max_dist&&d2<=max_dist)
		{
			cout<<"yes"<<endl;
		}
		else if(d1<=max_dist&&d3<=max_dist)
		{
			cout<<"yes"<<endl;
		}
		else if(d2<=max_dist&&d3<=max_dist)
		{
			cout<<"yes"<<endl;
		}
		else
			cout<<"no"<<endl;
	}
}