#include <bits/stdc++.h>

using namespace std;

int trap(vector<int>& height) {
  if (height.empty()) return 0;
  int left = 0, right = height.size() - 1;
  int left_max = height[left], right_max = height[right];
  int vol = 0;

  while (left < right) {
    left_max = max(left_max, height[left]);
    right_max = max(right_max, height[right]);
    if (left_max < right_max) {
      vol += left_max - height[left];
      left++;
    } else {
      vol += right_max - height[right];
      right--;
    }
  }

  return vol;
}

int main() {
  vector<int> v = { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
  cout << trap(v) << endl;
}
