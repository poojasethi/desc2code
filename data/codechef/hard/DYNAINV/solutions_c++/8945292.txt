#include <bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

#define LSOne(i) (i & (-i))

class BIT{
private:
	vector<int> ft;
public:
	BIT(int n){
		ft.resize(n+1,0);
	}
	int query(int x){
		int s = 0;
		for(; x>0; x-=LSOne(x))
			s+=ft[x];
		return s;
	}
	int query(int x, int y){
		return query(y) - (x == 1 ? 0 : query(x-1));
	}
	void update(int k, int v){
		for(; k<ft.size(); k+=LSOne(k))
			ft[k] += v;
	}
};

int pre(int n){
	BIT* b = new BIT(n); int a; int ret = 0;
	for(int i=0;i<n;i++){
		cin >> a;
		ret += b->query(a,n);
		b->update(a,1);
	}
	return (ret&1);
}

int main(){
	int n,q,x,y;
	ios::sync_with_stdio(false);
	cin >> n >> q;
	int curr = pre(n);
	while(q--){
		cout << (++curr) % 2 << endl;
	}
	return 0;
}