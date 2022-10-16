import java.io.*;
import java.util.Arrays;

public class Main {
  public static int getPrice(int time, int per, int price) {
    int div = time / per;
    int rest = time % per;
    return div * price + (rest >= 0 ? price : 0);
  }

  public static int getPriceByCallTimes(int[] total, int per, int price) {
    int result = 0;
    for (int j : total) result += getPrice(j, per, price);
    return result;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    br.readLine();
    String[] s = br.readLine().split(" ");
    int[] total = Arrays.stream(s).mapToInt(Integer::parseInt).toArray();
    int Y = getPriceByCallTimes(total, 30, 10);
    int M = getPriceByCallTimes(total, 60, 15);
    if (Y == M)
      System.out.println("Y M " + Y);
    else if (Y > M)
      System.out.println("M " + M);
    else
      System.out.println("Y " + Y);
  }
}
