#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int B, P;
cin >> B >> P;
B /= 2;
if (B == P) {
  cout << B << endl;
} else if (B < P) {
  cout << B << endl;
} else {
  cout << P << endl;
}

return 0;
}
