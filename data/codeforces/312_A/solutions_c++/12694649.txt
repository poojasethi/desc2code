#include <iostream>

int main() {
  int n;
  std::cin >> n;
  std::cin.ignore();
  std::string s;
  int size, temp1, temp2;
  while(n--) {
    std::getline(std::cin, s);
    size = s.size();
    temp1 = s.rfind("lala.");
    temp2 = s.find("miao.");
    if((temp1 == size - 5) && (temp2 != 0)) {
      std::cout << "Freda's\n";
    }
    else if((temp1 != size - 5) && (temp2 == 0)) {
      std::cout << "Rainbow's\n";
    }
    else {
      std::cout << "OMG>.< I don't know!\n";
    }
  }
}
