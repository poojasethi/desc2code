/*
Rashik Hasnat;
uva, a2oj:Rashik, codeforces, codechef, codemarshal:rashik004;
Khulna University of Engineering & Technology (KUET), Khulna
Bangladesh
*/
#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define ll long long
#define ull unisgned long long
#define read freopen("Input.txt","r",stdin)
#define write freopen("output.txt","w",stdout)
#define vi vector<int>
#define MAX 10000+5
#define all(v) v.begin(), v.end()
#define PI acos(-1.0)
#define mem(ara, value) memset(ara, value, sizeof(ara))
#define sf scanf
#define Tcase(t) for(int qq=1;qq<=t; qq++)
using namespace std;

/// ******************************** ///
int Set(int N, int pos){return N=N|(1<<pos);}
int check(int N, int pos){return N & (1<<pos);}
bool isLinier(int a, int b, int m, int n, int x, int y)
{
    int t1,t2;
    t1=(n-b)*(x-m);
    t2=(y-n)*(m-a);
    if(t1==t2)
        return true;
    else
        return false;
}
///************main code starts from below******************///

int tailTable[MAX*2],numbers[MAX*2];

void binary_search(int start, int end, int key)
{
	int mid;
	while(start<=end)
	{
		mid=(start+end)/2;

		if(tailTable[mid] == key)
			return;
		else if(tailTable[mid] > key)
			end=mid-1;
		else
			start=mid+1;
	}
	if(tailTable[start]<key)  // no need;  just for safety!!
		start++;
	tailTable[start]=key;
}


int lis(int start, int last)
{
    int i,n,cur,num;

    cur=1;
    tailTable[0]=numbers[start];
    for(int i=start+1;i<last;i++)
    {
        num=numbers[i];
        if(num>tailTable[cur-1])
            tailTable[cur++]=num;
        else if(num<tailTable[cur-1])
            binary_search(0,cur-1,num);
    }
    return cur;
}

int main()
{
    int testCase,x,y,m,k,h,n;

    cin>>testCase;
    Tcase(testCase)
    {
        cin>>n;
        for(int i=0;i<n; i++)
        {
            cin>>x;
            numbers[i]=x;
            if(i!=n-1)
                numbers[i+n]=x;
        }
        int maxM=-1;
        for(int i=0;i<n; i++)
        {
            int temp=lis(i,i+n);
            maxM=max(temp, maxM);
        }
        cout<<maxM<<endl;
    }

    return 0;
}
