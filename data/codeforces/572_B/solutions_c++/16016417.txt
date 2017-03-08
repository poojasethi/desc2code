#include <bits/stdc++.h>

using namespace std;

const int MaxN=1E5+10;
int buy[MaxN],sell[MaxN];
vector <int> v;

int main(){
	int n,k;
	cin >> n >> k;
	for (int i=0;i<n;++i){
		char c;
		int kind,val;
		cin >> c >> kind >> val;
		if(c=='B')
			buy[kind]+=val;
		else
			sell[kind]+=val;
	}
	int cnt=0;
	for(int i=0;cnt<k && i<MaxN;++i)
		if(sell[i]!=0){
			v.push_back(i);
			++cnt;
		}
	for(int i=v.size()-1;i>=0;--i)
		cout << 'S' << " " << v[i] << " " << sell[v[i]] << endl;
	cnt=0;
	for(int i=MaxN-1;cnt<k && i>=0;--i)
		if(buy[i]!=0){
			cout << 'B' << " " << i << " " << buy[i] <<endl;
			++cnt;
		}
}