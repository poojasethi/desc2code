#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
#include<numeric>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<list>
#include<climits>
#include<cstdlib>
#include<string>

using namespace std;

#define inf 1000000007
#define eps 1e-19
#define rev(s,e) reverse(s,e)
#define mset(s,i) memset(s,i,sizeof(s))
#define cpy(i,j) memset(i,j,sizeof(j))
#define mp(x,y) make_pair(x,y)
#define ff first
#define ss second
#define ld long double
#define li long int
#define lli long long int
#define pb(x) push_back(x)
#define f(i,a,b) for(int i=a;i<b;i++)
#define fr(i,a,b) for(int i=a;i>b;i--)

// stores the graph and visited vertices
int gp[26][26],v[26];

// stores the incoming and outgoing edges for each character
int in[26],out[26];

void dfs(int i){
  v[i]=1;
  f(j,0,26){
    if(!v[j] && gp[i][j]){
      dfs(j);
    }
  }
}

int main(){
  int t,n,k,a,b,c,d;
  string s;
  cin>>t;
  while(t--){
    mset(gp,0);mset(v,0);mset(in,0);mset(out,0);
    cin>>n;
    f(i,0,n){
      cin>>s;
      // now suitably modify the incoming,outgoing and gp arrays
      out[s[0]-'a']++;
      in[s[s.length()-1]-'a']++;
      gp[s[0]-'a'][s[s.length()-1]-'a']=1;
      gp[s[s.length()-1]-'a'][s[0]-'a']=1;
      k=s[0]-'a';
    }
    dfs(k);
    // check if everything can be visited
    int flag=1;
    f(i,0,26){
      if((in[i] || out[i]) && !v[i]){
	flag=0;
	break;
      }
    }
    if(!flag){
      cout<<"The door cannot be opened.\n";
      continue;
    }
    a=b=c=d=0;
    f(i,0,26){
      if(in[i] || out[i]){
	if(out[i]-in[i] ==1){
	  b++;
	}
	if(out[i]-in[i] ==-1){
	  a++;
	}
	if(out[i]-in[i] ==0){
	  c++;
	}
	d++;
      }
    }
    if(a>1 || b>1 || a+b+c!=d){
      cout<<"The door cannot be opened.\n";
    }
    else{
      cout<<"Ordering is possible.\n";
    }
  }
}
