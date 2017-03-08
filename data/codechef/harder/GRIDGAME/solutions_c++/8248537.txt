#include <cstdio>
#include <cassert>
#include <set>
#include <algorithm>
//#define DEBUG
using namespace std;
 
const int kNMax = 200010;
 
struct Segment {
	int l, r;
	Segment(){}
	Segment(int ll, int rr):
		l(ll), r(rr){}
	bool operator< (const Segment &S) const {
		return l < S.l;
	}
};
 
typedef set<Segment> set_t;
typedef set<Segment>::iterator itr_t;
 
set_t colS;
 
itr_t lowerBound(set_t &S, const Segment &T) {
	itr_t res = S.lower_bound(T);
	if ( res == S.end() ) {
		return S.size()?--S.end():S.end();
	}
	if ( res->l > T.l ) {
		if ( res == S.begin() ) return S.end();
		res--;
	}
	assert(res->l <= T.l);
	return res;
}
 
itr_t locate(set_t &S, int pos) {
	itr_t res = lowerBound(S, Segment(pos,pos));
	if ( res == S.end() || res->r < pos )
		return S.end();
	return res;
}
 
void snap(set_t &S, int pos) {
#ifdef DEBUG
	fprintf(stderr, "Snapping %d\n", pos);
#endif
	itr_t it = locate(S, pos);
	if ( it == S.end() ) return;
	int ll = it->l, rr = it->r;
	S.erase(it);
	if ( ll < pos ) S.insert(Segment(ll, pos-1));
	if ( pos < rr ) S.insert(Segment(pos+1, rr));
}
 
void integrate(set_t &S, Segment sg) {
#ifdef DEBUG
	fprintf(stderr, "Integrating [%d,%d]...\n", sg.l, sg.r);
	assert(locate(S, sg.l) == S.end());
	assert(locate(S, sg.r) == S.end());
	fprintf(stderr, "......before size = %d\n", S.size());
#endif
 
	itr_t pre = lowerBound(S, sg),
		  suc = S.upper_bound(sg);
	if ( pre != S.end() && suc != S.end()
			&& pre->r == sg.l-1 && suc->l == sg.r+1 ) {
		int ll = pre->l, rr = suc->r;
		S.erase(pre); S.erase(suc);
		S.insert(Segment(ll, rr));
	} else if ( suc != S.end() && suc->l == sg.r+1 ) {
		int rr = suc->r;
		S.erase(suc);
		S.insert(Segment(sg.l, rr));
	} else if ( pre != S.end() && pre->r == sg.l-1 ) {
		int ll = pre->l;
		S.erase(pre);
		S.insert(Segment(ll, sg.r));
	} else
		S.insert(Segment(sg.l, sg.r));
#ifdef DEBUG
	fprintf(stderr, "......after size = %d\n", S.size());
#endif
}
 
struct Coord {
	int x, y, id;
	bool operator< (const Coord &C) const {
		return x < C.x || (x == C.x && y < C.y);
	}
} ban[kNMax], ini[kNMax];
int ans[kNMax];
int keyRow[kNMax];
 
int main() {
//	freopen("t.in", "r", stdin);
	int TST;
	scanf("%d", &TST);
	while ( TST -- ) {
		int N, Q;
		scanf("%d", &N);
		int nKeyRow = 0;
		for ( int i = 0; i < N; i ++ ) {
			scanf("%d%d", &ban[i].x, &ban[i].y);
			keyRow[nKeyRow++] = ban[i].x;
		}
		scanf("%d", &Q);
		for ( int i = 0; i < Q; i ++ ) {
			scanf("%d%d", &ini[i].x, &ini[i].y);
			ini[i].id = i;
			keyRow[nKeyRow++] = ini[i].x;
		}
		sort(ban, ban+N);
		sort(ini, ini+Q);
		sort(keyRow, keyRow+nKeyRow);
		nKeyRow = unique(keyRow, keyRow+nKeyRow)-keyRow;
 
		int banPtr = 0, iniPtr = 0, curRow = -1;
		colS.clear();
 
		for ( int i = 0; i < nKeyRow; i ++ ) {
#ifdef DEBUG
			fprintf(stderr, "curRow = %d\n", curRow);
#endif
			if ( curRow < keyRow[i]-1 ) {
#ifdef DEBUG
				fprintf(stderr, "jumping to %d\n", keyRow[i]-1);
#endif
				int need = keyRow[i]-curRow-1, pre = -1;
				for ( itr_t it = colS.begin(); it != colS.end(); it ++ ) {
					int prov = it->l-pre-1;
					if ( prov > need ) {
						integrate(colS, Segment(pre+1, pre+need));
						need = 0;
						break;
					} else if ( prov > 0 ) {
						integrate(colS, Segment(pre+1, pre+prov));
						it = locate(colS, pre+1);
						need -= prov;
					}
					pre = it->r;
				}
				if ( need > 0 ) {
					integrate(colS, Segment(pre+1, pre+need));
				}
			}
#ifdef DEBUG
			fprintf(stderr, "Processing row %d\n", keyRow[i]);
#endif
			curRow = keyRow[i];
 
			static int blk[kNMax];
			int nBlk = 0;
			blk[nBlk++] = -1;
			while ( banPtr < N && ban[banPtr].x == curRow ) {
				snap(colS, ban[banPtr].y);
				blk[nBlk++] = ban[banPtr].y;
				banPtr++;
			}
			sort(blk, blk + nBlk);
 
			static set<int> zero;
			zero.clear();
 
			for ( int j = 0; j < nBlk; j ++ ) 
				if ( j == nBlk-1 || blk[j]+1<blk[j+1] ) {
					itr_t it = locate(colS, blk[j]+1);
					if ( it == colS.end() ) {
						zero.insert(blk[j]+1);
						integrate(colS, Segment(blk[j]+1, blk[j]+1));
					} else if ( j == nBlk-1 || it->r+1 < blk[j+1] ) {
						zero.insert(it->r+1);
						integrate(colS, Segment(it->r+1, it->r+1));
					}
				}
 
			while ( iniPtr < Q && ini[iniPtr].x == curRow ) {
				ans[ini[iniPtr].id] = zero.count(ini[iniPtr].y) == 0;
				iniPtr++;
			}
		}
 
		for ( int i = 0; i < Q; i ++ )
			printf("%s\n", ans[i]?"Alice":"Bob");
	}
} 