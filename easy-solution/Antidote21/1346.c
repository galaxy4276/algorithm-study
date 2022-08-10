

bool checkIfExist(int* arr, int arrSize){
    int i,j,k=0;
    
    for(i=0;i<arrSize;i++){
        if(arr[i]==0){
            ++k;
            if(k==2){
                return true;
            }
        }
    }
    
    for(i=0;i<arrSize;i++){
        for(j=0;j<arrSize;j++){
            if(arr[i] == 2*arr[j]&&arr[i]!=0){
                return true;
            }
        }
        
    }
    
    return false;
}
