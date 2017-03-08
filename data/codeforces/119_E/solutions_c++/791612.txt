#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

const long double EPS = 1e-8;

struct Point {
  long double x, y, z;
  
  Point() {}
  Point(long double a, long double b, long double c): x(a), y(b), z(c) {}

  // cross product of two vectors
  Point operator*(const Point& p) const {
    return Point(y*p.z - p.y*z, z*p.x - p.z*x, x*p.y - p.x*y);
  }

  void Normalize() {
    long double norm = sqrt(x*x+y*y+z*z);
    x /= norm;
    y /= norm;
    z /= norm;
  }
};

long double CalculateDistance(const Point& p1, const Point& p2) {
  return sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y) + (p1.z-p2.z)*(p1.z-p2.z));
}

struct Circle {
  Point center;
  long double radius;

  Circle(): center(Point(0, 0, 0)), radius(0) {}
  Circle(const Point& p1): center(Point(p1.x, p1.y, p1.z)), radius(0) {}
  Circle(const Point& p1, const Point& p2) {
    center = Point((p1.x+p2.x)/2, (p1.y+p2.y)/2, (p1.z+p2.z)/2);
    radius = CalculateDistance(center, p1);
  }
  Circle(const Point& p1, const Point& p2, const Point& p3) {
    // Vectors p1p2 and p1p3
    Point V(p2.x-p1.x, p2.y-p1.y, p2.z-p1.z);
    V.Normalize();
    Point W(p3.x-p1.x, p3.y-p1.y, p3.z-p1.z);
    W.Normalize();

    // Vector N = V x W
    Point N = V*W;
    N.Normalize();

    // Vector D1 = V x N
    Point D1 = V*N;
    // Vector D2 = W x N
    Point D2 = W*N;

    // Middles of p1p2 and p1p3
    Point M1 = Point((p1.x+p2.x)/2, (p1.y+p2.y)/2, (p1.z+p2.z)/2);
    Point M2 = Point((p1.x+p3.x)/2, (p1.y+p3.y)/2, (p1.z+p3.z)/2);
    // Solving M1 + alpha*D1 = M2 + beta*D2
    long double alpha;
    // The points may be in planes x = 0 or y = 0 or z = 0 which result in special cases where the
    // denominators are 0.

    if (fabs(D1.y*D2.x-D1.x*D2.y) > EPS) {
      alpha = (D2.x*(M2.y-M1.y) - D2.y*(M2.x-M1.x)) / (D1.y*D2.x-D1.x*D2.y);
    } else if (fabs(D1.z*D2.y-D1.y*D2.z) > EPS) {
      alpha = (D2.y*(M2.z-M1.z) - D2.z*(M2.y-M1.y)) / (D1.z*D2.y-D1.y*D2.z);
    } else {
      alpha = (D2.z*(M2.x-M1.x) - D2.x*(M2.z-M1.z)) / (D1.x*D2.z-D1.z*D2.x);
    }
    center = Point(M1.x + alpha*D1.x, M1.y + alpha*D1.y, M1.z + alpha*D1.z);
    radius = CalculateDistance(center, p1);
    assert(fabs(radius-CalculateDistance(center, p2)) < EPS);
    assert(fabs(radius-CalculateDistance(center, p3)) < EPS);
  }
};

vector <Point> ProjectPoints(int A, int B, int C, const vector<Point>& points) {
  vector <Point> result(points.size());
  for (size_t i = 0; i < points.size(); ++i) {
    long double alpha = -(A*points[i].x+B*points[i].y+C*points[i].z) / (A*A+B*B+C*C);
    result[i] = Point(points[i].x + alpha*A, points[i].y + alpha*B, points[i].z + alpha*C);
  }
  return result;
}

int IsPointInCircle(const Point& p, const Circle& c) {
  return CalculateDistance(p, c.center) <= c.radius+EPS;
}

Circle FindMinimumEnclosingCircle(
    vector<Point>& not_verified_points, vector<Point>& circumference_points) {
  if (not_verified_points.size() == 0 || circumference_points.size() >= 3) {
    if (circumference_points.size() == 0) {
      return Circle();
    }
    if (circumference_points.size() == 1) {
      return Circle(circumference_points[0]);
    }
    if (circumference_points.size() == 2) {
      return Circle(circumference_points[0], circumference_points[1]);
    }
    return Circle(circumference_points[0], circumference_points[1], circumference_points[2]);
  } else {
    int index = rand() % not_verified_points.size();
    Point p = not_verified_points[index];
    not_verified_points[index] = not_verified_points[not_verified_points.size()-1];
    not_verified_points.pop_back();
    Circle c = FindMinimumEnclosingCircle(not_verified_points, circumference_points);
    if (!IsPointInCircle(p, c)) {
      circumference_points.push_back(p);
      c = FindMinimumEnclosingCircle(not_verified_points, circumference_points);
      circumference_points.pop_back();
    }
    not_verified_points.push_back(p);
    return c;
  }
}

int main() {
  int seed = 1319233241;
  srand(seed);
#ifndef ONLINE_JUDGE
  freopen("e.in", "r", stdin);
#endif

  int num_points, num_tests;
  vector <Point> points;
  scanf("%d %d", &num_points, &num_tests);
  for (int i = 0; i < num_points; ++i) {
    int x, y, z;
    scanf("%d %d %d", &x, &y, &z);
    points.push_back(Point(x, y, z));
  }

  for (int test = 1; test <= num_tests; ++test) {
    int A, B, C;
    scanf("%d %d %d ", &A, &B, &C);
    vector <Point> projected_points = ProjectPoints(A, B, C, points);
    vector <Point> circumference_points = vector<Point>();
    Circle min_circle = FindMinimumEnclosingCircle(projected_points, circumference_points);
    cout << fixed << setprecision(10) << min_circle.radius << endl;
  }

  return 0;
}
