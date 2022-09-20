import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import static java.lang.Integer.parseInt;

public class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int caseCount = parseInt(br.readLine());
    char[] result = br.readLine().toCharArray();

    for (int i = 1; i < caseCount; i++) {
      char[] files = br.readLine().toCharArray();
      for (int j = 0; j < files.length; j++)
        if (files[j] != result[j])
          result[j] = '?';
        else
          result[j] = files[j];
    }

    System.out.println(result);
  }

}
