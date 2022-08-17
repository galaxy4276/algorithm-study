class Solution {
    public int thirdMax(int[] nums) {
        Arrays.sort(nums);
        int prev = nums[0];
        int index = 1;
        for (int i=1; i<nums.length; i++) {
            if (prev == nums[i]) {
                continue;
            }
            prev = nums[i];
            nums[index++] = nums[i]; 
        }

        if (index < 3) {
            return nums[index-1];
        }
        
        return nums[index-3];
    }
}
