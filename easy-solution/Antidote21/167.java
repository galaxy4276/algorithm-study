class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i,j;
        int index=0;
        int sum=0;
        int a[] = new int[2];
        int k=0;
        
        for(i=0;i<numbers.length;i++){
            sum = 0;
          
            sum += numbers[i];
            for(j=i+1;j<numbers.length;j++){
                sum += numbers[j];
                if(sum==target){
                    a[index]=i+1;
                    a[index+1]=j+1;
                    k=1;
                    break;
                    
                }
                sum -= numbers[j];
              
            }
            if(k==1)break;
           
        }
        return a;
    }
}
//Time Limit Exceeded

class Solution {
    public int[] twoSum(int[] numbers, int target) {

        int l = 0;
        int r = numbers.length-1;
        
        while(l<r)
        {
            if(numbers[l]+numbers[r]==target)
            {
                return new int[]{l+1,r+1};
            }
            else if(numbers[l]+numbers[r]>target)
            {
                r--;
            }
            else
            {
                l++;
            }
        }
        return null;
    }
}
