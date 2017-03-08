#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cassert>
using namespace std;
long long a[2222][103];
long long b[2222][103];
long long w[2222][103];
int vis[2222];
long long tmp[2222];
long long kmp[103];
int N;


int main(){
	string d;
	scanf("%d",&N);
	for(int i=0;i<N;++i){
		cin >> d;
		int k = d.size();
		for(int j=0;j<k;++j){
			tmp[k-j-1] = d[j]-'0';
		}
		for(int n=0;n<=70;++n){
			for(int j=k-1;j>0;--j){
				tmp[j-1] += (tmp[j] & ((1LL<<31)-1))*10LL;
				tmp[j] >>= 31;
			}
			a[i][n] = tmp[0] & ((1LL<<31)-1);
			tmp[0] >>= 31;
		}
		int D = 31*71-1;
		int idx = -1;
		bool maxbitset = false;
		for(int n=0;n<=70;++n) kmp[n] = 0;
		for(int n=70;n>=0;--n){
			//if(!a[i][n])continue;
			for(int j=30;j>=0;j--){
				long long p = a[i][n] & (1LL<<j);
				if(p){
					if(vis[D]){
						for(int m=0;m<=70;++m){
							a[i][m] ^= b[D][m];
							kmp[m] ^= w[D][m];
						}
					} else if(!maxbitset){
						idx = D;
						maxbitset = true;
					}
				}
				--D;
			}
		}
		/*
		bool ok = true;
		for(int n=0;n<=70;++n){
			if(a[i][n] & ((1LL << 31)-1)) {
				ok = false;
			}
			if(!ok)break;
		} 
		*/
		//if(ok){
		if(!maxbitset){
			int cntr = 0;
			for(int y=0;y<=70;++y){
				cntr += __builtin_popcountll(kmp[y]);
			}
			assert(cntr != 0);
			printf("%d", cntr);
			int xx = 0;
			for(int y=0;y<=70;++y){
				for(int u=0;u<=30;++u){
					if(kmp[y] & (1LL<<u)){
						cntr--;
						printf(" %d", xx);
					}
					++xx;
				}
			}
			assert(cntr==0);
			printf("\n");
		} else {
			assert(idx != -1);
			printf("0\n");
			for(int y=0;y<=70;++y){
				b[idx][y] = a[i][y];
			}
			for(int y=0;y<=70;++y){
				w[idx][y] = kmp[y];
			}
			w[idx][i/31] ^= (1LL << (i%31));
			vis[idx] = 1;
		}
	}
	return 0;
}