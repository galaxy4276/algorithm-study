class Solution {
    public int solution(String s) {
        int fCnt = 0, sCnt = 0, answer = 0;
        Character fixedChar = null;

        for (char c : s.toCharArray()) {
            if (fixedChar == null) fixedChar = c;
            if (fixedChar == c) fCnt++;
            if (fixedChar != c) sCnt++;
            if (fCnt == sCnt) {
                answer++;
                fCnt = 0;
                sCnt = 0;
                fixedChar = null;
            }
        }

      if (fixedChar != null) answer++;

      return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution("abracadabra"));
    }
}
