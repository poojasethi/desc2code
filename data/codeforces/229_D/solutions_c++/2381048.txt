#include<iostream>
using namespace std;
int height[5050];
int dp[5050], minh[5050];
int main()
{
  int n;
  cin>>n;
  for (int i = 1; i <= n; i++) cin>>height[i];
  dp[1] = 0, minh[1] = height[1];
  for (int i = 2; i <= n; i++) {
    int j = i-1, sum = height[i];
    while (j && minh[j]>sum) sum += height[j--];
    dp[i] = dp[j] + i-j-1;
    minh[i] = sum;
  }
  cout<<dp[n]<<endl;
  return 0;
}
