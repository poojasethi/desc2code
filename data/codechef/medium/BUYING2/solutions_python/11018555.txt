#include<stdio.h>

#define MAX 100

int main(void)
{
        int T, arr[MAX], N, cost, total_items;
        scanf("%d", &T);
        while (T--) {
                int i, sum, remain;
                scanf("%d%d", &N, &cost);
                sum = 0;
                for(i = 0; i < N; i++) {
                        scanf("%d", &arr[i]);
                        sum += arr[i];
                }
                total_items = sum / cost;
                remain = sum % cost;
                if (remain == 0) {
                        printf("%d\n", total_items);
                } else {
                        for (i = 0; i < N; i++) {
                                if (((sum - arr[i]) / cost) == total_items) {
                                        printf("-1\n");
                                        break;
                                }
                        }
                        if (i == N) {
                                printf("%d\n", total_items);
                        }
                }
        }
        return 0;
}
