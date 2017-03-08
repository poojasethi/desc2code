#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
const int MAX = 100001;
ll pows[MAX],m;
pair<ll,ll> ans;
pair<ll,ll> solve (ll M)
{
	if(!M)
		return make_pair(0,0);
	pair<ll,ll> a1,a2;
	ll a = upper_bound(pows,pows+MAX,M) - pows -1;
	a1 = solve (M-pows[a]);
	a2 = solve (pows[a] - pows[a-1] - 1);
	a1.first++;
	a2.first++;
	a1.second+=pows[a];
	a2.second+=pows[a-1];
	return max(a1,a2);
}
int main()
{
	for(int i=0;i<MAX; i++)
		pows[i] = 1ll*i*i*i;
	cin>>m;
	ans = solve(m);
	cout<<ans.first<<" "<<ans.second<<endl;
}
