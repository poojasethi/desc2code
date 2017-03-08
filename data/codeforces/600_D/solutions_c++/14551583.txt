#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main()
{
    long double x1, y1, r1, x2, y2, r2;
    cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
    if ( r1 > r2 )
    {
        swap(x1, x2);
        swap(y1, y2);
        swap(r1, r2);
    }
    long double d = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
    long double pi = acos(-1);
    long double area;
    if ( r1+r2 <= d )
        area = 0;
    else if ( r2-r1 >= d )
        area = pi*pow(r1, 2);
    else
    {
        long double rad1 = acos((r1*r1+d*d-r2*r2)/(2*r1*d)),
                    rad2 = acos((r2*r2+d*d-r1*r1)/(2*r2*d));
        area = rad1*r1*r1-0.5*r1*r1*sin(rad1*2) + rad2*r2*r2-0.5*r2*r2*sin(rad2*2);
    }
    cout << setiosflags(ios::fixed) << setprecision(8) << area << endl;
    return 0;
}
