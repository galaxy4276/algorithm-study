#include<iostream>

using namespace std;

int fact(int n) {
if (n <= 0) return 1;
if (n == 1) return n;
return n * fact(n - 1);
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
int N;
cin >> N;
cout << fact(N) << "\n";
}
