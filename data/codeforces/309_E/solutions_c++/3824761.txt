#include <algorithm>
#include <stdio.h>
#include <memory.h>

using namespace std;

#define NN 2100

struct sheep {
    int a, b, id;
    bool operator<(sheep s) const {
        return b<s.b;
    }
} s[NN];

int N;
bool con[NN][NN];
int pos[NN], cnt[NN], ori[NN], on[NN];

bool OK(int T) {
    int i, j, sum, cur;
    for (i=0; i<N; i++) {
        pos[i]=-1;
        cnt[i]=0;
        ori[i]=N-1;
    }
    cnt[N-1]=N;
    
    for (i=0; i<N; i++) {
        sum=0;
        for (j=0; j<N; j++) {
            sum+=cnt[j];
            if (sum>j+1) return false;
            if (sum==j+1 && j>=i) break;
        }
        
        for (j=0; j<N; j++)
            if (ori[j]<sum && pos[j]==-1) break;
        
        cnt[ori[j]]--;
        cnt[i]++;
        pos[j]=ori[j]=i;
        on[i]=j;
        
        cur=j;
        
        for (j=0; j<N; j++) if (con[cur][j] && ori[j]>i+T) {
            cnt[ori[j]]--;
            cnt[i+T]++;
            ori[j]=i+T;
        }
        
    }
    
    return true;
}

int main() {

    int i, j, a, b, high, low, mid;
    
    scanf("%d", &N);
    
    for (i=0; i<N; i++) {
        scanf("%d%d", &a, &b);
        s[i].a=a; s[i].b=b; s[i].id=i+1;
    }
    
    sort(s, s+N);
    
    for (i=0; i<N; i++)
        for (j=0; j<N; j++)
            con[i][j]=!(s[i].a>s[j].b || s[i].b<s[j].a);
    
    high=N; low=0;
    while (high>low+1) {
        mid=(high+low)/2;
        if (OK(mid)) high=mid;
        else low=mid;
    }
    
    OK(high);
    
    printf("%d", s[on[0]].id);
    for (i=1; i<N; i++) 
        printf(" %d", s[on[i]].id);
    puts("");
    
    return 0;
}