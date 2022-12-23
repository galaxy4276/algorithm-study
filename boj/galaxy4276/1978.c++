#include<iostream>

using namespace std;

int main() {
int N, c = 0, num;

cin >> N;
for (int i = 0; i < N; i++) {
  cin >> num;
  for (int j = 2; j <= num; j++) {
    if (j == num) c++;
    if (num % j == 0) break;
  }
}

cout << c << "\n";
}

//int main() {
//  int N, c, total = 0, num;
//
//  cin >> N;
//  for (int i = 0; i < N; i++) {
//    cin >> num;
//    c = 0;
//    for (int j = 1; j <= num; j++)
//      if ((num % j) == 0) c++;
//    if (c == 2) total++;
//  }
//
//  cout << total << "\n";
//}
