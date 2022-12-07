#include <iostream>
#include <bits/stdc++.h>
#include <stack>

using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
stack<char> S;
int t_count = 0, s_count = 0;
string T;
cin >> T;
string ST;
cin >> ST;

for (int i = ST.length() - 1; i >= 0; i--) {
  char c = ST[i];
  if (c == 't') t_count++;
  else s_count++;
  S.push(ST[i]);
}

while (t_count != s_count) {
  if (S.top() == 't') t_count--;
  else s_count--;
  S.pop();
}

while (!S.empty()) {
  cout << S.top();
  S.pop();
}
cout << endl;
}
