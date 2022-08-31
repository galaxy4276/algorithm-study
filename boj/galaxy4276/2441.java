import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int N = Integer.parseInt(br.readLine());
    int blankSpace = 0;

    for (int i = 0; i < N; i++) {
      for (int space = 0; space < blankSpace; space++)
        bw.write(" ");
      int starCount = N - blankSpace;
      for (int star = 0; star < starCount; star++)
        bw.write("*");
      blankSpace++;
      bw.write("\n");
    }

    bw.flush(); bw.close();
  }

}
