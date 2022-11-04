#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

string JINHO;
cin >> JINHO;
int C, TC = 0;
cin >> C;
for (int i = 0; i < C; i++) {
  string T;
  cin >> T;
  int compare = JINHO.compare(T);
  if (compare == 0) TC++;
}
cout << TC << endl;
return 0;
}
