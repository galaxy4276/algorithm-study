class Solution {
  public boolean isPalindrome(String s) {
    s = s
            .toLowerCase()
            .replace(" ", "")
            .replaceAll("[^a-zA-Z0-9]", "");
    if (s.length() < 2) return true;
    System.out.println(s);
    int firstIndex = 0;
    int lastIndex = s.length() - 1;
    char first = s.charAt(firstIndex);
    char last = s.charAt(lastIndex);

    for (int i = 0; i < s.length() / 2; i++) {
      if (first != last) return false;
      first = s.charAt(++firstIndex);
      last = s.charAt(--lastIndex);
    }
    return true;
  }

  public boolean isFastDrome(String s) {
    s = s.toLowerCase().replace(" ", "");
    int firstIdx = 0, lastIdx = s.length() - 1;

    while (firstIdx < lastIdx) {
      System.out.println("first: " + s.charAt(firstIdx) + ", last: " + s.charAt(lastIdx));
      if (!Character.isLetterOrDigit(s.charAt(firstIdx)))
        firstIdx++;
      else if (!Character.isLetterOrDigit(s.charAt(lastIdx)))
        lastIdx--;
      else if (s.charAt(firstIdx) != s.charAt(lastIdx)) {
        return false;
      } else {
        firstIdx++; lastIdx--;
      }
    }

    return true;
  }

}
