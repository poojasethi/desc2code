#include <vector>
#include <stdio.h>

int main() {
  int n,i;
  scanf("%d",&n);
  char a[n][n];
  for (i = 0;i < n;i++) scanf("%s",a[i]);
  std::vector<int> b(1,0);
  for (i = 1;i < n;i++) {
    int l=0,r=i-1;
    while (l<i && a[i][b[l]]=='0') l++;
    while (r>=0 && a[i][b[r]]=='1') r--;
    if (l==r+1)
        b.insert(b.begin()+l,i);
    else {
        printf("%d %d %d\n",b[l]+1,b[r]+1,i+1);
        return 0;
    }
  }
  if (i == n) printf("-1\n");
  return 0;
}