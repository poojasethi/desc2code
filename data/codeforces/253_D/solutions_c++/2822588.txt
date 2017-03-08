# include <stdio.h>
# include <fstream>
# include <string.h>

using namespace std;

FILE * fin = fopen("input.txt","r");
ofstream fout("output.txt");

int n,m,k;
char c[450][450];
int t[450][450];
int d[50];
long long ans=0;

int main()
{
	fscanf(fin,"%d %d %d",&n,&m,&k);
	
	for(int h=0; h<n; h++)
		fscanf(fin,"%s",c[h]);
		
	for(int h=1; h<=n; h++)
	{
		
		for(int j=1; j<=m; j++)
		{
			if(c[h-1][j-1]=='a')
				t[h][j]=1;
				
			t[h][j]+=t[h][j-1];
		}
	}
	
	for(int h=1; h<=m; h++)
		for(int j=1; j<=n; j++)
			t[j][h]+=t[j-1][h];
	
	for(int h=0; h<n; h++)
		for(int j=h+1; j<n; j++)
		{
			memset(d,0,sizeof(d));
			
			int x=0,y=1;
			
			if(c[h][0]==c[j][0])
				d[c[h][0]-97]++;
			
			while(y<m)
			{
				if(k<t[j+1][y+1]+t[h][x]-t[j+1][x]-t[h][y+1])
				{
					if(c[h][x]==c[j][x])
						d[c[h][x]-97]--;
					x++;
					
					if(x==y)
						y++;
					
					continue;
				}
				
				if(c[h][y]==c[j][y])
				{
					
					if(x!=y)
						ans+=d[c[h][y]-97];
					
					d[c[h][y]-97]++;
				}
				
				y++;
			}
		}
		
	fout<<ans;
}
