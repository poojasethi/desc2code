#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>

using namespace std;

typedef long long ll;

const int P = 4;
const int N = 4;
const double EPS = 1e-9;

inline bool isEqual(double d1, double d2)
{
    return fabs(d1-d2) < EPS;
}

class Polynomial
{
    vector<vector<double> > matrix;
    vector<double> coeff;
    vector<double> roots;
    double val(const vector<double> &c, const double t) const;
    double bsearch(double l, double r) const;
public:
    Polynomial(const vector<int> &tv, const vector<int> &vv);
    void gauss_jordan();
    void find_roots(const int T);
    double integrate();
};

Polynomial::Polynomial(const vector<int> &tv, const vector<int> &vv)
    : matrix(N, vector<double>(N+1)), coeff(N)
{
    for (int i = 0; i < N; i++)
    {
        ll p = 1;
        for (int j = N-1; j >= 0; j--)
        {
            matrix[i][j] = p;
            p *= tv[i];
        }
        matrix[i][N] = vv[i];
    }
}

void Polynomial::gauss_jordan()
{
    double d;
    for (int i = 0; i < N; i++)
    {
        d = matrix[i][i];
        for (int j = i; j <= N; j++)
            matrix[i][j] /= d;
        for (int r = 0; r < N; r++)
        {
            if (r == i)
                continue;
            d = matrix[r][i];
            for (int j = i; j <= N; j++)
                matrix[r][j] -= matrix[i][j] * d;
        }
    }
    for (int i = 0; i < N; i++)
    {
        if (isEqual(matrix[i][N], 0))
            coeff[i] = 0;
        else
            coeff[i] = matrix[i][N];
        cerr << coeff[i] << "x^" << N-i-1 << ' ';
    }
    cerr << endl;
}

double Polynomial::val(const vector<double> &c, const double t) const
{
    const int n = c.size();
    double r = c[n-1], _t = t;
    for (int i = n-2; i >= 0; i--, _t *= t)
        r += c[i]*_t;
    return r;
}

double Polynomial::bsearch(double l, double r) const
{
    const double dl = val(coeff, l);
    const double dr = val(coeff, r);
    if (dl * dr >= 0)
        return -1;
    double mid = (l+r)/2;
    double dm = val(coeff, mid);
    if (dl < 0)
    {
        while (!isEqual(dm, 0))
        {
            if (dm < 0) l = mid;
            else r = mid;
            mid = (l+r)/2;
            dm = val(coeff, mid);
        }
    }
    else
    {
        while (!isEqual(dm, 0))
        {
            if (dm < 0) r = mid;
            else l = mid;
            mid = (l+r)/2;
            dm = val(coeff, mid);
        }
    }
    return mid;
}

void Polynomial::find_roots(const int T)
{
    //differentiate
    double a = 3*coeff[0];
    double b = 2*coeff[1];
    double c = 1*coeff[2];

    cerr << a << "x^2 " << b << "x " << c << endl;

    //find roots of slope
    double d = b*b - 4*a*c;

    if (d < 0 || isEqual(d, 0))
    {
        //The roots of slope are imaginary
        //=> there is no maxima or minima of velocity
        //=> velocity is monotonic
        double r = bsearch(0, T);
        if (r > 0) roots.push_back(r);
        roots.push_back(T);
        return;
    }

    double r1 = (-b - sqrt(d))/(2*a);
    double r2 = (-b + sqrt(d))/(2*a);
    if (r1 > r2) swap(r1, r2);

    cerr << "d = " << d << " r1 = " << r1 << " r2 = " << r2 << endl;

    double r;
    if (r1 > 0)
    {
        r = bsearch(0, min(r1, (double)T));
        if (r > 0) roots.push_back(r);
    }
    if (r1 < T && r2 > 0)
    {
        r = bsearch(max(r1, 0.0), min(r2, (double)T));
        if (r > 0) roots.push_back(r);
    }
    if (r2 < T)
    {
        r = bsearch(max(0.0, r2), T);
        if (r > 0) roots.push_back(r);
    }
    roots.push_back(T);
}

double Polynomial::integrate()
{
    vector<double> intCoeff(N+1);

    for (int i = 0; i < N; i++)
    {
        intCoeff[i] = coeff[i]/(N-i);
        cerr << intCoeff[i] << "x^" << N-i << ' ';
    }
    cerr << endl;
    double t1 = 0, distance = 0;
    for (vector<double>::iterator it = roots.begin();
            it != roots.end(); it++)
    {
        distance += fabs(val(intCoeff, *it) - val(intCoeff, t1));
        cerr << *it << '\t';
        t1 = *it;
    }
    cerr << endl;
    cerr << "distance = " << distance << endl;
    return distance;
}

void solve()
{
    int T;
    vector<int> tv(P), vv(P);

    cin >> T;
    for (int i = 0; i < P; i++)
    {
        cin >> tv[i] >> vv[i];
    }

    Polynomial poly(tv, vv);
    poly.gauss_jordan();
    poly.find_roots(T);
    printf("%.12lf\n", poly.integrate());

    cerr << endl;
}

int main()
{
    int n;
    cin >> n;

    while (n--)
    {
        solve();
    }
    return 0;
}
