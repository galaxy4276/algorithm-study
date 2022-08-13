import java.util.Scanner;

class Solution {
  public int count = 0;
  public void question(int n) {
    this.printHelper();
    System.out.println("\"재귀함수가 뭔가요?\"");
    if (n == 0) {
      this.printHelper();
      System.out.println("\"재귀함수는 자기 자신을 호출하는 함수라네\"");
      this.printHelper();
    System.out.println("라고 답변하였지.");
      return;
    }
    this.printHelper();
    System.out.println("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.");
    this.printHelper();
    System.out.println("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.");
    this.printHelper();
    System.out.println("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"");
    this.count++;
    question(n - 1);
    this.count--;
    this.printHelper();
    System.out.println("라고 답변하였지.");
  }

  public void printHelper() {
    int n = 0;
    while (n < count) {
      System.out.print("____");
      n++;
    }
  }
  
}

class Main {  
  public static void main(String args[]) {
    Scanner scan = new Scanner(System.in);
    int n = scan.nextInt();
    System.out.println("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.");
    Solution s = new Solution();
    s.question(n);
  } 
}
