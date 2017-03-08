#include <cstdio>
#include <cstring>

const int N = 200010;
const int Y = N >> 5;

int qn;
char sa[N],sb[N];
int cnt[N];
unsigned int ca[N],cb[N],*ia,*ib;
const int mod = (1<<16) - 1;

inline unsigned int B(int i) {
    return 1<<i;
}

void genc(char sx[], unsigned int cx[]) {
    for (int i=0; sx[i]; i++) {
        int u = i >> 5 , v = i & 31;
        for (int j=0; j<32&&sx[i+j]; j++) {
            unsigned int now = sx[i+j]-'0';
            cx[v*Y + u] |= (now<<j);
        }
    }
}

inline int getv(unsigned int z) {
    return cnt[z>>16]+cnt[z&mod];
}

int main() {
    for (int i=0; i<B(16); i++) {
        cnt[i] = cnt[i>>1]+(i&1);
    }
    scanf("%s%s%d",sa,sb,&qn);
    genc(sa,ca);
    genc(sb,cb);
    int x,y,l,ans;
    while(qn--) {
        scanf("%d%d%d",&x,&y,&l);
        for(ans = 0,ia = ca + Y*(x&31)+(x>>5), ib = cb + Y*(y&31)+(y>>5); l >= 32; l -= 32) {
            ans += getv((*ia)^(*ib));
            ia++;
            ib++;
        }
        ans += getv(((*ia)^(*ib))&(B(l)-1));
        printf("%d\n",ans);
    }
    return 0;
}
