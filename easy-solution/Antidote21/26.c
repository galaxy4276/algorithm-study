int removeDuplicates(int* nums, int numsSize){
    int i,length = 0;
    for(i=1; i < numsSize; i++){
        if(nums[i] != nums[length]){
            length++;
            nums[length] = nums[i];
        }
    }
    return length+1;
}
