#include <cstdio>
using namespace std;
int main(){
	int n;
	scanf("%d",&n);
	int t,c,last = 0;
	int max = 0,cur = 0;
	for(int i = 0;i < n;i++){
		scanf("%d%d",&t,&c);
		if(last != 0)
			cur -= (t - last);
		if(cur < 0)
			cur = 0;
		cur += c;
		last = t;
		if(max < cur)
			max = cur;
	}
	printf("%d %d\n",cur + t,max);
	return 0;
}
