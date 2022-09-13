import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    st.nextToken();
    int M = Integer.parseInt(st.nextToken());

    int left = 1;
    int right = M;
    int count = 0;
    int appleDropCount = Integer.parseInt(br.readLine());

    for (int i = 0; i < appleDropCount; i++) {
      int where = Integer.parseInt(br.readLine());

      if (left <= where && right >= where)
        continue;

      if (left > where) {
        count += left - where;
        right -= left - where;
        left = where;
      }

      if (right < where) {
        count += where - right;
        left += where - right;
        right = where;
      }

    }

    System.out.println(count);
  }

}
