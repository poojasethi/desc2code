#include <iostream>
#include <cmath>

int main() {
  int k, a, b, v;
  std::cin >> k >> a >> b >> v;
  std::cout << std::max(std::ceil((float) a / v - b), std::ceil((float) a / (v * k))) << '\n';
}
