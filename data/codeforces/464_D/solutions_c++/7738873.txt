#include <iostream>
#include <iomanip>
using namespace std;

int n, k;
double d[710];

int main() {
    cin >> n >> k;

    for (int i = 0; i < 710; i++)
        d[i] = 0.0;

    for (int i = 1; i <= n; i++) {
        for (int t = 1; t < 710; t++) {
            d[t] = (k - 1)*1.0/k * d[t] + 1.0/(k*(t+1)) * (t * d[t] + d[t+1] + t*(t+3)*0.5);
        }
    }

    double res = d[1] * k;
    cout << fixed << setprecision(10) << res << endl;
    return 0;
}