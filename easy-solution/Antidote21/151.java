class Solution {
    public String reverseWords(String s) {
        String[] splitStr = s.trim().split("\\s+");
        StringBuilder sb = new StringBuilder();
        for(int i=splitStr.length-1;i>=0;i--){
            sb.append(splitStr[i]);
            if(i!=0)sb.append(" ");
        }
        return sb.toString();
    }
}
