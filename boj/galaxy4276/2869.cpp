#include<iostream>

using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
int A, B, V;
cin >> A >> B >> V;

int day = 1 + ( (V - A) / (A - B) );

if ((V - A) % (A - B) != 0) day++;
if (A >= V) cout << "1";
else cout << day;
}
