#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
 
int main() {
	int t;
	cin>>t;
	while(t)
	{
	    int a=0,b=0;
    	string arr1;
    	cin >> arr1;
    	for(int i=0; arr1[i]!='\0'; i++)
    	{
    		if(arr1[i]=='a')
    			a++;
    		else if(arr1[i]=='b')
    			b++;
    	}
    	cout<< min(a,b) <<endl;
    	t--;
	}
	return 0;
}  