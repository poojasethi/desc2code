#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

const int MAX_N = 1010;
const double EPS = 0.0000001;

struct Point {
  int x, y;

  Point() {}
  Point(int a, int b) : x(a), y(b) {}
};

int n;
long long k;
Point centers[MAX_N];
int radii[MAX_N];

double GetDist(int x1, int y1, int x2, int y2) {
  return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

void AddEvents(vector<pair<double, int> > &events, double ang1, double ang2) {
  for (int i = 0; i < 3; ++i) {
    events.push_back(make_pair(ang1+i*2*M_PI + EPS, 1));
    events.push_back(make_pair(ang2+i*2*M_PI - EPS, -1));
  }
}

int main() {
#ifndef ONLINE_JUDGE
  ifstream cin("e.in");
#endif

  cin >> n >> k;
  for (int i = 1; i <= n; ++i) {
    int x, y;
    cin >> x >> y >> radii[i];
    centers[i] = Point(x, y);
  }

  int best = 0;
  for (int i = 1; i <= n; ++i) {
    vector<pair<double, int> > events;
    int cnt = 0;
    for (int j = 1; j <= n; ++j) {
      if (i != j) {
        double ang = atan2(centers[j].y-centers[i].y, centers[j].x-centers[i].x);
        double d = GetDist(centers[i].x, centers[i].y, centers[j].x, centers[j].y);
        double u1 = asin((radii[i]-radii[j]) / d);
        double u2 = asin((radii[i]+radii[j]) / d);
        AddEvents(events, ang+u1-M_PI/2, ang+u2-M_PI/2); 
        AddEvents(events, ang-u2+M_PI/2, ang-u1+M_PI/2);
      }
    }

    sort(events.begin(), events.end());

    for (size_t j = 0; j < events.size(); ++j) {
      cnt += events[j].second;
      if (cnt < 0) {
        cnt = 0;
      }
      best = max(best, cnt);
    }
  }

  long long sol = k*(k+1)/2 + (k+1)*best + (n-best);
  cout << sol << endl;

  return 0;
}
