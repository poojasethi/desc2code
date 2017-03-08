#include <bits/stdc++.h>

using namespace std;

int input_length(char input[]){
	int len = 0;
	for(len = 0; input[len]!='\0'; len++);

	return len;
}

unsigned long long toDecimal(string binary){
	
	unsigned long long x = 0, power = 0, decimal;

	x = atoi(binary.c_str());

	while(x){
		decimal += 0;
		power++;
		x/=10;
	}

	
	return decimal;
}

int main(){

	char input[1000];

	int flag = 0;
	//bool 
	string binary = "";
	unsigned long long int number = 0;

	do{
		//initial
		/*scanf("%s", input);
		int len = input_length(input);
		flag = len % 2;

		//ignore "">
		char x;
		do{
			w
		}while(x)
		*/
		scanf("%s", input);


		//if(input[0] != '"'){
			if(input[0] == '#'){
				//case ends
				//output
				//cout << "ans:" << binary << endl;
				number = strtoull(binary.c_str(), NULL, 2);
				cout << number << endl;
				//clean up
				binary = "";
				number = 0;
			}
			else{
				int len = input_length(input);
				//printf("%s:%d\n", input,len);
				if(len == 1 || len == 2){
					flag = len % 2; // 0 -> 1, 1 -> 0
					//cout << "f:"<< flag << endl;
				}
				else{
					int temp_len = len - 2;
					while(temp_len--){
						if(flag == 0){
							binary.append("0");
							//number = number  << 2;
						}
						else if(flag == 1){
							binary.append("1");
							//number = number || 1;
						}
					}
				}
			}
		//}

//       68421 
// 27 =  11011
		

	}while(*input != '~');


	return 0;
}