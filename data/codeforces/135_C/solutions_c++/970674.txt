#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
#define N 100500
char s[ N ];

int main(){
	scanf( "%s", s );
	int tam = strlen( s );
	int q0 = 0, q1 = 0;
	int p = ( tam - 2 ) / 2, m = ( tam - 2 ) - p;
	
	for( int i = 0; i < tam; ++i ){
		if( s[ i ] == '0' ) ++q0;
		else if( s[ i ] == '1' ) ++q1;
	}
	
	//00
	if( q1 <= m ) printf( "00\n" );
	
	if( q1 <= m + 1 && q0 <= p + 1 ){
		//01
		if( s[ tam - 1 ] == '1' || ( q1 != m + 1 && s[ tam - 1 ] == '?' ) )
			printf( "01\n" );
		
		//10
		if( s[ tam - 1 ] == '0' || ( q0 != p + 1 && s[ tam - 1 ] == '?' ) )
			printf( "10\n" );
	}
	
	
	//11
	if( q0 <= p ) printf( "11\n" );
	
}

