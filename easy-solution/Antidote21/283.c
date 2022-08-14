void moveZeroes(int* nums, int numsSize){
    int i,j,length=0;
    for(i=0;i<numsSize;i++){
        if(nums[i]!=0){
            nums[length] = nums[i];
            length++;
        }      
    }


    for(j=length;j<numsSize;j++){
         nums[j] = 0;          
    }


    return nums;

} 
