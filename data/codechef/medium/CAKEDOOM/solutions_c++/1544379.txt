/*
Doom Bakes Cakes
Problem code: CAKEDOOM
	
SUBMITMY SUBMISSIONSALL SUBMISSIONS
From the FAQ:
What am I allowed to post as a comment for a problem?

Do NOT post code.
Do NOT post a comment asking why your solution is wrong.
Do NOT post a comment asking if you can be given the test case your program fails on.
Do NOT post a comment asking how your solution can be improved.
Do NOT post a comment giving any hints or discussing approaches to the problem, or what type or speed of algorithm is required.
 
Problem Statement

Chef Doom has decided to bake a circular cake. He wants to place N colored cherries around the cake in a circular manner. As all great chefs do, Doom doesn't want any two adjacent cherries to have the same color. Chef has unlimited supply of cherries of K = 10 different colors. Each color is denoted by the digit from the set {0, 1, ..., K ? 1}. Different colors are denoted by different digits. Some of the cherries are already placed and the Chef wants you to place cherries in the remaining positions. He understands that there can be many such arrangements, so in the case when the answer is not unique he asks you to find the lexicographically smallest one.
What does it mean?
Let's numerate positions for the cherries by the numbers 1, 2, ..., N starting from one of the positions in a clockwise direction. Then the current (possibly partial) arrangement of the cherries can be represented by a string of N characters. For each position i of the arrangement if the cherry of the color C is placed at this position then the ith character of the string is equal to the digit C. Otherwise, it is equal to the question mark ?. We identify the arrangement with the string that represents it.
One arrangement is called lexicographically smaller than the other arrangement if at the first position where they differ the first one has smaller digit (we compare only complete arrangements so we don't care about relation between digits and the question mark). For example, the arrangement 1230123 is lexicographically smaller than 1231230 since they have first 3 equal characters but the 4th character in the first arrangement is 0 and it is less than 1 which is the 4th character of the second arrangement.
Notes
The cherries at the first and the last positions are adjacent to each other (recall that we have a circular cake).
In the case N = 1 any arrangement is valid as long as the color used for the only cherry of this arrangement is less than K.
Initial arrangement can be already invalid (see the case 3 in the example).
Just to make all things clear. You will be given a usual string of digits and question marks. Don't be confused by circular stuff we have in this problem. You don't have to rotate the answer once you have replaced all question marks by the digits. Think of the output like the usual string for which each two consecutive digits must be different but having additional condition that the first and the last digits must be also different (of course if N > 1).
Next, you don't have to use all colors. The only important condition is that this string should be lexicographically smaller than all other strings that can be obtained from the input string by replacement of question marks by digits and of course it must satisfy conditions on adjacent digits.
One more thing, K here is not the length of the string but the number of allowed colors. Also we emphasize that the given string can have arbitrary number of question marks. So it can have zero number of question marks as well as completely consists of question marks but of course in general situation it can have both digits and question marks.
OK. Let's try to formalize things in order to make all even more clear. You will be given an integer K and a string S=S[1]S[2]...S[N] where each S[i] is either the decimal digit less than K or the question mark. We are serious. In all tests string S can have only digits less than K. Don't ask about what to do if we have digit = K. There are no such tests at all! We guarantee this! OK, let's continue. Your task is to replace each question mark by some digit strictly less than K. If there were no question marks in the string skip this step. Now if N=1 then your string is already valid. For N > 1 it must satisfy the following N conditions S[1] ? S[2], S[2] ? S[3], ..., S[N-1] ? S[N], S[N] ? S[1]. Among all such valid strings that can be obtained by replacement of question marks you should choose lexicographically smallest one. I hope now the problem is really clear.
Input

The first line of the input file contains an integer T, the number of test cases. T test cases follow. Each test case consists of exactly two lines. The first line contains an integer K, the number of available colors for cherries. The second line contains a string S that represents the current arrangement of the cherries in the cake.
Constraints

1 = T = 1000
1 = K = 10
1 = |S| = 100, where |S| denotes the length of the string S
Each character in S is either the digit from the set {0, 1, ..., K ? 1} or the question mark ?
Output

For each test case output the lexicographically smallest valid arrangement of the cherries in the cake that can be obtained from the given arrangement by replacement of each question mark by some digit from 0 to K ? 1. If it is impossible to place the cherries output NO (output is case sensitive).
Example

Input:
7
1
?
2
?0
10
79259?087
2
??
3
0?1
4
?????
3
012

Output:
0
10
NO
01
021
01012
012
Explanation

Case 2. The only possible replacement here is 10. Note that we output 10 since we can not rotate the answer to obtain 01 which is smaller.
Case 3. Arrangement is impossible because cherries at the first and the last positions are already of the same color. Note that K = 10 but the string has length 9. It is normal. K and |S| don't have any connection.
Case 4. There are two possible arrangements: 01 and 10. The answer is the first one since it is lexicographically smaller.
Case 5. There are three possible ways to replace question mark by the digit: 001, 011 and 021. But the first and the second strings are not valid arrangements as in both of them there exists an adjacent pair of cherries having the same color. Hence the answer is the third string.
Case 6. Note that here we do not use all colors. We just find the lexicographically smallest string that satisfies condition on adjacent digit.
Case 7. The string is already valid arrangement of digits. Hence we simply print the same string to the output.
*/
#include <iostream>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <sstream>
#include <ctime>
#include <numeric>
#include <cstring>
#include <functional>

