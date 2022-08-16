class Solution {
    public int heightChecker(int[] heights) {
        int i,cnt=0;
        int[] expected = new int[heights.length];
        for(i=0;i<heights.length;i++){
            expected[i] = heights[i];
        }
        Arrays.sort(expected);
        for(i=0;i<heights.length;i++){
            if(expected[i] != heights[i]){
                cnt++;
            }
        }
        return cnt;
    }
  
}
