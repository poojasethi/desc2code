#include <cstdio>

int main() {
 int x, y;
 scanf("%d:%d", &x, &y);
 for (int i=0; i<=23; i++) for (int j=0; j<=59; j++) {
  if (i>x || i==x && j>y) {
   if (i%10 == j/10 && i/10 == j%10) {
    printf("%02d:%02d\n", i, j);
    return 0;
   }
  }
 }
 puts("00:00");
 return 0;
}