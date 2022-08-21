

int dominantIndex(int* nums, int numsSize){
    int i,index=0; 
    
    for (i=1; i<numsSize; i++){
        if (nums[i] > nums[index]){
            index = i;
            }
        }
    
    for (i=0; i < numsSize; i++){
        if (index != i && nums[i]*2 > nums[index]){
            return -1;
            }
        }
    return index;

}
