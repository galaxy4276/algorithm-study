import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    var s = br.readLine();

    for (int i = 0; i < s.length(); i++) {
      bw.write(s.charAt(i));
      if (i % 10 == 9)
        bw.write("\n");
    }

    bw.flush(); bw.close();
  }

}
