#include<iostream>
#include<queue>
using namespace std;
int main()
{
	int N,K,temp;
	priority_queue <int , vector<int> , greater<int> > q;
	cin>>N>>K;
	while(N--)
	{
		cin>>temp;
		q.push(temp);
	}
	int i=1;
	while(i<K)
	{
		q.pop();
		i++;
	}
	cout<<q.top()<<endl;
}
