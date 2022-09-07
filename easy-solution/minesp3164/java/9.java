class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        if(x == 0){
            return true;
        }
        else{
            int start = 0;
            int end = x.length()-1;
            strx = str(x);
            while (start < end){
                if (strx.charAt(start++) != strx.charAt(end--)) return false;
            }
            return true;
        }
    }
}