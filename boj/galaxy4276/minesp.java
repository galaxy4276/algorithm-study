import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Integer.parseInt;

class Polynomial {
  int num;
  int index;
  Polynomial(int num, int index) { this.num = num; this.index = index; }
}


public class Main {

  public static void main(String[] args) throws IOException {
    var map = new HashMap<Integer, Integer>();
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    int polynomialCount = parseInt(br.readLine());

    for (int i = 0; i < polynomialCount; i++) {
      st = new StringTokenizer(br.readLine());
      st.nextToken();
      int cnt = parseInt(st.nextToken());
      for (int j = 0; j < cnt; j++) {
        st = new StringTokenizer(br.readLine(), " ");
        int num = parseInt(st.nextToken());
        int index = parseInt(st.nextToken());
        if (index > 100000) {
          System.out.println("Error");
          return;
        }
        int indexNum = map.getOrDefault(index, 0);
        map.put(index, num + indexNum);
      }
    }

    var storage = new ArrayList<Polynomial>();
    for (var entry : map.entrySet())
      storage.add(new Polynomial(entry.getValue(), entry.getKey()));
    List<Polynomial> result = storage.stream()
            .filter(polynomial -> polynomial.index != 0)
            .sorted((o1, o2) -> Integer.compare(o2.index, o1.index))
            .collect(Collectors.toList());
    System.out.println(result.size());
    result.forEach(polynomial -> {
      System.out.println(polynomial.num + " " + polynomial.index);
    });
  }
}
