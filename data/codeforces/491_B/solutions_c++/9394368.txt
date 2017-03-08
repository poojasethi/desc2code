#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
const ll inf = 1e15;
typedef pair<ll, ll> point;
#define x first
#define y second

point transform(point p)
{
	return point(p.x + p.y, p.x - p.y);
}

int main()
{
	ll minx = inf, miny = inf, maxx = -inf, maxy = -inf;
	ios::sync_with_stdio(false);
	int N, M;
	cin >> N >> M;
	int C;
	cin >> C;
	while(C--)
	{
		point p;
		cin >> p.x >> p.y;
		p = transform(p);
		minx = min(minx, p.x);
		miny = min(miny, p.y);
		maxx = max(maxx, p.x);
		maxy = max(maxy, p.y);
	}
	ll best = inf, besti = -1;
	int H;
	cin >> H;
	for(int i = 1; i <= H; i++)
	{
		point p;
		cin >> p.x >> p.y;
		p = transform(p);
		ll dist = max(max(abs(p.x - minx), abs(p.y - miny)),
				max(abs(p.x - maxx), abs(p.y - maxy)));
		if(dist < best)
			best = dist, besti = i;
	}
	cout << best << endl << besti;
}
