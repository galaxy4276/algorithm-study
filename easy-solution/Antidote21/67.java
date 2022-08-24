
class Solution {
    public String addBinary(String a, String b) { 
        StringBuilder sb = new StringBuilder();
        //https://hardlearner.tistory.com/288
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0; //자리올림 변수 
        
        while(i >= 0 || j >= 0){
            int sum = carry;
            if(i>=0)sum += a.charAt(i) - '0';//charAt()함수 String타입을 char타입으로 변환할 때 사용한다
            if(j>=0)sum += b.charAt(j) - '0';//아스키코드를 이용하여 정수 계산
            sb.append(sum % 2);
            carry = sum / 2;
            
            i--;
            j--;
        }
        if(carry != 0)sb.append(carry);
        return sb.reverse().toString();
    }
}
