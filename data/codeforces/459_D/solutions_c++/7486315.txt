#include <cstdio>
#include <map>

using namespace std;
const int N = 1000006;
int a[N];
map<int, int > m,mm;
int bit[N];
int n;

void update(int idx, int val) {
	for(int i = idx; i < N; i += i & -i)
		bit[i] += val;
}

int query(int idx) {
	int res = 0;
	for(int i = idx; i; i -= i & -i)
		res += bit[i];
	return res;
}

int main(){
	scanf("%d",&n);
	for(int i=0;i<n;++i){
		scanf("%d",&a[i]);
	}
	for(int i=n-1;i>=0;--i){
		m[a[i]]++;
		update(m[a[i]],1);
	}	
	long long sum=0;
	for(int i=0;i<n;++i){
		update(m[a[i]],-1);
		m[a[i]]--;
		mm[a[i]]++;
		sum+=query(mm[a[i]]-1);

	}
	printf("%lld\n",sum);
	return 0;
}
