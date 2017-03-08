#include<iostream>
#include<vector>
#include<algorithm>

#define MAX 1000*100+5
using namespace std;
int prev[MAX];
int type[MAX];
int cntfrom[MAX];


int main() { 
int n;
cin>>n;
for(int i=0;i<n;++i) cin>>type[i];


for(int i=0;i<n;++i) { 
cin>>prev[i];

prev[i]--;
if(prev[i]!=-1) 
cntfrom[prev[i]]++;


}

vector<int>ans;

for(int i=0;i<n;++i) {  

if(type[i]==1) { 

	int curv=i;
	vector<int>cur;
	while(prev[curv]!=-1 && cntfrom[prev[curv]]<=1) { 
		cur.push_back(curv);
		curv=prev[curv];
	}
	cur.push_back(curv);
	if(ans.size()<cur.size())
		ans=cur;
	}
	
}

cout<<ans.size()<<endl;
reverse(ans.begin(),ans.end());
for(int i=0;i<ans.size();++i) { 

if(i) cout<<" ";
cout<<ans[i]+1;

}
cout<<" ";

return 0;
}
