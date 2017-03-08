#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(;T--;)
	{
		string C[5];
		map<char,int> S;
		S['A'] = 1;
		S['2'] = 2;
		S['3'] = 3;
		S['4'] = 4;
		S['5'] = 5;
		S['6'] = 6;
		S['7'] = 7;
		S['8'] = 8;
		S['9'] = 9;
		S['T'] = 10;
		S['J'] = 11;
		S['Q'] = 12;
		S['K'] = 13;


		for (int i = 0; i < 5; ++i)
			cin >> C[i];

		bool isFlush = true;
		for (int i = 1; i < 5; ++i)
			if(C[i][1] != C[i-1][1])
				isFlush = false;

		bool isStraight = false;
		bool isRoyal = true;
		bool isFour = false;
		bool isThree = false;
		bool isTwo = false;
		bool isPair = false;
		
		int seq[15] = {0};

		for (int i = 0; i < 5; ++i)
			if(C[i][0] == 'A')
				++seq[1],++seq[14];
			else
				++seq[S[C[i][0]]];

		int count = 0;
		for (int i = 0; i < 15; ++i)
			if(seq[i] > 0)
			{
				++count;
				if(count == 5)
					isStraight = true;
			}
			else
				count = 0;
		

		count = 0;
		for(int i = 10; i < 15; i++)
			if(seq[i] > 0)
				++count;
		if(count != 5)
			isRoyal = false;

		count = 0;
		for(int i = 0; i < 14; i++)
			if(seq[i] == 4)
				isFour = true;
			else if(seq[i] == 3)
				isThree = true;
			else if(seq[i] == 2)
				++count,isTwo = true;

		if(isRoyal && isFlush)
			cout << "royal flush\n";
		else if(isStraight && isFlush)
			cout << "straight flush\n";
		else if(isFour)
			cout << "four of a kind\n";
		else if(isThree && isTwo)
			cout << "full house\n";
		else if(isFlush)
			cout << "flush\n";
		else if(isStraight)
			cout << "straight\n";
		else if(isThree)
			cout << "three of a kind\n";
		else if(isTwo && count == 2)
			cout << "two pairs\n";
		else if(isTwo)
			cout << "pair\n";
		else
			cout << "high card\n";
	}
	return 0;
}