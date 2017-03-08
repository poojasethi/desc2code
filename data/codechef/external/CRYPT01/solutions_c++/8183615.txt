#include<bits/stdc++.h>
using namespace std;

int main()
{ 
	ios_base::sync_with_stdio(0);
  	int t,n,i,x,r,f,c=0;
	  cin>>t;
	  while(t--)
	  {  
	  	r=0,f=0;
	  	c++;
	     	cin>>n;
	     	for(i=0;i<n;i++)
	     	{  
	     		cin>>x;
	        	r+=((x/30)+1)*10;
	        	f+=((x/60)+1)*15;
	     	}
	     	if(r>f)printf("Case %d: Frag %d\n",c,f);
	     	else if(f>r)printf("Case %d: Respawn %d\n",c,r);
	     	else printf("Case %d: Respawn Frag %d\n",c,f);
	  }
	  return 0;
}
   