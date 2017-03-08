#include <fstream>
#include <string>
#include <map>
#include <utility>
#include <iostream>

using namespace std;

bool shelf[35][35];

int main(){

	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int N, M, k, i, j, q;
	string id;
	map< string, pair< int, int > > at;
	
	fin >> N >> M >> k;

	for( i = 1; i <= N; i++ )
		for( j = 1; j <= M; j++ )
			shelf[i][j] = true;
	
	while( k-- ){
		fin >> q;
		if( q > 0 ){
			fin >> i >> j >> id;
			for( ; i <= N; i++ ){
				for( ; j <= M; j++ ){
					if( shelf[i][j] ){
						shelf[i][j] = false;
						at[id] = make_pair( i, j );
						break;
					}
				}
				if( j <= M ) break;
				j = 1;
			}
		} else {
			fin >> id;
			i = -1; j = -1;
			if( at.find( id ) != at.end() ){
				i = at[id].first; j = at[id].second;
				at.erase( id );
				shelf[i][j] = true;
			}
			fout << i << " " << j << "\n";
		}
	}
	
	return 0;
}