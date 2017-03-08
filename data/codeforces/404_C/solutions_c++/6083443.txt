#include<iostream>
#include<vector>
#include<cmath>
#define MAX 100005
using namespace std;
long long n, k, dist, nivel;
vector<int> V[MAX];

int main(){
	cin>>n>>k;
	
	for(int i = 1; i <= n; i++){
		cin>>dist;
		V[dist].push_back(i);
		nivel = max(dist ,nivel);
	}
	
	if(V[0].size() != 1) cout<<-1<<endl;
	else{
		bool f = 1;
		
		if(V[1].size() > k) f = 0;
		
		for(int i = 2; i <= nivel; i++){
			if(V[i].size() > V[i - 1].size()*(k - 1)){
				f = 0;
				break;
			}
		}
		
		if(!f) cout<<-1<<endl;
		else{
			cout<<n - 1<<endl;
			
			for(int i = 0; i < V[1].size(); i++){
				cout<<V[0][0]<<" "<<V[1][i]<<endl;
			}
			
			for(int i = 2; i <= nivel; i++){
				for(int j = 0; j < V[i].size(); j++){
					cout<<V[i - 1][j / (k - 1)]<<" "<<V[i][j]<<endl;
				}
			}
		}
	}
	
	return 0;
}