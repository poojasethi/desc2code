#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

long long a[4005], b[4005];
int r[2005][2005];
int N;
int main(){
	scanf("%d", &N);
	for(int i=0;i<N;++i){
		for(int j=0;j<N;++j){
			scanf("%d",&r[i][j]);
			a[i+j] += r[i][j];
			b[N-1+i-j] += r[i][j];
		}
	}
	long long x = -1, y = -1;
	int x1,x2,y1,y2;
	for(int i=0;i<N;++i){
		for(int j=0;j<N;++j){
			long long tmp = a[i+j] + b[N+i-1-j] - r[i][j];
			if((i+j)%2==0){
				if(tmp > x){
					x = tmp;
					x1 = i;
					y1 = j;
				}
			} else {
				if(tmp > y){
					y = tmp;
					x2 = i;
					y2 = j;
				}
			}
		}
	}
	cout << (x+y) << endl;
	printf("%d %d %d %d\n", x1+1, y1+1,x2+1,y2+1);
	return 0;
}