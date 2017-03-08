#include <iostream>

using namespace std;

int main() {
    int x1, x2, x3, x4, y1, y2, y3, y4;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4;
    if (((x1>y3 && y2>x4) && (x1>y4 && y2>x3)) || ((y1>x3 & x2>y4) && (y1>x4 && x2>y3))) {
        cout << "Team 1" << endl;
    } else if (((x3>y1 && y4>x2) || (y3>x2 && x4>y1)) && ((y3>x1 && x4>y2) || (x3>y2 && y4>x1))) {
        cout << "Team 2" << endl;
    } else cout << "Draw" << endl;
    return 0;
}
