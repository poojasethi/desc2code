#include <iostream>
#include <string>

using namespace std;

int main()
{
	string a = "<3",b;
    	int n,i,k = 0;
    	cin>>n;
    	for(i = 0; i < n; i++){
        	cin>>b;
       	 	a += b+"<3";
    	}
    	cin>>b;
    	for(i = 0;i < b.size(); i++){
        	if(a[k] == b[i]) 
            	k++;
    	}
    	cout<<((k == a.size())?"yes":"no");
}
