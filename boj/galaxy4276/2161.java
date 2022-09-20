import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;
import static java.lang.Integer.parseInt;

public class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    int N = parseInt(st.nextToken());
    Deque<Integer> q = new LinkedList<>();

    for (int i = 1; i <= N; i++)
      q.add(i);

    while (!q.isEmpty()) {
      System.out.print(q.poll() + " ");
      if (!q.isEmpty())
        q.addLast(q.poll());
    }
  }

}
