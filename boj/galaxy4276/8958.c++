#include<cstdio>

using namespace std;

int t;
char s[81];

int main() {
scanf("%d", &t);
while (t--) {
  int score = 0, tmp = 0;
  scanf("%s", s);
  for (int i = 0; i < s[i]; i++)
    s[i] == 'O' ? score += ++tmp : tmp = 0;
  printf("%d\n", score);
}
}


//int main() {
//  ios::sync_with_stdio(false);
//  cin.tie(nullptr);
//
//  int total;
//  cin >> total;
//  string arr[total];
//  int score = 0, temp_sc = 0;
//  for (int i = 0; i < total; i++)
//    cin >> arr[i];
//  for (string s : arr) {
//    for (char c : s) {
//      if (c == 'O') {
//        temp_sc++;
//        score += temp_sc;
//      } else { temp_sc = 0; }
//    }
//    cout << score << "\n";
//    score = 0;
//    temp_sc = 0;
//  }
//
//}
