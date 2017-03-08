#include <cstdio>
#include <cstring>
char s[100010];
char ans[100010];
int sum[100010];
int n;
bool check()
{
    for (int i = 0; i < n / 2;)
    {
        if (sum[i] == sum[n - 1 - i])//  789 987     78  87
            ++i;
        else if (sum[i] == sum[n - 1 - i] + 1 || sum[i] == sum[n - 1 - i] + 10 + 1)
        {
            sum[i]--;
            sum[i + 1] += 10;
        }
        else if (sum[i] == sum[n - 1 - i] + 10)
        {
            sum[n - 2 - i]--;
            sum[n - 1 - i] += 10;
        }
        else
            return false;
    }
    if (n % 2 == 1)
    {
        if (sum[n / 2] % 2 == 1 || sum[n / 2] > 18 || sum[n / 2] < 0)
            return false;
        else
            ans[n / 2] = sum[n / 2] / 2 + '0';
    }
    for (int i = 0; i < n / 2; ++i)
    {
        if (sum[i] > 18 || sum[i] < 0)
            return false;
        ans[i] = (sum[i] + 1) / 2 + '0';
        ans[n - 1 - i] = sum[i] / 2 + '0';
    }
    return ans[0] > '0';
}
int main()
{
    scanf("%s", s);
    n = strlen(s);
    for (int i = 0; i < n; ++i)
        sum[i] = s[i] - '0';
    if (check())
        puts(ans);
    else if (s[0] == '1' && n > 1)
    {
        for (int i = 0; i < n; ++i)
            sum[i] = s[i + 1] - '0';
        n--;
        sum[0] += 10;
        if (check())
            puts(ans);
        else
            puts("0");
    }
    else
        puts("0");
    return 0;
}