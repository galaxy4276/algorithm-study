#include<iostream>
#include<bits/stdc++.h>

using namespace std;

bool vis[501][501];
int paint[501][501];
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, -1, 0, 1 };

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, m;
queue<pair<int, int>> Q;
int area, max_area = 0, ans = 0;
cin >> n >> m;

for (int i = 0; i < n; i++)
  for (int j = 0; j < m; j++)
    cin >> paint[i][j];

for (int i = 0; i < n; i++) {
  for (int j = 0; j < m; j++) {
    if (vis[i][j] || paint[i][j] == 0) continue;
    ans += 1;
    vis[i][j] = 1;
    area = 0;
    Q.push({ i, j });

    while (!Q.empty()) {
      area += 1;
      auto cur = Q.front(); Q.pop();
      for (int dir = 0; dir < 4; dir++) {
        int nx = cur.first + dx[dir];
        int ny = cur.second + dy[dir];
        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
        if (vis[nx][ny] || paint[nx][ny] != 1) continue;
        vis[nx][ny] = 1;
        Q.push({ nx, ny });
      }
    }
    max_area = max(max_area, area);
  }
}

cout << ans << "\n" << max_area;
}