using namespace std;
int main(){
	int t;
	cin>>t;
	for(int test=0; test<t; test++){
		int k; string str;
		cin>>k>>str;
		int lastIndex = str.size()-1;

//IF SIZE(STR) IS 1
		if(str.size() == 1){
			if(str[0] == '?')
				str[0] = '0';
			cout<<str<<endl;
			continue;
		}
//NOW THE SIZE(STR) > 1		
//CHECKING IF CONSECUTIVE LETTERS ARE SAME OR K IS 1 GIVEN SIZE(STR)>1
		bool same = false;
		if(str[0] != '?' && str[0] == str[lastIndex])
			same = true;
		for(int i=1; same==false && i<str.size(); i++){
			if(str[i] != '?' && str[i-1]==str[i])
				same = true;
		}
		if(same || k==1){
			cout<<"NO\n";
			continue;
		}
		
//NOW CONSECUTIVE LETTERS ARE NOT SAME & K>=2
//IF K IS 2
		if(k==2){
			if(lastIndex%2==0){
				cout<<"NO\n";
				continue;
			}
			int posZero=-1, posOne=-1;
			for(int i=0; i<=lastIndex; i++){
				if(str[i]=='0')
					posZero = i;
				else if(str[i]=='1')
					posOne = i;
			}
			if(posZero == -1 && posOne == -1){
				for(int i=0; i<=lastIndex; i+=2)
					cout<<"01";
				cout<<endl;
			}else{
				if(posOne != -1)
					posZero = posOne+1;
				posZero %= 2;
				int itemAtZero = ((posZero==0)?(0):(1));
				for(int i=0; i<=lastIndex; i+=2){
					if(str[i] == '?')
						str[i]=(itemAtZero+'0');
					if(str[i]!=(itemAtZero+'0')){
						str="NO";
						break;
					}
				}
				for(int i=1; i<=lastIndex; i+=2){
					if(str[i] == '?')
						str[i]=(itemAtZero^1+'0');
					if(str[i]!=(itemAtZero^1+'0')){
						str="NO";
						break;
					}
				}
				cout<<str<<endl;
			}
			continue;
		}
//FIXING STR[0]		
		if(str[0] == '?'){
			bool zero = false, one = false;
			if(str[1] == '0' || str[lastIndex]=='0')
				zero = true;
			if(str[1] == '1' || str[lastIndex]=='1')
				one = true;
			if(zero == false)
				str[0] = '0';
			else if(one == false)
				str[0] = '1';
			else if(k>2)
				str[0]='2';
			else{
				cout<<"NO\n";
				continue;
			}
		}

//FIXING STR[1] TO STR[LAST_INDEX-1]
		bool done = false;
		for(int i=1; !done && i<lastIndex; i++){
			if(str[i] != '?')
				continue;
			int j;
			for(j=0; j<k; j++){
				if(j == str[i-1]-'0' || j==str[i+1]-'0')
					continue;
				break;
			}
			assert(j<3);
			if(j==k){
				cout<<"NO\n";
				done = true;
				continue;
			}
			str[i] = j+'0';
		}
		if(done)
			continue;

//FIXING STR[LAST_INDEX]
		if(str[lastIndex] == '?'){
			bool zero = false, one = false;
			if(str[0] == '0' || str[lastIndex-1]=='0')
				zero = true;
			if(str[0] == '1' || str[lastIndex-1]=='1')
				one = true;
			if(zero == false)
				str[lastIndex] = '0';
			else if(one == false)
				str[lastIndex] = '1';
			else if(k>2)
				str[lastIndex]='2';
			else{
				cout<<"NO\n";
				continue;
			}
		}
		cout<<str<<endl;
	}
	return 0;
}
