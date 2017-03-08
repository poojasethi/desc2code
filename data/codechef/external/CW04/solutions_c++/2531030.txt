/* bhupkas */

/* Code for generating all permutations of a string */

#include "iostream"
#include "stdio.h"
#include "string.h"
#include "string"

using namespace std;

#define FOR(i,a,b)		for(i=a;i<b;i++)

void permute(string str,int i,int n)
	{
		if(i==n-1)		cout<<str<<endl;
		int j;
		FOR(j,i,n)
			{
				swap(str[i],str[j]);
				permute(str,i+1,n);
				swap(str[i],str[j]);
			}
	}

int main()
	{
		string str;
		cin>>str;
		int si=str.size();
		permute(str,0,si);
		return 0;
	}