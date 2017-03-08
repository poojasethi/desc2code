//code chef Retail Shop
#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <tr1/unordered_map>
#include <ctime>
#include <cctype>
#include <cmath>

using namespace std;

vector<int> variation;
vector<vector<int> > allPerms;

void perm(vector<int> &indexes,map<int,bool> &m)
{	
	bool done = true;
	for(int i=0;i<indexes.size();i++){
		if(!m[indexes[i]]){
			done = false;
			m[indexes[i]] = true;
			variation.push_back(indexes[i]);
			perm(indexes,m);
			variation.pop_back();
			m[indexes[i]] = false;
		}
	}

	if(done){
		allPerms.push_back(variation);
	}
}

vector<vector<int> > getPerm(vector<int> &indexes)
{	
	map<int,bool> m;
	perm(indexes,m);
	return allPerms;
}

int findMax(vector<int> indexes,vector<vector<int> > &a,int t [10][10])
{
	int maxPoints = 0;
	for(int row=0;row<a.size();row++)
	{	
		int totalPoints = 0;
		for(int col=0;col<a[row].size();col++)
		{
			totalPoints += t[a[row][col]][indexes[col]];
		}
		maxPoints = max(maxPoints,totalPoints); 
	}
	return maxPoints;
}

int main(){
	int t [10][10] = {
		{55,60,4,25,18,10,12,8,11,50},
		{60,45,75,23,27,20,24,7,33,12},
		{4,75,78,32,36,30,36,6,12,65},
		{25,23,32,15,45,40,48,5,14,23},
		{18,27,36,45,54,50,60,4,15,12},
		{10,20,30,40,50,60,72,3,32,34},
		{12,24,36,48,60,72,84,2,23,34},
		{8,7,6,5,4,3,2,1,34,123},
		{11,33,12,14,15,32,23,34,65,48},
		{50,12,65,23,12,34,34,123,48,71}
	};
	int caseNum;
	cin >> caseNum;
	//cout << "t1" << endl; 
	for(int i=0;i<caseNum;i++)
	{
		vector<int> items;
		variation.clear();
		allPerms.clear();
		for(int j=0;j<10;j++){
			int num;
			cin >> num;
			items.push_back(num);
		}
		//cout << "t2" << endl; 
		vector<int> wish;
		vector<int> indexes;
		for(int j=0;j<10;j++){
			int bit;
			cin >> bit;
			wish.push_back(bit);
			if(bit){
				indexes.push_back(j);
			}
		}
		//cout << "t3" << endl; 
		//create all possible permutation of indexes
		vector<vector<int> > allperms = getPerm(indexes);
		//cout << "t4" << endl; 
		int max = findMax(indexes,allPerms,t);
		cout << max << endl;
	}



	return 0;
}


