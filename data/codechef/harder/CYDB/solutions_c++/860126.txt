#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <queue>
using namespace std;
 
typedef long long int64;
 
#define MOD 1000000007
 
class node {
public:
  int len, score;
  node *go[2], *fail;
  node() {
    go[0]=0; go[1]=0;
    fail=0; len=0; score=0;
  }
};
 
int sqr(int len) { return len*len; }
 
char a[1009],c[1009],b[10000009];
int na,nb;
 
void buildTrie(node *n, int p, int k=0) {
  for (int i=p;i<na;i++) {
    if (c[i]=='1' && k<2) {
      for (int ch=0;ch<=1;ch++) {
        n->go[ch] = new node();
        n->go[ch]->len = n->len+1;
        buildTrie(n->go[ch], i+1, k+(ch!=a[i]-'0'));
      }
      break;
    } else {
      int ch=a[i]-'0';
      n->go[ch] = new node();
      n->go[ch]->len = n->len+1;
      n=n->go[ch];
    }
  }
}
 
node* Q[1000000];
int bQ=0, eQ=0;
 
int solve() {
  // build trie of patterns
  node *root = new node();
  buildTrie(root, 0);
  // compute fail links
  bQ=0; eQ=0;
  for (int ch=0;ch<=1;ch++) {
    if (!root->go[ch]) root->go[ch]=root;
    else {
      node *nn = root->go[ch];
      nn->fail=root;
      Q[eQ++]=nn;
      nn->score = sqr(nn->len);
    }
  }
  while (bQ<eQ) {
    node *n=Q[bQ++];
    for (int ch=0;ch<=1;ch++) if (n->go[ch]) {
      node *nn = n->go[ch];
      Q[eQ++]=nn;
      node *v = n->fail;
      while (!v->go[ch]) v=v->fail;
      nn->fail = v->go[ch];
      nn->score = nn->fail->score + sqr(nn->len);
    }
  }
  // search
  node *s=root;
  int64 r=0;
  for (int i=0;i<nb;i++) {
    int ch=b[i]-'0';
    while (!s->go[ch]) s=s->fail;
    s=s->go[ch];
    r+=s->score;
  }
  return r%MOD;
}
 
char ca[209], cc[209];
char cb[2000009];
 
void decode(char *c, int n, char *d) {
  for (int i=0;i<n;i++) {
    int x=0;
    if ('a'<=c[i] && c[i]<='z') x=c[i]-'a';
    else if ('A'<=c[i] && c[i]<='F') x=c[i]-'A'+26;
    for (int j=0;j<5;j++) {
      d[i*5+4-j]='0'+x%2;
      x/=2;
    }
  }
  d[5*n]='\0';
}
 
int main() {
  scanf("%s %s %s",ca,cb,cc);
  na=strlen(ca);
  nb=strlen(cb);
  decode(ca,na,a);
  decode(cb,nb,b);
  decode(cc,na,c);
  na*=5; nb*=5;
  printf("%d\n",solve());
  return 0;
}