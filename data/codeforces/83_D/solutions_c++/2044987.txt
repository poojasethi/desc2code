#include<iostream>
using namespace std;
bool isPrime(int x)
{
  for (int i = 2; i*i <= x; i++) if (x%i == 0) return false;
  return true;
}
int solve(int a, int k)
{
  if (k > a || !isPrime(k)) return 0;
  int ret = a/k;
  for (int i = 2; i < k && i <= a/k; i++)
    ret -= solve(a/k,i);
  return ret;
}
int main()
{
  int a, b, k;
  cin>>a>>b>>k;
  cout<<solve(b,k)-solve(a-1,k)<<endl;
  return 0;
}
