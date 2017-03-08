#include <cstdio>
int cnt[10];
char str[55];
int main()
{
    scanf("%s",str);
    for(int i=0; str[i]; i++)
        cnt[str[i]-'0']++;
    if(cnt[4]+cnt[7]==0)
        printf("-1");
    else
        printf("%d",cnt[4]>=cnt[7]?4:7);
    return 0;
}
