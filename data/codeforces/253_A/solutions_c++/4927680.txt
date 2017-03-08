using namespace std;

#include<fstream>
#include<algorithm>

ifstream cin("input.txt");
ofstream cout("output.txt");

int main(){

int n,m;
cin>>n>>m;

if(n>m){

while(m){
cout<<"BG";
m--; n--;
}
while(n){
cout<<"B";
n--;
}

}else{


while(n){
cout<<"GB";
m--; n--;
}
while(m){
cout<<"G";
m--;
}

}

return 0;
}