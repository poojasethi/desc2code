#include <cstdio>
#include <cstring>
using namespace std;
int main(){
	int n,a[101],ans,i;
	while(scanf("%d",&n)!=EOF){
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(ans=i=0;i<n;i++){
			if(a[i]||!a[i]&&i>0&&a[i-1]&&i<n-1&&a[i+1]) ans++;
		}
		printf("%d\n",ans);
	}
}