#include <bits/stdc++.h>
using namespace std;
#define MAX 200009
int SA[200009];
int rank[20][200009];
int lcp[200009];
int cnt[300000];
struct tuple
{
	int left , right , pos;
	tuple(){
		left = right = pos = 0;
	}
};
bool compare(const tuple &a , const tuple &b)
{
	return a.left == b.left ? a.right < b.right : a.left < b.left;
}
void counting_sort(tuple t[] , int n)
{
	tuple temp[n+9];
	memset(cnt , 0 ,sizeof cnt);

	for(int i = 0 ; i < n ; i++){
		cnt[t[i].right+1]++;
	}

	for(int i = 1 ; i < MAX ; i++){
		cnt[i] += cnt[i-1];
	}

	for(int i = n-1 ; i >= 0  ; i --)
	{
		temp[cnt[t[i].right + 1] - 1] = t[i];
		cnt[t[i].right + 1]--;
	}

	memset(cnt , 0 , sizeof cnt);

	for(int i = 0 ; i < n ; i ++ )
		cnt[t[i].left + 1]++;

	for(int i = 1 ; i < MAX ; i++)
		cnt[i] += cnt[i-1];
	
	for(int i = n-1 ; i>=0 ; i --)
	{
		t[ cnt[temp[i].left + 1] -1 ] = temp[i];
		cnt[temp[i].left + 1]--;
	}
}
void suffixArray(char s[] , int len)
{
	for(int i = 0; i < len ; i++){
		if(s[i] == '#')
			rank[0][i] = 0;
		else
			rank[0][i] = s[i] - 'a' + 1;
	}
	tuple t[len+9];
	for(int stp = 1 , cnt = 1 ; (cnt>>1) < len ; cnt<<=1 , stp++)
	{
		for(int i = 0; i < len ; i++)
		{
			t[i].left = rank[stp-1][i];
			t[i].right = i+cnt < len ? rank[stp-1][i+cnt] : -1;
			t[i].pos = i;
		}

		//sort(t,t+len , compare);
		counting_sort(t,len);

		for(int i = 0 ;i < len ; i++)
			rank[stp][t[i].pos] = i>0 && t[i].left == t[i-1].left && t[i].right == t[i-1].right ? rank[stp][t[i-1].pos] : i;
	}
	int pos = ceil(log(len) / log(2));
	for(int i = 0; i < len ; i++)
		SA[rank[pos][i]] = i;
}
long long lcpArray(char s[],int len)
{
	int *rank = (int *)calloc(len+9, sizeof(int)) , k = 0 ;
	long long sum = 0;

	for(int i = 0 ; i < len ; i++) rank[SA[i]] = i;

	for(int i = 0 ; i < len ; i++ , k?k--:0)
	{
		if(rank[i] == len - 1){
			k = 0; 
			continue;
		}
		int j = SA[rank[i] + 1];
		while(i+k < len && j + k < len && s[i+k] == s[j+k]) k++;
		sum+=k;
	}
	return sum;
}
int main()
{
	char s[100009],t[100009],cat[200009];
	scanf("%s",s);
	scanf("%s",t);
	strcat(cat,s);
	strcat(cat,"#");
	strcat(cat,t);
	long long  a,b,c,lcp,ssum = 0;
	a = strlen(s);
	b = strlen(t);
	c = strlen(cat);
	long long l = a,r = b;
	suffixArray(s,a);
	lcp = lcpArray(s,a);
	a = a*(a+1)/2 - lcp;
	memset(SA , 0 , sizeof SA);
	ssum = 0;
	suffixArray(t,b);
	lcp = lcpArray(t,b);
	b = b*(b+1)/2 - lcp;
	memset(SA , 0 , sizeof SA);
	ssum = 0;
	suffixArray(cat,c);
	lcp = lcpArray(cat,c);
	c = c*(c+1)/2 - lcp - (l+1)*(r + 1);
	printf("%lld\n", 2*c - a - b);
	return 0;
}