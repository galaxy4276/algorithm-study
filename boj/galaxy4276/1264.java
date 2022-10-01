import java.io.*;


public class Main {

  public static int getCorrectChar(char c) {
    c = Character.toLowerCase(c);
    if (c == 'a')
      return 1;
    else if (c == 'e')
      return 1;
    else if (c == 'i')
      return 1;
    else if (c == 'o')
      return 1;
    else if (c == 'u')
      return 1;
    else return 0;
  }

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String s = "";
    while (true) {
      int count = 0;
      s = br.readLine();
      if (s.equals("#")) break;
      for (var c : s.toCharArray())
        count += getCorrectChar(c);
      System.out.println(count);
    }
    br.close();
  }
}
