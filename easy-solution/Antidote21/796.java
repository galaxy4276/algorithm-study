class Solution {
    public boolean rotateString(String s, String goal) {
        boolean isBoolean = false;
        for(int i=0;i<s.length();i++){
            String str = s.substring(i,s.length()) + s.substring(0,i) ; 
            System.out.println(str);
            if(goal.equals(str)){
                isBoolean = true;
                break;
            }
               
        }
        return isBoolean;

    }
}
    
