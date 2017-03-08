#include<cstdio>
#define N 100010
int L, R, ans = 0, cnt[N];
int stk[N], tp;
char s[N];
void check(int l, int r){
    if(ans < cnt[r]-cnt[l]){
        ans = cnt[r]-cnt[l];
        L = l; R = r;
    }
}
int main(){
    stk[tp++] = 0;
    scanf("%s", s+1);

    for(int i = 1; s[i]; i++){
        
        cnt[i] = cnt[i-1] + (s[i] == '[');
        
        if(s[i] == '[' || s[i] == '(') stk[tp++] = i;
        else if(s[i] == ']' && s[stk[tp-1]] != '[' || s[i] == ')' && s[stk[tp-1]] != '(') tp = 0, stk[tp++] = i;
        else tp--, check(stk[tp-1], i);

    }
    printf("%d\n", ans);
    for(int i = L+1; i <= R; i++) putchar(s[i]);
    puts("");
}