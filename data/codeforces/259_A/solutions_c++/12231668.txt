#include <iostream>

int main() {
  std::string s;
  while(std::cin >> s) {
    if((s != "WBWBWBWB") && (s != "BWBWBWBW")) {
      std::cout << "NO\n";
      return 0;
    }
  }
  std::cout << "YES\n";
}
