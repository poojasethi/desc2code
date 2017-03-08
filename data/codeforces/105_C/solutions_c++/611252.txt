#include <stdlib.h>
#include <string.h>
#include <vector>
#include <map>
#include <list>
#include <map>
#include <set>
#include <fstream>
#include <iostream>
#include <queue>
#include <algorithm>
#include <sstream>
#include <limits.h>
#define _USE_MATH_DEFINES 
#include <math.h> 

#define pb(a) push_back(a) 
#define sz size()
#define ALL(a) a.begin(),a.end()
#define ALLR(a) a.rbegin(),a.rend()
#define X first
#define Y second

typedef long long ll;
typedef long double ld;

template<typename T> inline void SWAP(T &a, T &b){T tmp=a;a=b;b=tmp;}
template<typename T> inline T ABS(const T &val) {return val<0?-val:val;}
template<typename T> inline T MAX(const T &a, const T &b){return a>b?a:b;}
template<typename T> inline T MIN(const T &a, const T &b){return a<b?a:b;}

#define MSET(d) memset(d,0,sizeof(d))
#define forn(i,n) for(int i=0;i!=n;i++)
#define for1(i,n) for(int i=1;i<=n;i++)
#define forab(i,a,b) for(int i=a;i!=b;i++)
#define for1ab(i,a,b) for(int i=a+1;i<=b;i++)
#define fordab(i,a,b) for(int i=b-1;i>=a;i--)
#define ford1ab(i,a,b) for(int i=b;i!=a;i--)
#define ford(i,n) for(int i=n-1;i!=-1;i--)
#define ford1(i,n) for(int i=n;i!=0;i--)

const int INTinf=2147483647;
const int nINTinf=0-2147483648;
#define LLinf 9223372036854775807

using namespace std;
typedef pair<int, int> pii;
int bonus[3][11];

int sum;
struct resid{
	string name;
	int type;
	int param;
	resid(string name, char type, int param){
		this->name.assign(ALL(name));
		this->param=param;
		int tmp;
		switch(type){
			case 'g':
				tmp=0;
				break;
			case 's':
				tmp=1;
				break;
			case 'p':
				tmp=2;
				break;
		}
		this->type=tmp;
	}
};
bool comp(const resid *q, const resid *w){
	return q->param>w->param;
}
struct item {
	string name;
	int params[4], type;
	item(string name, int *params, char type){
		this->name.assign(ALL(name));
		forn(i,4) this->params[i]=params[i];
		int tmp;
		switch(type){
			case 'w':
				tmp=0;
				break;
			case 'a':
				tmp=1;
				break;
			case 'o':
				tmp=2;
				break;
		}
		this->type=tmp;
	}

	int getMax(){
		if (sum){
			return params[type]+bonus[type][params[3]];
		} else {
			int s=0;
			forn(i,resids.sz){
				if (type==resids[i]->type) s+=resids[i]->param;
			}
			return params[type]+s;
		}
	}
	vector<resid*> resids;
};
int n,m;
vector<item*> items[3];
vector<resid*> resids[3];
map<string, item*> MP;
string str, str1, str2;
int params[4];
int param;

int main(){
#ifdef _DEBUG
	freopen("input.txt","r",stdin);
#endif
	cin>>n;
	sum=0;
	forn(i,n){
		cin>>str>>str1>>params[0]>>params[1]>>params[2]>>params[3];
		sum+=params[3];
		item * tmpIt = new item(str, params, str1[0]);
		MP.insert(pair<string, item*>(str, tmpIt));
		items[tmpIt->type].pb(tmpIt);
	}
	cin>>m;
	forn(i,m){
		cin>>str>>str1>>param>>str2;
		resid *tmpR = new resid(str, str1[0], param);
		MP[str2]->resids.pb(tmpR);
		resids[tmpR->type].pb(tmpR);
	}
	sum=sum!=m;

	if (sum){
		forn(i,3){
			sort(ALL(resids[i]),comp);
			bonus[i][0]=0;
			for1(j,10){
				if (j>resids[i].sz){
					bonus[i][j]=bonus[i][j-1];
				} else {
					bonus[i][j]=bonus[i][j-1]+resids[i][j-1]->param;
				}
			}
		}
	}

	int MX[]={-1,-1,-1};
	item* best[3];
	forn(x,3){
		forn(i,items[x].sz){
			int tmp=items[x][i]->getMax();
			if (tmp>MX[x]){
				MX[x]=tmp;
				best[x]=items[x][i];
			}
		}
	}

	if (sum){
		int begins[]={0,0,0};
		forn(i,3){
			best[i]->resids.clear();
			int to=MIN(best[i]->params[3], (int)resids[i].sz);
			forn(j, to){
				best[i]->resids.pb(resids[i][begins[i]++]);
			}
		}
		int now=0;
		forn(i,3){
			int kol=best[i]->params[3]-best[i]->resids.sz;
			while(kol){
				while(begins[now]==resids[now].sz){
					now++;
					if (now==3) goto answ;
				}
				best[i]->resids.pb(resids[now][begins[now]++]);
				kol--;
			}
		}
	}
answ:
	forn(i,3){
		cout<<best[i]->name<<' '<<best[i]->resids.sz;
		forn(j,best[i]->resids.sz){
			cout<<' '<<best[i]->resids[j]->name;
		}
		cout<<endl;
	}

	return 0;
}