#include <iostream>


int main(){
  int a, b, c, d;

    std::cin >> a >> b >> c >> d;

  //geometric
  if(a*c == b*b && b*d == c*c)
    //geometric
    std::cout << ((b*d) % a ? 42 : (d*b)/a) << std::endl;
  else if(a-b == b-c && b-c == c-d)
    std::cout << d+(d-c) << std::endl;
  else
    std::cout << 42 << std::endl;
  
  return 0;
}
