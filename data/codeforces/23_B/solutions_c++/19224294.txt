#include <stdio.h>

int main(){
  int n;
  scanf("%d",&n);
  for(int i=1,k;i<=n;i++)
    scanf("%d",&k),printf("%d\n",k>=2?k-2:0);
  return 0;
}

