import java.util.Arrays;
class Solution {	
	public int[] sortedSquares(int[] nums) {				
	    int i;
	    int[] rstAry = nums;
	    for(i=0;i<nums.length;i++){       	
	        rstAry[i] = nums[i]*nums[i];               
	       }	    
	    Arrays.sort(rstAry);
	    return rstAry;
	 }     
}


