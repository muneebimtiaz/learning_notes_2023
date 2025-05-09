#include <iostream>
using namespace std;
// The function that calls itself inside a £unction body again and again.
int sum(int k) {
  if (k > 0) {
    return k + sum(k - 1);
  } else {
    return 0;
  }
}

int main() {
  int result = sum(10);
  cout << result;
  return 0;
}
/*
We know. each function has some local variables that exist only inside that function. When a function
is called recursively, then for each call a new set of local variables is created(except static), their name
is same bu't they are stored at different places and contain different values. These values are remembered
by the compiler till the end of function call, so that these values are available in the unwinding phase.
*/