// 10 monthes remaining for red =D
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;

const int maxtime=50000;
map<string,int>sub;
int rest[4][2];
int tme[maxtime];
int val[100+10][maxtime];
int lastk[100+10][maxtime];
int last[100+10][maxtime];
int tot;
int fromTime(int d,int hh,int mm){
	return (d-1)*24*60 + hh*60 + mm;
}
void toTime(int v,int& d,int& hh,int &mm){
	mm=v%60;
	v/=60;
	hh=v%24;
	v/=24;
	d=v+1;
}
bool isRest(int hh,int mm){
	int it=fromTime(1,hh,mm);
	for(int i=0;i<4;i++){
		if(it>=rest[i][0] && it<=rest[i][1])
			return true;
	}
	return false;
}


struct employ{
	int dl;
	int idx;
	int len,pay;
	bool friend operator < (const employ& p1,const employ& p2){
		return p1.dl<p2.dl;
	}
};
int n,m,nk;
string names[100+10];
char line[100+10];
employ es[100+10];
void pass(int idx){
	copy(val[idx - 1],val[idx - 1]+tot,val[idx]);
	copy(last[idx - 1],last[idx - 1]+tot,last[idx]);
	copy(lastk[idx - 1],lastk[idx - 1]+tot,lastk[idx]);
	int cost=es[idx].len;
	int i;
	for(i=tot-1;i>=0 && tme[i]>=es[idx].dl;i--);
	if(i<cost)return;
	for(;i>=cost;i--){
		if(val[idx][i-cost] + es[idx].pay > val[idx][i]){
			val[idx][i]= val[idx][i-cost] + es[idx].pay;
			last[idx][i] = idx;
			lastk[idx][i] = idx - 1;
		}
	}
}

void output(int x,int k){
	if(last[k][x]<=0)return;
	output(x - es[last[k][x]].len,lastk[k][x]);
	int dd,h1,m1,dl,h2,m2;
	toTime(tme[x],dd,h1,m1);
	toTime(tme[x-es[last[k][x]].len+1],dl,h2,m2);
	printf("%d %d %02d:%02d %d %02d:%02d\n",es[last[k][x]].idx,
			dl,h2,m2,dd,h1,m1);
}
int main(){
	cin>>m>>n>>nk;
	int cost,dd,h1,m1,h2,dl,m2;
	for(int i=0;i<m;i++){
		cin>>names[i];
	}
	for(int i=0;i<m;i++){
		cin>>cost;
		sub.insert(make_pair(names[i],cost));
	}
	for(int i=0;i<4;i++){
		cin>>line;
		sscanf(line,"%d:%d-%d:%d",&h1,&m1,&h2,&m2);
		rest[i][0]=fromTime(1,h1,m1);
		rest[i][1]=fromTime(1,h2,m2);
	}
	tot=1;
	tme[0]=-1;
	for(int i=1;i<=nk;i++)
		for(int j=0;j<=23;j++)
			for(int k=0;k<=59;k++){
				if(!isRest(j,k))
					tme[tot++]=fromTime(i,j,k);
			}
	/*for(int i=0;i<tot;i++)
		cout<<tme[i]<<' ';
	cout<<endl;*/
	fill(last[0],last[0]+tot,-1);
	fill(lastk[0],lastk[0]+tot,-1);
	fill(val[0],val[0]+tot,0);
	string csub;
	int pay;
	int k=1;
	for(int i=1;i<=n;i++){
		cin>>csub>>dd>>line>>pay;
		sscanf(line,"%d:%d",&h1,&m1);
		if(sub.find(csub)!=sub.end()){
			es[k].len=sub[csub];
			es[k].dl=fromTime(dd,h1,m1);
			es[k].pay = pay;
			es[k].idx=i;
			k++;
		}
	}
	n = k - 1;
	sort(es+1,es+1+n);
	int besti=-1,best=0;
	for(int i=1;i<=n;i++){
		pass(i);
	}

	for(int i=1;i<tot;i++){
		if(last[n][i]>0 && val[n][i]>best){
			best=val[n][i];
			besti=i;
		}
	}
	if(besti<0)
		printf("0\n0\n");
	else{
		printf("%d\n",best);
		int j=besti,k=n,tj;
		int cnt=0;
		while(last[k][j]>0){
			cnt++;
			tj = j - es[last[k][j]].len;
			k = lastk[k][j];
			j = tj;
		}
		printf("%d\n",cnt);
		j = besti;
		output(j,n);
	}
	return 0;
}
