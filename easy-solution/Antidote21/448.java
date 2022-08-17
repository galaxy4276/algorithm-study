class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Arrays.sort(nums);
        List<Integer> result = new ArrayList<>();
        for(int i =0; i< nums.length; i++){
            if(nums[i] != i+1) {
                if(Arrays.binarySearch(nums, i+1)<0){
                     result.add(i+1);
                };
            }
        }
       return result;
    }
}
