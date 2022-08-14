class Solution {
  public int maximumWealth(int[][] accounts) {
    int maxWealth = 0;
    for (int i = 0; i <= accounts.length - 1; i++) {
      int customerMoney = 0;
      for (int n : accounts[i])
        customerMoney += n;
      if (customerMoney > maxWealth) maxWealth = customerMoney;
    }

    return maxWealth;
  }
}
