#include <iostream>
#include <bits/stdc++.h>
#include <stack>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  stack<char> S;
  string input;
  int total = 0;
  cin >> input;
  for (int i = 0; i < input.length(); i++) {
    if (input[i] == '(') {
      S.push(input[i]);
    } else if (input[i] == ')' && input[i - 1] == '(') {
      S.pop();
      total += S.size();
    } else {
      S.pop();
      total++;
    }
  }

  cout << total << endl;
}
