import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
import static java.lang.Integer.parseInt;

class Pair {
  public int x, y;
  public Pair(int x, int y) {
    this.x = x;
    this.y = y;
  }
  int getX() { return x; }
  int getY() { return y; }
}

public class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    Queue<Pair> q = new LinkedList<>();

    int canvasHeight = parseInt(st.nextToken());
    int canvasWidth = parseInt(st.nextToken());

    var canvas = new int[canvasHeight][canvasWidth];
    var visit = new boolean[canvasHeight][canvasWidth];
    int[] dx = { 1, 0, -1, 0 };
    int[] dy = { 0, 1, 0, -1 };
    int paintCount = 0;
    int area = 0;
    int max = 0;

    for (int i = 0; i < canvasHeight; i++) {
      st = new StringTokenizer(br.readLine(), " ");
      for (int j = 0; j < canvasWidth; j++)
        canvas[i][j] = parseInt(st.nextToken());
    }

    for (int i = 0; i < canvasHeight; i++) {
      for (int j = 0; j < canvasWidth; j++) {
        if (canvas[i][j] == 0 || visit[i][j]) continue;
        paintCount++;
        q.offer(new Pair(i, j));
        visit[i][j] = true;
        area = 0;

        while (!q.isEmpty()) {
          Pair p = q.poll();
          area++;
          for (int k = 0; k < 4; k++) {
            int x = p.x + dx[k];
            int y = p.y + dy[k];
            if (x < 0 || x >= canvasHeight || y < 0 || y >= canvasWidth)
              continue;
            if (canvas[x][y] == 1 && !visit[x][y]) {
              q.offer(new Pair(x, y));
              visit[x][y] = true;
            }
          }
        }

        if (area > max) max = area;
      }
    }

    System.out.println(paintCount);
    System.out.println(max);
  }

}
