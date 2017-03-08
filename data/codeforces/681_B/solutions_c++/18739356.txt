#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
		int n;
		cin>>n;
		for(int a = 0; a <= n; a+= 1234567){
			for(int b=0; b <= n - a; b+= 123456){
				if(((n-a-b) % 1234) == 0){
					cout<<"YES"<<endl;
					return 0;
				}
			}
		}
		cout<<"NO"<<endl;
	return 0;
}
