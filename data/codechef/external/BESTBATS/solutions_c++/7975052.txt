#include<iostream>
#include<algorithm>
using namespace std;

int fect(int n)
{int i,f=1;
for(i=1;i<=n;i++)f*=i;

return f;
}

int main()
{ int t,i,a[11],n,k,c;
  cin>>t;
  while(t--)
  { c=1,n=0;
  for(i=0;i<11;i++)cin>>a[i];
  cin>>k;
  sort(a,a+11,greater<int>());
  for(i=0;i<11;i++)
   {if(a[k-1]==a[i]) n++;
    if(i<(k-1))
    {if(a[k-1]==a[i]) c++;}
   }
   if(n==1) cout<<c<<endl;
   else cout<<fect(n)/(fect(c)*fect(n-c))<<endl;
   }
return 0;
}
