#include <iostream>
using namespace std;

int main() {
    int n;
    cin >>n;
    int a[n];
    for (int i=0;i<n;i++) cin >>a[i];
    int b = min(a[0], a[n-1]);
    for (int i=0;i<n-1;i++) b = min(b, max(a[i], a[i+1]));
    cout <<b <<endl;
    return 0;
}
