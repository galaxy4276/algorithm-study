#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool solution(string s) {
int p_count = 0, y_count = 0;
for (auto c : s) {
if (c == 'p' or c == 'P') p_count++;
if (c == 'y' or c == 'Y') y_count++;
}
return p_count == y_count;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
string input;
cin >> input;
bool result = solution(input);
cout << result << endl;
}
