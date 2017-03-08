#include<bits/stdc++.h>

using namespace std;

typedef long long LI;
typedef long double DL;

DL calc(DL r1, DL r2, DL d) {
	DL ang1 = acos((r1*r1 + d*d - r2*r2) / (2*r1*d));
	DL ang2 = acos((r2*r2 + d*d - r1*r1) / (2*r2*d));
	DL a1 = r1*r1*(ang1 - sin(ang1)*cos(ang1));
	DL a2 = r2*r2*(ang2 - sin(ang2)*cos(ang2));
	return a1 + a2;
}

int main() {
	LI x1, y1, r1, x2, y2, r2;
	cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
	LI dx = x2-x1, dy=y2-y1, rr=r1+r2, d2 = dx*dx + dy*dy;
	cout << setprecision(12);
	if(d2 >= rr*rr) {
		cout << 0.0 << endl;
		return 0;
	}
	DL d = sqrt((DL)d2);
	if(d + (DL)min(r1, r2) <= (DL)max(r1, r2)) {
		cout << M_PI*(double)(min(r1, r2)*min(r1, r2)) << endl;
		return 0;
	}

	cout << calc(r1, r2, d) << endl;
	return 0;
}
