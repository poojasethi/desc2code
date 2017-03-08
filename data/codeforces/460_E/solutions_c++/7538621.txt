#include <cstdio>

const int K = 210, N = 9;

int x[K], y[K], z[K], ax[N], ay[N], tx[N], ty[N], n, r, i, j, k, r1, r2, t, s;

void go(int t, int p)
{
    if (p == n)
    {
        int u = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                u += (tx[i] -  tx[j]) * (tx[i] - tx[j]) + (ty[i] - ty[j]) * (ty[i] - ty[j]);
        if (u > s)
        {
            s = u;
            for (int i = 0; i < n; i++)
                ax[i] = tx[i], ay[i] = ty[i];
        }
    }
    else
        for (int i = t; i < k; i++)
        {
            tx[p] = x[i], ty[p] = y[i];
            go(i, p + 1);
        }
}

int main()
{
    scanf("%d%d", &n, &r);

    r1 = (r - 1) * (r - 1);
    r2 = r * r;

    for (i = -r; i <= r; i++)
        for (j = -r; j <= r; j++)
        {
            t = i * i + j * j;
            if (t <= r2 && t > r1)
                x[k] = i, y[k] = j, z[k++] = t;
        }

    for (i = 0; i < k; i++)
        for (j = i + 1; j < k; j++)
            if (z[j] > z[i])
            {
                t = x[j], x[j] = x[i], x[i] = t;
                t = y[j], y[j] = y[i], y[i] = t;
                t = z[j], z[j] = z[i], z[i] = t;
            }

    k = 30 - n * 2;

    go(0, 0);

    printf("%d\n", s);
    for (i = 0; i < n; i++)
        printf("%d %d\n", ax[i], ay[i]);

    return 0;
}