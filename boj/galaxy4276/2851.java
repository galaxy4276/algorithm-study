import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

// 2851. 슈퍼 마리오 (B1)
public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int[] mushroomLine = new int[10];
    int score = 0;

    for (int i = 0; i < mushroomLine.length; i++)
      mushroomLine[i] = Integer.parseInt(br.readLine());

    for (int mushroom : mushroomLine) {
      if (score + mushroom > 100) {
        if ((100 - score) == (score + mushroom) - 100)
          score += mushroom;
        else if ((100 - score) > ((score + mushroom) - 100)) {
          score += mushroom;
        }
        break;
      }
      score += mushroom;
    }
    bw.write(score + "\n");
    bw.flush(); bw.close();
  }

}
