class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int even_num,length=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]%2==0){
                even_num = nums[i];
                nums[i] = nums[length];
                nums[length] = even_num;              
                length++;
            }
        }
        return nums;
    }
} 
