#include <iostream>
#include <cmath>

int main() {
  int n, x, y;
  std::cin >> n >> x >> y;
  std::cout << std::max(ceil(n * y / 100.0) - x, 0.0) << '\n';
}
