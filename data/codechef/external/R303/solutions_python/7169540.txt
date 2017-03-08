#include<bits/stdc++.h>
#define INF 1000000002
using namespace std;
struct Point {
    double x, y;
};

class Polygon {
    public:
        int points;
        double area;
        vector<Point> P;
        void addVertices(double x, double y) {
            Point t;
            t.x = x;
            t.y = y;
            P.push_back(t); 
        }
        ~Polygon() {
            P.clear();
        }
        void polygonArea();
};

void Polygon::polygonArea() {
    double ar = 0.0;
    int i, j;

    for (i = 0 ; i < points; i++) {
        j = (i + 1) % points;
        ar += P[i].x * P[j].y - P[i].y * P[j].x; 
    }
    area = ar * 0.5;
    if(area < 0)
        area = -area;
}

int main() {
    int t, i, n;
    double x, y;
    vector<double> X, Y;
    Polygon temp, max;
    scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        Polygon tmp;
        tmp.points = n;
        X.clear();
        Y.clear();
        for(i = 0 ; i < n ; i++) {
            scanf("%lf", &x);
            X.push_back(x);
        }
        for(i = 0 ; i < n ; i++) {
            scanf("%lf", &x);
            Y.push_back(x);
        }
        for(i = 0 ; i < n ; i++) {
            tmp.addVertices(X[i], Y[i]);
        }
        tmp.polygonArea();
        printf("%.1lf\n", tmp.area);
    }
    return 0;
}
