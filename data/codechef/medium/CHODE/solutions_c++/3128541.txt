/* bhupkas */

#include "bits/stdc++.h"

using namespace std;

bool cmp(pair <int , int > p1 , pair < int , int > p2)
{
	if(p1.first == p2.first)	return p1.second < p2.second;
	return p1.first < p2.first;
}

int main()
{
	string str1,str2;
	int t;
	cin >> t;
	int A[30];
	vector < pair < int , int > > v;
	map < char , char > mymap;
	while(t--)
	{
		v.clear();
		str1.clear() , str2.clear();
		mymap.clear();
		cin >> str1;
		getchar();
		getline(cin,str2);
		for(int i = 0 ; i < 26 ; i++)	A[i] = 0;
		for(int i = 0 ; i < str2.size() ; i++)	
		{
			if(str2[i] >= 'a' && str2[i] <= 'z')	A[str2[i] - 'a']++;
			else if(str2[i] >= 'A' && str2[i] <='Z')	A[str2[i] - 'A']++;
		}
		for(int i = 0 ; i < 26 ; i++)	v.push_back(make_pair(A[i],i));
		sort(v.begin(),v.end(),cmp);
		for(int i = 0 ; i < 26 ; i++)	mymap[v[i].second + 'a'] = str1[i];
		for(int i = 0 ; i < str2.size() ; i++)
		{
			if(str2[i] >= 'a' && str2[i] <= 'z')		cout << mymap[str2[i]];
			else if(str2[i] >= 'A' && str2[i] <='Z')	cout << (char)(mymap[str2[i] - 'A' + 'a'] - 'a' + 'A');
			else						cout << str2[i];
		}
		cout << endl;
	}
	return 0;
}
