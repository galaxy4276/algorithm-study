class Solution {
    public int[] replaceElements(int[] arr) {
        int i,tmp,max=-1; 
        for(i=arr.length-1;i>=0;i--){
            tmp= arr[i];
            arr[i]=max;
            if(tmp>max){
                max=tmp;
            }
        }
        return arr;
    }
}

class Solution {
    public int[] replaceElements(int[] arr) {
        for(int i = 0; i < arr.length; i++){
            if(i==arr.length-1){
                arr[arr.length-1] = -1;
                break;
            }
            
            int max=arr[i+1];
            for (int j = i+1; j < arr.length-1; j++){
                if(arr[j]<arr[j+1]){
                    max=Math.max(max,arr[j+1]);
                }
            }
            
            arr[i]=max;
        }
        
        return arr;
    }
}
