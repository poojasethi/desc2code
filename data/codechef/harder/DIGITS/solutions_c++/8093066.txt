#include<bits/stdc++.h>
using namespace std;
const int P =    1000000007;
const int inv5 = 400000003;
const int inv7 = 142857144;

struct item
{
	int value;
	int a;
	int b;
}w[1500000];
int cntw=0;
int compare(const void *a,const void *b)
{
	item* aa=(item*)a;
	item* bb=(item*)b;
	if(aa->value != bb->value) return aa->value<bb->value?-1:1;
	return 0;

}
void init()
{
	long long int pow2=1;
	for(int a=0;a/3<700;a++)
	{
		long long int pow3=pow2;
		for(int b=0;b/2+a/3<700;b++)
		{
			w[cntw].value=(int)pow3;
			w[cntw].a=a;
			w[cntw++].b=b;
			pow3=(pow3*3)%P;
		}
		pow2=(pow2*2)%P;
	}

	qsort(w,cntw,sizeof(w[0]),compare);
}
const int MAXL=910;
int temp[MAXL];
int res[MAXL];
int find(int value)
{
	//cout<<cntw<<endl;
	int l=0,r=cntw-1;
	while(l<=r)
	{
		int mid=(l+r)/2;
		if(w[mid].value == value)
			 return mid;
	    else if(w[mid].value>value)
	    
	    	  r=mid-1;
	    
	    else
	    	l=mid+1;
	}
	return -1;
}
int minLen;
bool isLess(int len)
{
	for(int i=len-1;i>=0;i--)
	{
		if(temp[i]!=res[i]) return temp[i]<res[i];
	}
	return false;
}
void check(int a,int b,int c,int d)
{
	if(a/3+b/2+c+d>900) return;
	int i=0;
	while(b>=2)
	{
		temp[i++]=9;
		b-=2;
	}
	while(a>=3)
	{
		temp[i++]=8;
		a-=3;
	}
	while(d>=1)
	{
		temp[i++]=7;
		d-=1;
	}
	while(a>=1 && b>=1)
	{
		temp[i++]=6;
		a--;
		b--;
	}
	while(c>=1)
	{
		temp[i++]=5;
		c-=1;
	}
	while(a>=2)
	{
		temp[i++]=4;
		a-=2;
	}
	while(b>=1)
	{
		temp[i++]=3;
		b--;
	}
	while(a>=1)
	{
		temp[i++]=2;
		a-=1;
	}
	int len=i;
	if(minLen>len|| minLen==len&&isLess(len))
	{
		for(int i=0;i<len;i++)
		{
			res[i]=temp[i];
		}
		minLen=len;
	}
}


void solve(int n)
{
	if(n==0)
	{
		printf("10\n");
		return ;
	}
	else if(n==1)
	{
		printf("1\n");
		return ;
	}
	else
	{
		minLen=1000;
		long long int pow5=n;
		for(int c=0;c<700;c++)
		{
			long long int pow7=pow5;
			for(int d=0;d+c<700;d++)
			{
				//cout<<pow7<<endl;
				int index=find(pow7);
				if(index!=-1)
				{

					check(w[index].a,w[index].b,c,d);
				}
				pow7=(pow7*inv7)%P;
			}
			pow5=(pow5*inv5)%P;
		}
		for(int i=minLen-1;i>=0;i--)
			printf("%d",res[i]);
		printf("\n");
	}
}
int main()
{
	init();
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int n;
		scanf("%d",&n);
		solve(n);
	}
}